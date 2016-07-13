def hows_the_parrot():
    print("He's pining for the fjords!")

hows_the_parrot()

def lumberjack(name):
    if name.lower() == 'saul':
        print("Saul's a lumberjack and he's OK!")
    else:
        print("{} sleeps all night and {} works all day!".format(name, name))

lumberjack("Saul")
lumberjack("Waldemar")
lumberjack("Saul Waldemar")

def lunarjet(name, pronoun):
    print("{}'s a lunar and {} doing jet!".format(name, pronoun))

lunarjet("Saul", "S's")
lunarjet("Saul Waldemar", "Saul")

def average(num1, num2):
    return(num1+num2) / 2

avg = average(2, 8)
print(avg) # this exports int, not float
