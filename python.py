a=input()
s=0
for i in range(len(a)):
    c=ord(a[i])
    d=[int(i) for i in bin(c)[2:]]
    s=s+sum(d)
print(s)
