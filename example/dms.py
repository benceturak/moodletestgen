def dms(input):
    mnt,sec = divmod(input[0]*3600,60)
    deg,mnt = divmod(mnt,60)
    return ("%d-%02d-%02d" % (deg,mnt,round(sec,0)))

#print(dms(41.05044))
