#!/usr/bin/env python3
"""Pagination"""


def index_range(page, page_size):
    """Simple helper function"""
    return page_size * page - page_size, page_size * page
