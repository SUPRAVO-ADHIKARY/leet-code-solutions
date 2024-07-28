def passWordChecker(a):
    sp,cap,num=0,0,0
    if(len(a)<4):
        return(0)
    if(a[0].isdigit()):
        return(0)
    for i in range(0,len(a)):
        if(a[i].isupper()):
            cap+=1
        if(a[i].isdigit()):
            num+=1
        if(a[i]==' ' or a[i]=='/'):
            return(0)
    if(num>=1 and cap>=1):
        return(1)
    else:
        return(0)

a="L6otp"
print(passWordChecker(a))