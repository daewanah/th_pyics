# The dictionary will be something like:
# {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewhere
# too!
#
# Your code goes below here.

def most_classes(dict):
    most_class = "" # holds the name of teach with most class
    max_count = 0 # max counter for classes
    for teacher in dict:
        if len(dict[teacher]) > max_count:
            max_count = len(dict[teacher])
            most_class = teacher
    return most_class

def num_teacher(dicts):
    t_teacher = 0
    for key in dicts.keys():
        t_teacher += 1
    return t_teacher
