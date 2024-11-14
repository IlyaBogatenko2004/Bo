#Задача C
import pandas as pd


def cheque(price_list, **kwargs):
    my_products = sorted(kwargs)
    product_dict = {
        'product': my_products,
        'price': [price_list[i] for i in my_products],
        'number': [kwargs[i] for i in my_products]
    }
    product_dict['cost'] = [price_list[i] * product_dict['number'][ind] for ind, i in enumerate(my_products)]
    s = pd.DataFrame(product_dict)
    return s