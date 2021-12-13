"""

"""
import numpy as np
from .attribute import Attribute


class DummyAttribute(Attribute):
    def __init__(self, builder, name):
        super().__init__(builder, name)

    def allocate(self, idx):
        super().allocate(idx)
        self.data[:] = np.nan

    def get(self):
        return self.data


def make_dummy_attribute_factory(name):
    def _factory(builder):
        return DummyAttribute(builder, name=name)
    return _factory
