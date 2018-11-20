# -*- coding: utf-8 -*-

"""Parsers and downloaders for Bio2BEL HSDN."""

from bio2bel.downloading import make_df_getter
from .constants import HSDN_PATH, HSDN_URL

__all__ = ['get_hsdn_df']

get_hsdn_df = make_df_getter(
    HSDN_URL,
    HSDN_PATH,
    sep='\t',
)
