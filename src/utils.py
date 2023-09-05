def flatten(arr):
    res = {}

    for item in arr:
        res.update(item)
    return res
