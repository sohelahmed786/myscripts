str = "hello"
#rotate by 1
rotate = str[len(str)-1] + str[:len(str)-1] #or str[-1:] + str[:len(str)-1]
print(rotate)
