Tup = ('www','hackerrank','com','domains','python')
str = ".".join(Tup)
splt_front = str.split(".")[:3]
joinwdot = ".".join(splt_front)
splt_back = str.split(".")[3:]
joinwslash = "/".join(splt_back)
print('/'+joinwdot+'/'+joinwslash)

