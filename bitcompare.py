def countBit(bin1,bin2):
    count=0
    bit=16
    req=0
    if(len(bin1)==len(bin2)):
        if(bin1==bin2):
            return 0
        else:
            for i in range(0,len(bin1)):
                if(bin1[i]!=bin2[i]):
                    count+=1
        return count
    else:
        req=(16-len(bin1))
        bin1=("0"*req)+bin1
        req=(16-len(bin2))
        bin2=("0"*req)+bin2
        if(bin1==bin2):
            return 0
        else:
            for i in range(0,16):
                if(bin1[i]!=bin2[i]):
                    count+=1
        return count


def decimalToBinary(dec):
    las=int()
    strdec=str()
    intdec=int()
    while(dec!=0):
        las=dec%2
        strdec=str(las)+strdec
        dec=dec//2
    return strdec


dec1=int(input("Enter the first value"))
dec2=int(input("Enter the second value"))
bin1=str()
bin2=str()
result=int()
bin1=decimalToBinary(dec1)
bin2=decimalToBinary(dec2)

result=countBit(bin1,bin2)
print(result)

