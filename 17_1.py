#Задача A
import pandas as pd


def length_stats(text):
    text = ''.join(i for i in text if i.isalpha() or i == ' ')
    arr = sorted(set(text.lower().split()))
    s = pd.Series([len(i) for i in arr], index=arr)
    return s 