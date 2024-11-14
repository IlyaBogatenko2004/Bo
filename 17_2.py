#Задача B
import pandas as pd


def length_stats(text):
    text = ''.join(i for i in text if i.isalpha() or i == ' ')
    arr = sorted(set(text.lower().split()))
    arr_odd = [i for i in arr if len(i) % 2]
    arr_even = [i for i in arr if not len(i) % 2]
    odd = pd.Series([len(i) for i in arr_odd], index=arr_odd, dtype='int64')
    even = pd.Series([len(i) for i in arr_even], index=arr_even, dtype='int64')
    return odd, even