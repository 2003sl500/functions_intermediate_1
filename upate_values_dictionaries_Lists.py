x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def changeList():
    indexfirst = 0
    for index0 in x:
        indexsecond = 0
        for index1 in index0:
            if index1 == 10:
                x[indexfirst][indexsecond] = 15 
            indexsecond = indexsecond + 1
        indexfirst = indexfirst + 1
    return x

def changeStudents():
    index = 0
    for x in students:
        if x["last_name"] == "Jordan":
            students[index].update({"last_name": "Bryant"})
            index = index + 1
    return students

def changeSportsDirectory():
    for x in sports_directory:
        index = 0 
        for y in sports_directory[x]:
            if y == "Messi":
                sports_directory[x][index] = "Andres"
            index = index + 1
    print(sports_directory, "\n")

def changeValue():
    print("Before:", z)
    index = 0
    for x in z:
        for y in x:
            if x[y] == 20:
                x[y] = 30
           
    print("After:", z, "\n")

print(changeList(), "\n")
print(changeStudents(), "\n")
changeSportsDirectory()
changeValue()