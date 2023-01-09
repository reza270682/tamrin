#چاپ مثلث
#رضا عزيزالهي
#يکشنبه ها از 7:45 تا 10

n = int(input("enter your number : "))
m = 0
for i in range (n):
    print(m * "*")
    m+=1
for i in range(n):
    print(m * "*")
    m-=1
