i=int(input("enter a no"))
n=i
sum=0
while i>0:
    sum=sum+(i%10)
    i=i//10
    if n%sum==0:
        print(sum,"it is harshad no")
    else:
        print(sum,"it is not harshad no")