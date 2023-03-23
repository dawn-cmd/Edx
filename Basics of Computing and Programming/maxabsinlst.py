from typing import List


def max_abs_val(arr: List) -> int:
    return max([abs(i) for i in arr])