D=int(input("Enter Number of Days:"))

y=D//365

print("\n Years:",y)

w=(D%365)//7
print("\n Weeks:",w)

d= D-((y*365)+(w*7))
print("\n Days:",d)