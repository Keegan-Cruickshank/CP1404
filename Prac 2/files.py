user_name = input("What is yor name? ")
name_file = open("name.txt", "w")
print(user_name, file=name_file)
name_file.close()

name_file = open("name.txt", "r")
user_name = name_file.readline()
print("Your name is {}".format(user_name), end="")
name_file.close()


numbers_file = open("numbers.txt", "r")
running_total = 0
for line in numbers_file:
    running_total += int(line)
print("The running total of the file was: {}".format(running_total))

