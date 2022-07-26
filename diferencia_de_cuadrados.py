def diffSquares(n):
    count1=0
    count2=0
    for i in range(n):
        i+=1
        count1+=i
        count2+=i**2
    print((count1**2)-count2)
diffSquares(10)
