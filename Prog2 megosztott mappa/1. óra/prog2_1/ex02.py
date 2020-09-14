# 2. Exercise
# Write a Python program to construct the following pattern, using a
# nested for loop


def drawPattern():
    pattern = ''
    for i in range(5):
       pattern+='*'
       print(pattern)
       if i == 4:
           for j in range(5):
               pattern = pattern[:-1]
               print(pattern)

drawPattern()