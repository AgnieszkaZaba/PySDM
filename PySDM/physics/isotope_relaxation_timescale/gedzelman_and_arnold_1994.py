""" eq. 24 in [Gedzelman and Arnold 1994](https://doi.org/10.1029/93JD03518) """


class GedzelmanAndArnold1968:  # pylint: disable=too-few-public-methods
    def __init__(self, _):
        pass

    @staticmethod
    # pylint: disable=too-many-arguments
    def tau(const, e_s, D, M, vent_coeff, radius, alpha, temperature):
        return (
                radius * const.rho_w * alpha / 3 / vent_coeff / D / e_s / M * const.R_str * temperature
        )
