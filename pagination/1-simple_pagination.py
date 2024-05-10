#!/usr/bin/env python3
""" Pagination with Python """
import csv
import math
from typing import List, Tuple


def index_range(page, page_size: int) -> Tuple[int, int]:
    """ Calculates the index range to start """
    start_index = (page - 1) * page_size

    end_index = start_index + page_size - 1

    return start_index, end_index


class Server:
    """ Server class to paginate a database of popular baby names. """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ Constructor init for Server class """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
                self.__dataset = dataset[1:]
        return self.__dataset


def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
    """ Gets a page from the dataset """
    assert isinstance(page, int) and page > 0
    assert isinstance(page_size, int) and page_size > 0

    dataset = self.dataset()
    total_rows = len(dataset)

    start_index, end_index = index_range(page, page_size)

    if start_index >= total_rows or start_index < 0:
        return []

    return dataset[start_index:end_index + 1]