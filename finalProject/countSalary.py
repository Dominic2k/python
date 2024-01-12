def countSalalry(hour, salaryPerHour):
    if hour <= 40:
        totalSalary = hour * salaryPerHour
        
        strTotalSalary = str(int((totalSalary)))
        resultTotalSalary = ""
        countCharacter = 0
        for i in range(len(strTotalSalary) -1, -1, -1):
            countCharacter = countCharacter + 1
            if countCharacter % 3 != 0:
                resultTotalSalary = resultTotalSalary + strTotalSalary[i]
            else:
                resultTotalSalary = resultTotalSalary + strTotalSalary[i]
                resultTotalSalary = resultTotalSalary + "."
        finalSalary = ""
        for j in range(len(resultTotalSalary) - 1, -1, -1):
            finalSalary = finalSalary + resultTotalSalary[j]
        if finalSalary[0] == ".":
            finalSalary = finalSalary[1:len(finalSalary)+1]
            
        return finalSalary
    else:
        totalSalary = 40 * salaryPerHour
        moreSalary = (hour - 40) * salaryPerHour * 1.5
        salaryAfterSum = totalSalary + moreSalary
        
        strTotalSalary = str(int((salaryAfterSum)))
        resultTotalSalary = ""
        countCharacter = 0
        for i in range(len(strTotalSalary) -1, -1, -1):
            countCharacter = countCharacter + 1
            if countCharacter % 3 != 0:
                resultTotalSalary = resultTotalSalary + strTotalSalary[i]
            else:
                resultTotalSalary = resultTotalSalary + strTotalSalary[i]
                resultTotalSalary = resultTotalSalary + "."
        finalSalary = ""
        for j in range(len(resultTotalSalary) - 1, -1, -1):
            finalSalary = finalSalary + resultTotalSalary[j]
        if finalSalary[0] == ".":
            finalSalary = finalSalary[1:len(finalSalary)+1]
        
        return finalSalary
    
        