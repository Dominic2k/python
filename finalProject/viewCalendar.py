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

