fileName = input("what is the file name")
firstName = input("What is your first name")
address = input("What is your street address name")
phone = input("what is your phone number")

with open(fileName, 'w') as newFile:
    newFile.write(firstName + ',' + address + ',' + phone)

with open(fileName) as readFile:
    for line in readFile:
        print(line)
