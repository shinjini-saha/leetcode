def quicksort(a: list[int]) -> None:
    quicksort_helper(a, 0, len(a) - 1)


# start_idx, end_idx inclusive
def quicksort_helper(a: list[int], start_idx: int, end_idx: int) -> None:
    if end_idx <= start_idx:
        return
    midpoint_idx = start_idx + (end_idx - start_idx + 1) // 2
    pivot = a[midpoint_idx]
    a[end_idx], a[midpoint_idx] = pivot, a[end_idx]

    smaller_ptr = start_idx
    bigger_ptr = end_idx - 1
    while True:
        while a[smaller_ptr] <= pivot and smaller_ptr < end_idx:
            smaller_ptr += 1
        while a[bigger_ptr] >= pivot and bigger_ptr > start_idx:
            bigger_ptr -= 1

        if bigger_ptr <= smaller_ptr:
            break

        a[smaller_ptr], a[bigger_ptr] = a[bigger_ptr], a[smaller_ptr]

    a[smaller_ptr], a[end_idx] = a[end_idx], a[smaller_ptr]

    quicksort_helper(a, start_idx, smaller_ptr - 1)
    quicksort_helper(a, smaller_ptr + 1, end_idx)


def quicksort_copy(_a: list[int]) -> list[int]:
    a = _a[:]
    if len(a) <= 1:
        return a

    midpoint_idx = len(a) // 2
    end_idx = len(a) - 1
    pivot = a[midpoint_idx]
    a[end_idx], a[midpoint_idx] = pivot, a[end_idx]

    smaller_ptr = 0
    bigger_ptr = end_idx - 1
    while True:
        while a[smaller_ptr] <= pivot and smaller_ptr < end_idx:
            smaller_ptr += 1
        while a[bigger_ptr] >= pivot and bigger_ptr > 0:
            bigger_ptr -= 1

        if bigger_ptr <= smaller_ptr:
            break

        a[smaller_ptr], a[bigger_ptr] = a[bigger_ptr], a[smaller_ptr]

    a[smaller_ptr], a[end_idx] = a[end_idx], a[smaller_ptr]

    a_smaller = quicksort_copy(a[:smaller_ptr])
    a_larger = quicksort_copy(a[smaller_ptr + 1 :])
    a = [*a_smaller, pivot, *a_larger]
    return a
