dec=int(input("Enter the value"))
las=int()
strdec=str()
intdec=int()
while(dec!=0):
    las=dec%2
    strdec=str(las)+strdec
    dec=dec//2
print(strdec)
intdec=strdec
int(intdec)
print(intdec)