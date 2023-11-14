import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data=pd.read_csv('test.csv')

dat=data.head(1000)

any_null_values = dat.isnull().any().any()

print(any_null_values)

plt.boxplot(x = dat['Square'])
plt.show()
plt.xlabel('Square')
plt.ylabel('LifeSquare')
plt.hist(x = dat['Square'], bins = 4, orientation = "horizontal",ec = "blue")
plt.show()

data.fillna(0, inplace = True)

a = dat.isnull().any().any()

print(a)

room_counts = data.groupby('Rooms').size().reset_index(name='Количество квартир')

print("Количество квартир для каждого числа комнат:")
print(room_counts)

pivot_table = pd.pivot_table(dat, values = 'Id', index = 'DistrictId', columns = 'Rooms', aggfunc = 'count',fill_value = 0)

print("Сводная таблица:")
print(pivot_table)

dat.to_csv('surname.csv')