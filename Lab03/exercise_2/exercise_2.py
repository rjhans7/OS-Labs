import os
import random
import string
from datetime import datetime, timedelta

# Data
KB = 1024
MB = KB * KB
var_size = 200 * MB
filename = "data/file.txt"
exec_time = timedelta(minutes = 2)

# File
f = open(filename, "r+")

# Utility functions
def max_rand_pos():
    file_size = os.stat(filename).st_size
    result = file_size - (var_size)
    return result

def get_rand_pos():
    return random.randint(1, max_rand_pos())

def get_rand_char():
    return random.choice(string.ascii_letters)

# Exercise functions
def random_read():
    pos = get_rand_pos()
    f.seek(pos, 0)
    f.read(var_size)

def random_write():
    pos = get_rand_pos()
    char = get_rand_char()
    f.seek(pos, 0)
    f.write(char * var_size)

def seq_read():
    f.read(var_size)

def seq_write():
    char = get_rand_char()
    f.write(char * var_size)

# Test each exercise function
def test_random_read():
    now = datetime.now()
    until = now + exec_time
    while now <= until:
        random_read()
        now = datetime.now()

def test_random_write():
    now = datetime.now()
    until = now + exec_time
    while now <= until:
        random_write()
        now = datetime.now()

def test_seq_read():
    now = datetime.now()
    until = now + exec_time
    f.seek(0, 0)
    while now <= until:
        seq_read()
        now = datetime.now()

def test_seq_write():
    now = datetime.now()
    until = now + exec_time
    f.seek(0, 0)
    while now <= until:
        seq_write()
        now = datetime.now()

def test_random_read_variable_size():
    var_size = random.randint(1, 500 * MB)
    now = datetime.now()
    until = now + exec_time
    while now <= until:
        random_read()
        now = datetime.now()

def test_random_write_variable_size():
    var_size = random.randint(1, 500 * MB)
    now = datetime.now()
    until = now + exec_time
    while now <= until:
        random_write()
        now = datetime.now()


test_random_read()
print ("Done 1!")
#test_random_write()
#print ("Done 2!")
#test_seq_read()
#print ("Done 3!")
#test_seq_write()
#print ("Done 4!")
#test_random_read_variable_size()
#print ("Done 5!")
#test_random_write_variable_size()
#print ("Done all!")
f.close()
