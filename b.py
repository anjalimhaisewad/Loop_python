# amount = int(input("enter the amount"))
# if amount>=2000:
#     n_2000=amount//2000
#     print(2000,"=",n_2000)
# if amount>=500:
#     n_500=amount//500
#     print(500,"=",n_500) 
# if amount>=200:
#     n_200=amount//200
#     print(200,"=",n_200)
# if amount>=100:
#     n_100=amount//100
#     print(100,"=",n_100)
# if amount>=50:
#     n_50=amount//50
#     print(50,"=",n_50)
# if amount>=20:
#     n_20=amount//20
#     print(20,"=",n_20)   
# if amount>=10:
#     n_10=amount//10
#     print(10,"=",n_10)       
# else: 
#     print("no")
# n=int(input("enetr a number"))
# str="2"
# i=0
# while i<n:
#     print(str,end=",")
#     str=str+"2"
#     i=i+1
# n=int(input("enter a number"))

# i=1
# sum=0
# while (i<=n):
#     if i%2==0 :
#         sum=sum+i
#     i=i+1
# print("sum of even number=",sum)
# 
#    
# 
# 
#
# 











# x=int(input("enter a number"))  
# y=1
# while y<=x:
#     print(x*y) 
#     y=y+1




# n=int(input("enter a number"))
# rev=0
# while n>0:
#     rev=rev*10+n%10
#     n=n//10
# print("reverse=",rev)    






# n=int(input("enter a number"))
# fac=1
# while n>0:
#     fac=fac*n
#     n=n-1
    
# print("factorial=",fac) 
# 
# 
#



# b=110111
# x=(b,2)
#     print(x)


# n=int(input("enter a number"))
# sum=0
# i=0
# a=len(str(n))
# while n>0:
#     r=n%2
#     b=r*10**i
#     sum=sum+b
#     n=n//2
# print(sum)    

# number=int(input("enter a number"))
# x=number
# rem=0
# place=1
# binary =0
# while (x>0):
#     rem =x%2
#     binary =(rem*place)+binary
#     x//=2
#     place*=10
# print( binary)   
# 
# 


# n=[23,45,32,25,46,33,71,90]


# n=int(input("enter a number"))
# i=1
# while n>0:
#     b=1
#     while b<i:
#         print(" ",end=" ")
#         b=b+1
#     j=1
#     while j<=(n*2)-1:
#         print(n,end=" ")   
#         j=j+1
#     print()  
#     n=n-1
#     i=i+1   

# n=int(input("enter a number"))
# for i in range (65,n+65):
#     for j in range (65,i+1):
#         print(chr(j),end=" ")
#     print()        



# n=int(input("enter the number"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(chr(64+j),end=" ")
#         j=j+1
#     print()
#     i=i+1
# i=1
# v=1
# b=1
# while i<5:
#     b=1
#     while b<=5-i :
#         print(" ",end=" ")
#         b=b+1
#         j=1
#     while j<=i:
#         print(v,end=" ")   
#         v=v+2
#         j+=1
#         b=b+1
#     print()  
#     i=i+1


# n=int(input("enter a number"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(j,"*" end=" ")
#         j=j+1
      
#     i=i+1 

# i=1
# while i<=6:
#     if (i==3):
#         break
#     print() 
#     i=i+1


# i=0
# while i<=30:
#     i+=2
#     if i==8:
#         continue
#         i+=1
#     if i==22:
#         break
#     print(i)


# n=10
# for n in range (n):
#     if n==10:
#         break
#     print("*")

    


# while i<=a:
#     j=1
# a=int(input("enter a number"))
# i
#     while j<=10:
#         print(i*j,i+j)
#         j=j+1
#     i=i+1
#     print()    


# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j=j+1
#     print() 
#     i=i+1   
# 
# i=1
# sum=0
# while i<=5:
#     b=1
#     while b<i+1:
#         print
# (sum,end=" ")
#         sum=sum+1
#         b=b+1
#     print() 
#     i=i+1   


# n=int(input("enter a number"))
# i=1
# sum=0
# while i<=n:
#     if i%2==0:
#         sum=sum+i
#     i=i+1
# print("sum of even number=",sum)    


# a=-1
# while a>=(-10):
#     print(-a)
#     a=a-1



# n=int(input("enter a number"))
# i=n
# count=0
# sum=0
# while i<=n:
#     if i%2==0:
#         print("this is even")
#     elif i%2!=0:
#         print("this is odd no")
#     else:
#         print("none")
#         sum=sum+n
#         count=count+i
#     i=i+1


# for i in range (1,6):
#     for j in range (1,i+1):
#         if i==1:
#             print(j,end=" ")
#         elif j==1:
#             print(j,"*",end=" ")   
#         elif i==j:
#             print(j,end=" ")  
#         else:
#             print("*",end=" ")  
#     print()             

# k=0
# for i in range (1,5):
#     for j in range (5,0,-1):
#         if i>=j:
#             print(j+k,end=" ")
#         else:
#             print("",end=" ")    
#     k=k+i
#     print()   
# 
# 
# n=int(input("enter a number"))     
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(chr(64+j), j,end=" ")
#         j=j+1
#     print()   
#     i=i+1 

# from re import I


# n=int(input("enter a number"))
# k=ord("U")
# i=n
# while i>0:
#     j=n
#     while j<=n:
#         print(chr(k),end=" ")
#         j=j+1
#     k=k+1   
#     i=i-1
#     print()

# n=int(input("enter a number"))
# i=1
# sum=0
# while i<=n:
#     j=1
#     while j<i+1:
#         print(sum+1,end=" ")
#         sum=sum+1
#         j=j+1
#     i=i+1
#     p rint()   

# n=int(input("enter a number"))   
# i=0
# while i<n:
#     j=1
#     while j<=n:
#         print(j+i,end=" ")       
#         j=j+1
#     i=i+1
#     print()  
# 123456
# 234567  
# 67891011                                                                                

# n=int(input("enter a number"))
# i=n
# while i<=n: 
#     if i*n: 
#         print(i*n)
#     i=i+1
# table 


a.sort6666556556-=-6556-=-65    qwertyuiop[][poitreqaxcvb;'
fzxcvbm']
    






