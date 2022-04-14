# -*- coding: utf-8 -*-
print("*********第一個作業***********")
for x in range(1,6):
    for y in range(x):
        print(x,end='')
    print()   

"""
第一個作業
1
22
333
4444
55555  
"""   

print("********第二個作業************")

for x in range(5,0,-1):
    for y in range(x):
        print(x,end='')
    print()  

"""
第二個作業
55555
4444
333
22
1  
"""

print("*******第三個作業*************")

for x in range(9,0,-2):
    for y in range(x):
        print(x,end='')
    print() 
"""
第三個作業
999999999
7777777
55555
333
1
"""
print("***********第四個作業****************")

"""
第四個作業
求質數    ： 可以被  1  及 自己 整數的數稱為質數
請輸入１～１００之間的質數有那些

4 是質數????   不是；因為他被 1  、2  、4  整數
5 是質數???    是：因為他只被 1  及 5 整數
"""


for i in range(1,101):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i,end=" ")





