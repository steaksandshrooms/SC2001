import random

x = 10**6
size_list = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000, 5000000, 10000000]
datasets = {}
for i in size_list[:2]:                                 #remove 2 in submission. 2 is for testing
    ind_list = [random.randint(1, x) for _ in range(i)]
    """truncated version of 
    s_data = []
    for i in range(1000):
        data.append(random.randint(1, x))
    """
    datasets[i] = ind_list

print(datasets)

