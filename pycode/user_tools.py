import random

ft_in_mile = 5280
m_in_km = 1000
name = ['Tom', 'Jerry', 'Happy', 'Arnold']

def get_file(filename):
    return filename[filename.index('.')+1:]

def roll_dice(num):
    return random.randint(1, num)