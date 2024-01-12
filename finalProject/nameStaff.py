# import re
def viewInfoStaff(nameStaff):
    firstName = ""
    lastName = ""
    fullName = ""
    countSpace = 0
    listFullName = []
    eachWordInFullName = []
    firstNameTmp = ""
    #Viết hoa
    for i in range(len(nameStaff)):
        if i == 0 or nameStaff[i - 1] == " ":
            fullName = fullName + nameStaff[i].upper()
        else:
            fullName = fullName + nameStaff[i].lower()
    #Lấy tên
    for i in range(len(fullName) - 1, -1, -1):
        if fullName[i] != " ":
            firstNameTmp = firstNameTmp + fullName[i]
        else:
            break
    for i in range(len(firstNameTmp) - 1, -1,-1):
        firstName = firstName + firstNameTmp[i]
        
    #Lấy họ
    for i in range(len(fullName)):
        if fullName[i] == " ":
            countSpace = countSpace + 1
    if countSpace == 1:
        timeSpace = 0       
        for k in range(len(fullName)):
            if fullName[k] == " ":
                timeSpace = timeSpace + 1
            lastName = lastName + fullName[k]
            if timeSpace == 1:
                break
        print("Họ và tên lót của nhân viên là: ", lastName)
        print("Tên của nhân viên là: ", firstName)
        print("Họ tên đầy đủ của nhân viên là: ", fullName)
    elif countSpace == 2:
        timeSpace = 0
        for m in range(len(fullName)):
            if fullName[m] == " ":
                timeSpace = timeSpace + 1
            lastName = lastName + fullName[m]
            if timeSpace == 2:
                break
        print("Họ và tên lót của nhân viên là: ", lastName)
        print("Tên của nhân viên là: ", firstName)
        print("Họ tên đầy đủ của nhân viên là: ", fullName)
    elif countSpace == 3:
        timeSpace = 0
        for n in range(len(fullName)):
            if fullName[n] == " ":
                timeSpace = timeSpace + 1
            lastName = lastName + fullName[n]
            if timeSpace == 3:
                break
        print("Họ và tên lót của nhân viên là: ", lastName)
        print("Tên của nhân viên là: ", firstName)
        print("Họ tên đầy đủ của nhân viên là: ", fullName)
    elif countSpace == 4:
        timeSpace = 0
        for h in range(len(fullName)):
            if fullName[h] == " ":
                timeSpace = timeSpace + 1
            lastName = lastName + fullName[h]
            if timeSpace == 4:
                break
        print("Họ và tên lót của nhân viên là: ", lastName)
        print("Tên của nhân viên là: ", firstName)
        print("Họ tên đầy đủ của nhân viên là: ", fullName)
    else:
        print("Tên không được quá ngắn hoặc quá dài!")

    

            
        


