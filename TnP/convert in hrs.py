#-------------------Converting Seconds into Hours-------------------

iS=int(input("Enter Seconds : "))

hr=iS//3600
print("hrs", hr)
m = (iS -(3600*hr))//60
print("M",m)

s= (iS -(3600*hr)-(m*60))
print("Sec", s)

#---------------------------------END--------------------------------