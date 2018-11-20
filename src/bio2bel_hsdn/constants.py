# -*- coding: utf-8 -*-

"""Constants for Bio2BEL HSDN."""

import os

from bio2bel import get_data_dir

__all__ = [
    'VERSION',
    'MODULE_NAME',
    'DATA_DIR',
    'get_version',
    'HSDN_PATH',
    'HSDN_URL',
]

VERSION = '0.0.1'
MODULE_NAME = 'bio2bel_hsdn'
DATA_DIR = get_data_dir(MODULE_NAME)


def get_version() -> str:
    """Get the software version."""
    return VERSION


HSDN_URL = 'https://raw.githubusercontent.com/dhimmel/hsdn/gh-pages/data/symptoms-DO.tsv'
HSDN_PATH = os.path.join(DATA_DIR, 'symptoms-DO.tsv')
