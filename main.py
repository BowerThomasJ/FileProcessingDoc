def information():
    fileName = input("What is the file name: ")
    firstName = input("What is your first name: ")
    address = input("What is your street address: ")
    phone = input("What is your phone number: ")

    fileSave(fileName, firstName, address, phone)


def fileSave(fileName, firstName, address, phone):
    with open(fileName, 'w') as newFile:
        newFile.write(firstName + ',' + address + ',' + phone)

    with open(fileName) as readFile:
        for line in readFile:
            print(line)


# Call the information() function to start the process
information()