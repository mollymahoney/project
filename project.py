inputName = input("What is your name?")
print(inputName)


inputSchoolLevel = input("Are you in High School or College? ")
print(inputSchoolLevel)


listGrades = []

for thing in range(numOfClasses):
    classInput = int(input("What grades did you make? "))
    listGrades.append(classInput)

print(listGrades)



listClass = []
numOfClasses = int(input("How many classes are you taking? "))
for thing in range(numOfClasses):
    classInput = input("What classes are you taking? ")
    print(classInput)
