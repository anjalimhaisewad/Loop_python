user=int(input("enter a no"))
n=len(str(user))
sum=0
i=user
while user>0:
    a=user%10
    b=a**n
    sum=sum+b
    user=user//10
if sum==i:
    print(sum,"it is armstrong no")
else:
    print(sum,"it is not armstrong no")
    