my_set = {1,2,3}
my_set.add(4)
print(my_set)

# set add only unique values

my_set = {1,2,3}
my_set.add(3)
print(my_set)

# list add give type error

# my_set.add(['4'])
# print(my_set)


# remove element from set

my_set.remove(2)
print(my_set)

# discard element from set
my_set_discard={1,2,3}
my_set_discard.discard(4)
print(my_set_discard)

# discard element from set
my_set_clear={1,2,3}
my_set_clear.clear()
print(my_set_clear)
# set with del method

my_set_del = {1,2,3}
del my_set_del # we never use print for my_set_del because the variable deleted

# set sorting

set_sortings = {1,2,3}
print(set_sortings)

# using pop method

my_set_pop =set("world")
print(my_set_pop.pop(),my_set_pop)

# union set with updated
my_set_num = {1,2,3}
my_set_nums = {3,4,5}
my_set_num.update(my_set_nums)
print(my_set_num)

