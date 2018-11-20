# -*- coding: utf-8 -*-

"""Test cases for Bio2BEL HSDN."""

import os

from bio2bel.testing import AbstractTemporaryCacheClassMixin
from bio2bel_hsdn import Manager

__all__ = [
    'TemporaryCacheClass',
]

HERE = os.path.abspath(os.path.dirname(__file__))
TEST_MESH_DESCRIPTORS_PATH = os.path.join(HERE, 'test_mesh_descriptors.xml')


class TemporaryCacheClass(AbstractTemporaryCacheClassMixin):
    """A test case containing a temporary database and a Bio2BEL HSDN manager."""

    Manager = Manager
    manager: Manager

    @classmethod
    def populate(cls):
        """Populate the Bio2BEL HSDN database with test data."""
        raise NotImplementedError
