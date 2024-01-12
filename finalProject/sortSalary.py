def viewSalary(listSalary):    
    for i in range(0,len(listSalary) - 1):
        for j in range(i + 1, len(listSalary)):
            if listSalary[i][1] > listSalary[j][1]:
                tmp = listSalary[i]
                listSalary[i] = listSalary[j]
                listSalary[j] = tmp
            for i in range(len(listSalary)):
                sumSpaceName = 25 - len(listSalary[i][0])
                listSalary[i][0] = listSalary[i][0] + (sumSpaceName * " ")
            for i in range(len(listSalary)):
                sumSpaceSalary = 10 - len(str(listSalary[i][1]))
                listSalary[i][1] = str(listSalary[i][1]) + (sumSpaceSalary * " ")
    return listSalary
    
    
    
    
    

    # newList = []                          
    # n = 0
    # minSalary = listSalary[0][1]
    # while n < len(listSalary) - 1:
    #     for i in range(len(listSalary)):
    #         if listSalary[i][1] < minSalary:
    #             minSalary = listSalary[i][1]
                
    #     if minSalary == listSalary[n][1]:
    #         newList.append(listSalary[n])
    #         listSalary.pop(n)
    #     n = n + 1
    # return newList
# myList = [["Dat", 1000],["Vinh", 9000],["Minh", 5000]]
           