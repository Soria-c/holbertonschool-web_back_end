#!/usr/bin/env python3
"""Pagination"""

import csv
import math
from typing import List, Dict


index_range = __import__("0-simple_helper_function").index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

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

    def get_hyper_index(self, index: int = None, page_size: int = 10):
        """Deletion-resilient hypermedia pagination"""
        data = self.indexed_dataset()
        assert index <= len(data)
        next_index = index + page_size
        page_data = []
        current_idx = index

        while current_idx < next_index:
            if data.get(current_idx, None):
                page_data.append(data[current_idx])
            else:
                next_index += 1
            current_idx += 1

        return {
            'index': index,
            'data': page_data,
            'page_size': page_size,
            'next_index': next_index
        }
