dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for x in dojo:
        index = 0
        print(len(dojo[x]), x)
        for y in dojo[x]:
            print(y)
        print()

printInfo(dojo)