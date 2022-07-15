age=int(input())
decades=int(age/10)
if age%10!=0:
    remaining=age%10
    print("{} decades {} years".format(decades,remaining))
else:
    print("{} decades".format(decades))

