my_tuple = (1, 2, 3)
my_tuple
# >>> (1, 2, 3)
my_second_tuple = 1, 2, 3
my_second_tuple
# >>> (1, 2, 3)
my_third_tuple = tuple([1, 2, 3])
my_third_tuple
# >>> (1, 2, 3)
my_third_tuple[1]
# >>> 2
my_third_tuple[1] = 5
# >> TypeError
dir(tuple)
# To show the attributes of tuple
