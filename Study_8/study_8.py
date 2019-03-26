import os

file_list = os.listdir('./DB')
with open('./DB/{}'.format(file_list[0])) as f:
    temp = f.read()

print(temp.count('제어봉'))


