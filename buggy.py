my_list = [5, 2, 1, True, "abcdefg", 3, False, 4]

import pdb; pdb.set_trace() # only for this and get rid of after use
del my_list[3] # [5, 2, 1,"abcdefg", 3, False, 4]
del my_list[3] # [5, 2, 1, True, 3, False, 4]
del my_list[4] # [5, 2, 1, True, 3, 4]
print(my_list)
