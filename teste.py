import pandas as pd


def recur(end):
    print(end)
    if end <= 1:
        return end
    return recur(end - 1)


recur(900)