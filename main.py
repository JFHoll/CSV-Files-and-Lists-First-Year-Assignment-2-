import csv

#Part 1
ls = ["Hello", "Hi", "bye"]

file = open('assignment2.csv', 'w+', newline='')

with file:
    write = csv.writer(file)
    write.writerow(ls)
file.close()

#Part 2
list2 = []

file = open('assignment2.csv', 'r+', newline='')

with open('assignment2.csv', newline='') as csvfile:
    data = csv.reader(csvfile)
    for item in data:
        list2.append(item)


print(list2)