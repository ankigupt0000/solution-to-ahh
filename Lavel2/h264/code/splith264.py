# need python 3 to run
import sys

def PrintProgress(length,percent):
        prog='['+('#'*int(percent*float(length/100))).ljust(length,'-')+']'+str(int(percent)).rjust(4,' ')+'% Complete'
        sys.stdout.write(prog)
        sys.stdout.write('\b'*len(prog))
        sys.stdout.flush()
        if percent==100:
                sys.stdout.write('\n')


f=open('..\\input\\20140726_040000_ps.h264','rb')
target=[
        open('..\\output\\file1.h264','wb'),
        open('..\\output\\file2.h264','wb'),
        open('..\\output\\file3.h264','wb'),
        open('..\\output\\file4.h264','wb')
        ]
last4=[0,0,0,0]
plast4=[0,0,0,0]
pseq=[0,0,0,0]
d=4
count=0
pcount=0
try:
        byte=f.read()
        PrintProgress(50,0)
        lst=byte.split(b'\x00\x00\x01')
        b=0
        file=0
        length=len(lst)
        for b in range(length):
                if (lst[b])[:1]==b'\x65' and lst[b-1][5:6] == b'\x00':
                        meta=int.from_bytes((lst[b-1])[3:4],byteorder='big')
                        pmeta=int.from_bytes(lst[b-4][6:7],byteorder='big')
                        pseqmeta=int.from_bytes(lst[b-4][0:1],byteorder='big')
                        if count<4:
                                    last4[count]=meta
                                    target[count].write(b'\x00\x00\x01'+lst[b-4]+b'\x00\x00\x01'+lst[b-3]+b'\x00\x00\x01'+lst[b-2]+b'\x00\x00\x01'+lst[b-1]+b'\x00\x00\x01'+lst[b])
                                    plast4[count]=pmeta
                                    pseq[count]=pseqmeta
                                    count+=1
                        else:
                                break;
                
        while b < length:
             H=int((b/length)*100)
             PrintProgress(50,H)
             # I Frame  distinguished and saved in different files.
             if (lst[b])[:1]==b'\x65' and lst[b-1][5:6] == b'\x00':
                    meta=int.from_bytes((lst[b-1])[3:4],byteorder='big')
                    pmeta=int.from_bytes(lst[b-4][6:7],byteorder='big')
                    pseqmeta=int.from_bytes(lst[b-4][0:1],byteorder='big')
                    for j in range(4):
                            if  meta == (last4[j]+2)%256:
                                    #print(meta, last4[0])
                                    target[j].write(b'\x00\x00\x01'+lst[b-4]+b'\x00\x00\x01'+lst[b-3]+b'\x00\x00\x01'+lst[b-2]+b'\x00\x00\x01'+lst[b-1]+b'\x00\x00\x01'+lst[b])
                                    last4[j]=meta
                                    plast4[j]=pmeta
                                    pseq[j]=pseqmeta
                                    file=j
                    
                    nextImeta=0
                    nextI=length
                    for j in range(b+1,length):
                            nextImeta=int.from_bytes((lst[j-1])[3:4],byteorder='big')
                            if nextImeta == (meta+2)%256:
                                    nextI=j
                                    break;

                    for j in range(b+1,nextI):
                        if lst[j-1][5:6] == b'\x01' :
                           #pmeta=int.from_bytes(lst[j-1][6:7],byteorder='big')
                           pseqmeta=int.from_bytes(lst[j-1][0:1],byteorder='big')
                           for k in range(4):        
                                   if  pseqmeta == pseq[k]+1: 
                                           target[file].write(b'\x00\x00\x01'+lst[b-1]+b'\x00\x00\x01'+lst[b])
                                           plast4[k]=pmeta
                                           pseq[k]=pseqmeta
                                   pcount+=1
             b+=1
        PrintProgress(50,100)
finally:
    f.close()
    for i in range(d):
            target[i].close()
