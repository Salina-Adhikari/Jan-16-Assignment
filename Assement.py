

from collections import deque
tasks=deque(['Do Homework','Wash Dishes','Iron Clothes'])
tasks_1=tasks.append('Make Dinner')
print(tasks)
tasks_2=tasks.remove('Iron Clothes')
print(tasks)
tasks.rotate(2)
print(tasks)

from collections import Counter
about_Counter="hi i am Salina i like food .hi nice to meet you.My friend like to eat food.Do you like to eat food"
word_counter = Counter(about_Counter.split())
print(word_counter)
print(word_counter.most_common(3))

from collections import defaultdict


product_inventory = defaultdict(list)

product_inventory["laptop"].extend(["dell", "acer"])
product_inventory["Phone"].extend(["oppo", "popo"])
product_inventory["dishes"].extend(["cup", "mug"])


def add_product(category, product):
    product_inventory[category].append(product)


add_product("Electronics", "tablet")
add_product("Phone", "samsung")
add_product("Books", "novel")    


for category, products in product_inventory.items():
    print(f"{category}: {', '.join(products)}")

import numpy as np
one_arrry=np.array([2,3,4,5])
print(np.mean(one_arrry))
print(np.sum(one_arrry))
print(np.std(one_arrry))
multiply=one_arrry*2
print(multiply)

First=np.array([[3,4],[9,4]])
Second=np.array([[6,7],[4,6]])
total=np.dot(First,Second)
print(total)





