# question asked in Fintech
"""Write a program to Merge overlapping intervals."""


def merge_interval(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


if __name__ == '__main__':
    arr = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # arr = [[1,3]]
    print(merge_interval(arr))
