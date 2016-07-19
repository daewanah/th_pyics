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

def most_classes(dicts):
    most_class = "" # holds the name of teach with most class
    max_count = 0 # max counter for classes
    for teacher in dicts:
        if len(dict[teacher]) > max_count:
            max_count = len(dicts[teacher])
            most_class = teacher
    return most_class

def num_teachers(dicts):
    t_teacher = 0
    for key in dicts.keys():
        t_teacher += 1
    return t_teacher

def stats(dicts):
    my_list = []
    for key, value in dicts.items():
        a_list = [key, len(value)]
        my_list.append(a_list)
    return my_list

def courses(dicts):
    courseList = []
    for classes in dicts.values():
        courseList.extend(classes)
    return courseList
