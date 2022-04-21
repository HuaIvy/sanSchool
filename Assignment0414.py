# -*- coding: utf-8 -*-

print('******作業1 終極密碼******')
import random

ans = random.randint(1,100)
guess = -1

start = 1
end = 100

while True:
    guess = int(input("請輸入{}~{}之間猜數字".format(start,end)))
    if guess == ans:
        print("您猜對了，數字是:",ans)
        break
    elif guess > ans:
        end = guess 
        print("數字太大了")
    else:
        start = guess
        print("數字太小了")

print("程式執行完畢")   


print('******作業2 因數分解******')


number = int(input("請輸入正整數 因數分解"))
txt = ""
i = 2

while number>1:
    while number%i==0:
        if txt == "":
            txt+= str(number)+'='+str(i)
        else:
            txt+= 'x'+str(i)
        number/=i    
    i+=1

print(txt)                



print('*****作業3 有四個數字，1,2,3,4 能組成多少個互不相同且無重覆數字的三位數')
import itertools
mylist1=list(itertools.permutations([1,2,3,4],3)) #排列
print(mylist1)
print('有',(len(mylist1)),'種組合')

print()
print("老師解法:")
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            if x!=y and y!=z and z!=x:
                print("{}{}{}".format(x,y,z),end=' ')            


# print('**********作業4 分數序列**************')

print()
print("老師解法:")

num = [1,2]
for i in range(2,21):
    num.append(num[i-2]+num[i-1])
print(num)

sum = 0
for i in range(20):
    sum += num[i+1] / num[i]
    print("{}/{}".format(num[i+1],num[i]),end=' ')
print(sum)        


print('******作業5 ******')

# step = [1,3,5,7,5,3,1]
# for i in step:
#     print()
#     print("{:^7}".format('*'*i),end='')


for i in range(1,8,2):
    print()
    print("{:^7}".format('*'*i),end='')    

for i in range(5,0,-2):
    print()
    print("{:^7}".format('*'*i),end='')  

print()
print("老師解法: ")

star = ""

for i in range(1,8,2):
    for x in range(i):
        star+='*'
    print("{:^7}".format(star))   
    star = ""     

for i in range(5,0,-2):
    for x in range(i):
        star+='*'
    print("{:^7}".format(star))   
    star = ""                

      



