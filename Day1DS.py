#Create Lists and Integers and uses Methods

numbers=[1,3,5,7,9]
numbers.append(11)
print(numbers)
numbers.remove(5)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

# Create a tuple and access elements, then concatenate two tuples. 

color = ('Green', 'Black', 'Yellow', 'White')

print(color[0])

mix_colors = color + ('Brown', 'Purple', 'Blue')
Green, Black, Yellow, White = color
print(mix_colors)

#Create a set, perform union, intersection, and difference operations.
my_set = {1, 3,8, 5, 7, 9} 
my_set.add(4)
my_set.remove(5)
print(my_set)
another_set={19,9,8,7,6,5,11}
print(another_set)
union_set = my_set.union(another_set)
print(union_set)
common_el= my_set.intersection(another_set)
print(common_el)
difference_set=my_set.difference(another_set)
print(difference_set)

#Create a dictionary, update values, and delete keys.
student = {'Name': 'Tariq', 'Age':21, 'Grade':'A'}
print(student)
student['Age']=23
student['Semester'] = '6th'
print(student)
del student['Age']
print(student)

#Generate a list of squares using list comprehension.
squares = [x**2 for x in range(1,6)]
print(squares)

#Create a dictionary where the keys are numbers and the values are their cubes. 
cube = {x : x**3 for x in range(1,5)}
print(cube)

# Write and read data from a text file. 
with open('example.txt', 'w') as file: 
    file.write("Hello, this is a test file.") 
    file.write("\n Hi This is Tariq Gul")
with open('example.txt', 'r') as file: 
    content = file.read() 
print(content) 

#Open file
with open('A.docx', 'w') as file:
    file.write("Hello, This is the Word Documents")
with open('A.docx', 'r') as file:
    printContent= file.read()
print(printContent)

#Combine two lists into a dictionary
students = ['Tariq','Ali', 'Amjad','Awais']
grades = ['A','A1', 'B', 'C']
studentGrades =dict(zip(students,grades))
print(studentGrades)

#Create and manipulate a nested dictionary. 

student = {'Name': 'Tariq', 'Age': 23 , 'subject' : {'Math':'A', 'Physics':'B'}}
print(student)
print(student['subject']['Math'])

#Perform set operations such as union, intersection, and difference.
set1 = {1,2,4,6,8}
set2 = {2,3,4,5,7,9,}

Union =set1.union(set2)
Intersection=set1.intersection(set2)
differenceSet=set1.difference(set2)
print(f'Union : {Union} , Intersection : {Intersection}, Difference : {differenceSet}')











