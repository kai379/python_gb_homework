# | Задание 44 |
# | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
#
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() |


import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})


unique_values = data['whoAmI'].unique()
data_one_hot = pd.DataFrame()

for i in unique_values:
    data_one_hot[i] = ((data['whoAmI']) == i).astype(int)

data_one_hot.head(10)
