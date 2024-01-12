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
    