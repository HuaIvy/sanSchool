# -*- coding: utf-8 -*-

print('******作業1 終極密碼******')
import random

ans = random.randint(1,100)
guess = -1

start = 1
end = 100

while True:
    guess = int(input("請輸入1-100之間的數字來猜數:"))
    if guess == ans:
        print("您猜對了，數字是:",ans)
        break
    elif guess > ans:
        end = guess 
        print("數字太大了，請輸入{}~{}之間".format(start,end))
    else:
        start = guess
        print("數字太小了，請輸入{}~{}之間".format(start,end))

print("程式執行完畢")   


# print('******作業2 因數分解******')



print('*****作業3 有四個數字，1,2,3,4 能組成多少個互不相同且無重覆數字的三位數，各是多少**************')
import itertools
mylist1=list(itertools.permutations([1,2,3,4],3)) #排列
print(mylist1)
print('有',(len(mylist1)),'種組合')


print('**********作業4 分數序列**************')




print('******作業5 ******')

step = [1,3,5,7,5,3,1]
for i in step:
    print()
    print("{:^7}".format('*'*i),end='')

      



