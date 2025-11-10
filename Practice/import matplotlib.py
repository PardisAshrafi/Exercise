import matplotlib
from bidi.algorithm import get_display
from arabic_reshaper import reshape
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
import io


######### تعداد سفارش هر شهر چندتاست؟ بیست شهر اول################


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
dataset = pd.read_csv(
    r"C:\Users\pardis\Desktop\digikala\orders.csv", encoding='utf-8')

print(dataset.shape)

dataset_location = dataset['city_name_fa']
orders = dataset_location.value_counts()
print(orders)

orders = orders.to_dict()

cityes = list(orders.keys())[:21]
amount = list(orders.values())[:21]

cityes.reverse()
amount.reverse()


matplotlib.rc('xtick', labelsize=10)
matplotlib.rc('ytick', labelsize=10)
matplotlib.rc('font', family='B Nazanin')

cityes_fa = [get_display(reshape(label)) for label in cityes]
plt.style.use('fivethirtyeight')
plt.barh(cityes_fa, amount, color='red')
plt.show()
