"""
Created at 23.04.2020

@author: Piotr Bartman
@author: Sylwester Arabas
"""


import numpy as np

from PySDM.particles_builder import ParticlesBuilder
from PySDM.dynamics import Condensation
from PySDM.environments import MoistLagrangianParcelAdiabatic
from PySDM.physics import formulae as phys
from PySDM.initialisation.r_wet_init import r_wet_init
from PySDM.state.products.particles_size_spectrum import ParticlesSizeSpectrum

# TODO: the q1 logic from PyCloudParcel?


class Simulation:
    def __init__(self, setup):

        dt_output = setup.total_time / setup.n_steps  # TODO: overwritten in jupyter example
        self.n_substeps = 1  # TODO:
        while (dt_output / self.n_substeps >= setup.dt_max):
            self.n_substeps += 1
        self.bins_edges = phys.volume(setup.r_bins_edges)
        particles_builder = ParticlesBuilder(backend=setup.backend, n_sd=setup.n_sd)
        particles_builder.set_environment(MoistLagrangianParcelAdiabatic, {
            "dt": dt_output / self.n_substeps,
            "mass_of_dry_air": setup.mass_of_dry_air,
            "p0": setup.p0,
            "q0": setup.q0,
            "T0": setup.T0,
            "w": setup.w,
            "z0": setup.z0
        })

        r_wet = r_wet_init(setup.r_dry, particles_builder.particles.environment, np.zeros_like(setup.n), setup.kappa)
        particles_builder.register_dynamic(Condensation, {
            "kappa": setup.kappa,
            "coord": setup.coord,
            "adaptive": setup.adaptive,
            "rtol_x": setup.rtol_x,
            "rtol_thd": setup.rtol_thd,
        })
        attributes = {'n': setup.n, 'dry volume': phys.volume(radius=setup.r_dry), 'volume': phys.volume(radius=r_wet)}
        products = {ParticlesSizeSpectrum: {}}
        self.particles = particles_builder.get_particles(attributes, products)

        self.n_steps = setup.n_steps

    # TODO: make it common with Arabas_and_Shima_2017
    def save(self, output):
        cell_id = 0
        output["r_bins_values"].append(self.particles.products["Particles Size Spectrum"].get(self.bins_edges))
        volume = self.particles.state['volume']
        volume = self.particles.backend.to_ndarray(volume)  # TODO
        output["r"].append(phys.radius(volume=volume))
        output["S"].append(self.particles.environment["RH"][cell_id] - 1)
        output["qv"].append(self.particles.environment["qv"][cell_id])
        output["T"].append(self.particles.environment["T"][cell_id])
        output["z"].append(self.particles.environment["z"][cell_id])
        output["t"].append(self.particles.environment["t"][cell_id])

    def run(self):
        output = {"r": [], "S": [], "z": [], "t": [], "qv": [], "T": [], "r_bins_values": []}

        self.save(output)
        for step in range(self.n_steps):
            self.particles.run(self.n_substeps)
            self.save(output)
        return output