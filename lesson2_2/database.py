def insert(filename, key, value):
    f = open(filename, 'a')
    f.write(key + '\t' + value + '\n')
    f.close()

def find(filename, key):
    f = open(filename, 'r')
    for row in f:
        (k, v) = row.split('\t', 1)
        if k == key:
            return v[:-1]
        if k not in f:
            return 'Your name was not listed in the directory.'
    f.close()

def delete(filename, key):
    f = open(filename, 'r')
    result = open('result.txt', 'w')
    for row in f:
        (k, v) = row.split('\t', 1)
        if k != key:
            result.write(row)
            return 'The name and the phone number are deleted.'
        else:
            return 'Your name was not listed in the directory.'
    f.close()
    result.close()
    import os
    os.replace('result.txt', filename)

def update(filename, key, value):
    f = open(filename, 'r')
    result = open('result.txt', 'w')
    for row in f:
        (k, v) = row.split('\t', 1)
        if k == key:
            result.write(key + '\t' + value + '\n')
        else:
            result.write(row)
    f.close()
    result.close()
    import os
    os.replace('result.txt', filename)
    
