#!/usr/bin/env python3
''' A Python3 Module '''

import math
import csv
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' Simple helper function '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        """ Simple pagination """
        dataset = self.dataset()

        assert isinstance(page, int) and page > 0

        assert isinstance(page_size, int) and page_size > 0

        try:
            start_index, end_index = index_range(page, page_size)
            return dataset[start_index:end_index]
        except Exception:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Hypermedia pagination """

        assert isinstance(page, int) and page > 0

        assert isinstance(page_size, int) and page_size > 0

        data = []

        with open("Popular_Baby_Names.csv") as f:
            reader = csv.reader(f)
            for role in reader:
                data.append(role)
        data = data[1:]
        total_pages = math.ceil(len(data) / page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": data[(page - 1) * page_size:page * page_size],
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
