# 作業一
# 請用 for  來處理
# data = [100,80,90,70,59,30,21,35]

# 請排序它，==> 從小到大 => [21,30,35,59,70,80,90,100]
# 請排序=> 從大到小  => [100,90,80,70,59,35,30,21]

print("******作業一 排序從大到小 從小到大********")

dataOrder = [100,80,90,70,59,30,21,35]

print('原始順序:',dataOrder)

# 找出陣列中最大的值
def findMax(dataOrder):
    max = dataOrder[0]
    for i in dataOrder:
        if i > max:
            max = i 
    del dataOrder[dataOrder.index(max)]   
    return max,dataOrder

totalMax = len(dataOrder)
dataMax = dataOrder
maxList = []

while totalMax>0: 
    max,dataMax = findMax(dataMax)
    maxList.append(max)
    totalMax-=1        
print('由大到小',maxList)

print('由小到大',maxList[-1:(-1*len(maxList))-1:-1])  


# 作業二  data =  [10,20,30,25,50,60]
# 請反轉內容  ==> [60,50,25,30,20,10]

print("*******作業二  反轉內容*******")
data =  [10,20,30,25,50,60]
print("原始順序:",data)
print("反轉後:",data[-1:-7:-1])


# 作業三。額外練習題
# 巴斯卡三角形 ，請用一簡串來處理