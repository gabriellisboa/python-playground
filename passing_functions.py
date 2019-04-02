def methodception(another):
    return another()

def add_two_numbers():
    return 33 + 77

#print(methodception(add_two_numbers))
#print(methodception(lambda: 33 + 77))

my_list = [10, 20, 60, 120]

print(list(filter(lambda x: x != 20, my_list)))

(lambda x: x * 3)(5)

def not_ten(x):
    return x != 10

print(list(filter(not_ten, my_list)))

print([x for x in my_list if x != 120])