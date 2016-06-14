import sys
f=open('..\\input\\20140726_040000_ps.h264','rb')
target=[
        open('..\\output\\other1.h264','wb'),
        open('..\\output\\other2.h264','wb'),
        open('..\\output\\other3.h264','wb'),
        open('..\\output\\other4.h264','wb')
        ]
last4=[0,0,0,0]
plast4=[0,0,0,0]
pseq=[0,0,0,0]
d=4
count=0
pcount=0
try:
        byte=f.read()
        lst=byte.split(b'\x00\x00\x01')
        print(len(lst))
        for b in range(len(lst)):
            #print(bytes((lst[b])[0:1]))
                
            # I Frame  distinguished and saved in different files.
            if (lst[b])[:1]==b'\x65':
                    meta=int.from_bytes((lst[b-1])[3:4],byteorder='big')
                    pmeta=int.from_bytes(lst[b-4][6:7],byteorder='big')
                    pseqmeta=int.from_bytes(lst[b-4][0:1],byteorder='big')
                    #print()
                    # print('I', lst[b-4])
                    # print()
                    #print(meta)
                    if count<4:
                            last4[count]=meta
                            target[count].write(b'\x00\x00\x01'+lst[b-4]+b'\x00\x00\x01'+lst[b-3]+b'\x00\x00\x01'+lst[b-2]+b'\x00\x00\x01'+lst[b-1]+b'\x00\x00\x01'+lst[b])
                            plast4[count]=pmeta
                            pseq[count]=pseqmeta
                    elif  meta == (last4[0]+2)%256:
                            #print(meta, last4[0])
                            target[0].write(b'\x00\x00\x01'+lst[b-4]+b'\x00\x00\x01'+lst[b-3]+b'\x00\x00\x01'+lst[b-2]+b'\x00\x00\x01'+lst[b-1]+b'\x00\x00\x01'+lst[b])
                            last4[0]=meta
                            plast4[0]=pmeta
                            pseq[0]=pseqmeta
                    elif  meta == (last4[1]+2)%256:
                            #print(meta, last4[1])
                            target[1].write(b'\x00\x00\x01'+lst[b-4]+b'\x00\x00\x01'+lst[b-3]+b'\x00\x00\x01'+lst[b-2]+b'\x00\x00\x01'+lst[b-1]+b'\x00\x00\x01'+lst[b])
                            last4[1]=meta
                            plast4[1]=pmeta
                            pseq[1]=pseqmeta
                    elif  meta == (last4[2]+2)%256:
                            #print(meta, last4[2])
                            target[2].write(b'\x00\x00\x01'+lst[b-4]+b'\x00\x00\x01'+lst[b-3]+b'\x00\x00\x01'+lst[b-2]+b'\x00\x00\x01'+lst[b-1]+b'\x00\x00\x01'+lst[b])
                            last4[2]=meta
                            plast4[2]=pmeta
                            pseq[2]=pseqmeta
                    elif  meta == (last4[3]+2)%256:
                            #print(meta, last4[3])
                            target[3].write(b'\x00\x00\x01'+lst[b-4]+b'\x00\x00\x01'+lst[b-3]+b'\x00\x00\x01'+lst[b-2]+b'\x00\x00\x01'+lst[b-1]+b'\x00\x00\x01'+lst[b])
                            last4[3]=meta
                            plast4[3]=pmeta
                            pseq[3]=pseqmeta
                    count+=1
            #print(len(last4))
            #print(len(plast4))
            if (lst[b])[:1] ==b'\x61' and lst[b-1][5:6] == b'\x01' :
                   pmeta=int.from_bytes(lst[b-1][6:7],byteorder='big')
                   pseqmeta=int.from_bytes(lst[b-1][0:1],byteorder='big')
                   if pmeta == (plast4[0]+40)%256 and pseqmeta == pseq[0]+1:
                           target[0].write(b'\x00\x00\x01'+lst[b-1]+b'\x00\x00\x01'+lst[b])
                           plast4[0]=pmeta
                           pseq[0]=pseqmeta
                   if pmeta == (plast4[1]+40)%256 and pseqmeta == pseq[1]+1:
                           target[1].write(b'\x00\x00\x01'+lst[b-1]+b'\x00\x00\x01'+lst[b])
                           plast4[1]=pmeta
                           pseq[1]=pseqmeta
                   if pmeta  == (plast4[2]+40)%256 and pseqmeta == pseq[2]+1:
                           target[2].write(b'\x00\x00\x01'+lst[b-1]+b'\x00\x00\x01'+lst[b])
                           plast4[2]=pmeta
                           pseq[2]=pseqmeta
                   if pmeta == (plast4[3]+40)%256 and pseqmeta == pseq[3]+1:
                           target[3].write(b'\x00\x00\x01'+lst[b-1]+b'\x00\x00\x01'+lst[b])
                           plast4[3]=pmeta
                           pseq[3]=pseqmeta
                   pcount+=1
finally:
    f.close()
    for i in range(d):
            target[i].close()
