#!/usr/bin/env python3
'''Task 12's module.
'''
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''validates piece of code and apply any necessary changes
    '''
    zoomed_in: List = [
        item for item in lst
        for x  in range(int(factor))
    ]
    return zoomed_in


arr = (12, 72, 91)

zoom_2x = zoom_array(arr)

zoom_3x = zoom_array(arr, 3)
