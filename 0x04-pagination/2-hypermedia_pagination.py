#!/usr/bin/env python3
"""Pagination"""

import csv
import math
from typing import List


index_range = __import__("0-simple_helper_function").index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Simple pagination"""
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        rang = index_range(page, page_size)
        data = self.dataset()
        return [] if (rang[0] > len(data) - 1) \
            or (rang[1] > len(data) - 1) else data[rang[0]:rang[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Hypermedia pagination"""
        data = self.get_page(page, page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": page + 1 if data else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": math.ceil(len(self.__dataset) / page_size)
        }
