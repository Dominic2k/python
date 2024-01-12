# import re
import calendar

def displayMenu():
    print("                    ---------------------------------------------")
    print("                    -                                           -")
    print("                    -                                           -")
    print("                    -         Chuong trinh thong minh           -")
    print("                    -                                           -")
    print("                    -                                           -")
    print("                    ---------------------------------------------")
    print()
    print("                    ====================MENU====================")
    print()
    print("Xin vui lòng chọn: ")
    print("1. Xem lịch. ")
    print("2. Tính lương: ")
    print("3. Xem lương: ")
    print("4. Xem thông tin nhân viên: ")
    print("5. Tính điểm của học sinh: ")
    print("6. Thoát chương trình: ")

def dayOfMonth(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        print("Tháng",month, "có 31 ngày")
    elif month in [4, 6, 9, 11]:
        print("Tháng",month, "có 30 ngày")
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print("Tháng",month, " có 29 ngày")
        else:
            print("Tháng",month, "có 28 ngày")

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

def viewInfoStaff(nameStaff):
    firstName = ""
    lastName = ""
    fullName = ""
    countSpace = 0
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

def countScores(listMain):
    sumCoefficient = 0
    sumScores = 0
    sumAvg = 0
    for i in range(len(listMain)):
        sumCoefficient = sumCoefficient + listMain[i][1]
        sumScores = sumScores + listMain[i][0]
        sumEachScores = listMain[i][0] * listMain[i][1]
        sumAvg = sumAvg + sumEachScores
        avg = sumAvg / sumCoefficient
    
    print("Tổng số môn học: ", len(listMain))
    print("Tổng số hệ số: ", sumCoefficient)
    print("Điểm trung bình của môn học: ", format(avg, ".2f"))


while True:
    try:
        displayMenu()
        choice  = int(input("Nhập lựa chọn của bạn: "))
        if choice == 1:
        #1. Xem lịch : Kiểm tra tháng có bao nhiêu ngày
            
            while True:
                try:
                    month = int(input("Nhập tháng muốn kiểm tra: (1-12) "))
                    while month <= 0 or month >= 13:
                        month = int(input("Nhập lại tháng muốn kiểm tra: (1-12) "))
                    viewFullCalendar = input("Bạn có muốn xem lịch đầy đủ không? (Y/N)")
                    if viewFullCalendar == "Y" or viewFullCalendar == "y":
                        yearInViewCalendar = int(input("Nhập năm: "))
                        dayOfMonth(month,yearInViewCalendar)
                        print(calendar.month(yearInViewCalendar, month))
                    else:
                        if month == 2:
                            yearInViewCalendar = int(input("Nhập năm: "))
                            dayOfMonth(month,yearInViewCalendar)
                        else:
                            yearInViewCalendar = 2000
                            dayOfMonth(month,yearInViewCalendar)
                    confirm = input("Bạn có muốn tiếp tục không? (Y/N): ")
                    if confirm == "N" or confirm == "n":
                        break
                    
                except ValueError:
                    print("Bạn phải nhập một số nguyên từ (1-12). Hãy thử lại.")
        elif choice == 2:
        #2. Tính lương: Nhập số giờ và lương mỗi giờ để tính tổng lương
            
            while True:    
                try:
                    salaryPerHour = int(input("Nhập tiền lương mỗi giờ: "))
                    while salaryPerHour < 0:
                        salaryPerHour = int(input("Nhập lại tiền lương mỗi giờ: "))
                    hour = float(input("Nhập số giờ làm: "))
                    while hour < 0:
                        hour = float(input("Nhập lại số giờ làm: "))
                    print("Tổng lương: ",countSalalry(hour, salaryPerHour),"VND")
                    confirm = input("Bạn có muốn tiếp tục không? (Y/N): ")
                    if confirm == "N" or confirm == "n":
                        break
                    
                except ValueError:
                    print("Bạn phải nhập lương và giờ là số. Hãy thử lại.")
        elif choice == 3:
        #3. Xem lương: Nhập tên và lương theo thứ tự ngẩu nhiên, hiển thị kết quả đã sắp xếp từ nhỏ tới lớn.
            
            while True:
                try:
                    listSalary = []
                    numberOfStaff = int(input("Nhập số lượng nhân viên: "))
                    for i in range(numberOfStaff):
                        eachStaff = []
                        for i in range(1):
                            name = input("Nhập tên nhân viên: ")
                            eachStaff.append(name)
                            salary = int(input("Nhập lương nhân viên: "))
                            eachStaff.append(salary)
                        listSalary.append(eachStaff)
                    print(["      Tên nhân viên      "],["  Lương  "])
                    for i in range(len(viewSalary(listSalary))):    
                        print(viewSalary(listSalary)[i])
                    confirm = input("Bạn có muốn tiếp tục không? (Y/N) ")
                    if confirm == "N" or confirm == "n":
                        break
                    
                except ValueError:
                    print("Bạn phải nhập đúng kiểu dữ liệu. Hãy thử lại")
        elif choice == 4:
        #4.Format tên: Nhậptên nhân viên, in ra tên đã được viết hoa chưa cái đầu, tên họ lót và tên của nhân viên.
            
            while True:
                nameStaff = str(input("Nhập tên nhân viên: "))
                hasNumber = False
                for i in nameStaff:
                    if "0" <= i <= "9":
                        hasNumber = True
                        break
                    else:
                        hasNumber = False
                if hasNumber == True:
                    print("Tên không được chưa số. Hã nhập lại")
                else:
                    viewInfoStaff(nameStaff)
                    
                confirm = input("Bạn có muốn tiếp tục không? (Y/N)" )
                if confirm == "N" or confirm == "n":
                    break
        elif choice == 5:
        #5. Tính điểm trung bình: 
            
            while True:
                try:
                    listMain = []
                    numberOfSubject = int(input("Nhập số lượng môn học: "))
                    for i in range(numberOfSubject):
                        eachSubject = []
                        for j in range(1):
                            scores = float(input("Nhập điểm từng môn: (0-10)"))
                            while scores < 0 or scores > 10:
                                scores = float(input("Nhập lại điểm vừa nhập: (0-10)"))
                            eachSubject.append(scores)
                            coefficient = float(input("Nhập hệ số từng môn: (1,2,3,1.5,2.5)"))
                            while coefficient not in [1,2,3,1.5,2.5]:
                                coefficient = float(input("Nhập lại hệ số vừa nhập: (1,2,3,1.5,2.5)"))
                            eachSubject.append(coefficient)
                        listMain.append(eachSubject)
                    countScores(listMain)
                    confirm = input("Bạn có muốn tiếp tục không? (Y/N) ")
                    if confirm == "N" or confirm == "n":
                        break
                    
                except ValueError:
                    print("Bạn phải nhập số lượng và điểm theo yêu cầu. Hãy thử lại!")
        elif choice == 6:
            print("Tạm biệt! Hẹn gặp lại!")
            break
        else:
            print("Bạn phải nhập các số từ 1 đến 6")
        
    except ValueError:
        print("Bạn phải nhập số từ 1 đến 6. Hãy thử lại!")
        
        

        
        
        
        
        
        
        
        
    
    
    
