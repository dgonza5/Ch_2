# num1 = 1
# num2 = 10
# num3 = 1000
# sum_of_all_numbers = num1 + num2 + num3

# print("Sum is {0:n}".format(sum_of_all_numbers))

# list_of_numbers = [1, 10, 1000]
# # print(sum(list_of_numbers))
# print(list_of_numbers) # [1, 10, 1000]
# list_of_numbers.clear()
# print(list_of_numbers) # [1, 10, 1000]
# list_of_numbers.append(100)
# list_of_numbers.append(100)
# list_of_numbers.append(100)
# list_of_numbers.append(100)
# list_of_numbers2 = [3, 100, 5]

# #Adding/concatenating arrays .extend
# list_of_numbers.extend(list_of_numbers2)
# print(list_of_numbers) #

# # Adding/concatenating arrays using +
# l1 = [1, 32, 4]
# l2 = [100, 200, 300]
# l3 = l1 + l2
# print(l3)

# words = ["Spam", "Wink", "Hi", "My", "In"]
# words.insert(len(words), "Hello")

# print("Words======>", words)

## Calculate average of grades
# grades = []     # Create the variable grades and assign it the empty list. 

# num = float(input("Enter the first grade: "))
# grades.append(num)

# num = float(input("Enter the second grade: "))
# grades.append(num)

# num = float(input("Enter the third grade: "))
# grades.append(num)

# num = float(input("Enter the fourth grade: "))
# grades.append(num)

# num = float(input("Enter the fifth grade: "))
# grades.append(num)

# min_grade = min(grades)
# grades.remove(min_grade)

# min_grade = min(grades)
# grades.remove(min_grade)

# average = sum(grades) / len(grades)

# print("Average Grade: {0:.2f}".format(average))

# grades.append(1)
# grades.append(2)
# grades.append(4)
# grades.append(9)

# print("grades", grades)

# length = len(grades) #
# print("length", length)
# print("sliced:", grades[2:3])
# str1= "a,b,c"
# parts = str1.split(",")

# print("parts: ", parts)

# lines = ["To", "be", "or", "not", "to", "be"]

# print("lines before join: ", lines)

# joined = "-".join(lines)

# print("joined: ", joined)

# Open up the Data.txt file in read mode
# infile = open("Data.txt", "r")

# print("infile", infile)
# names = []
# # Using the for loop to populate the names array with names
# for line in infile:
#     # print("line: ", line)
#     # print("line after striping the right side: ", line.rstrip())
#     names.append(line.rstrip())

# print("names: ", names)
# names_using_list_comprehension = [line.rstrip() for line in infile]

# print("names_using_list_comprehension: ", names_using_list_comprehension)
# # Close the Data.txt file to perserve memory
# infile.close()


# infile = open("Grades.txt", 'r')

# for line in infile:
#     print("line: ", eval(line))

# infile.close()


# infile = open("Grades.txt", 'r')

# list_of_numbers = [eval(line) for line in infile]

# print("list_of_numbers: ", list_of_numbers)

# infile.close()


list_of_names = ("Dionicio", "John", ["A", (1, 2, 3), "B", "C"])

print("list_of_names", list_of_names[2][1][-1])