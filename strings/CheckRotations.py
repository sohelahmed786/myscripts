def checkRotation(str1,str2):
    return(len(str1)==len(str2) and str2 in str1*2)




if __name__ == "__main__":
    str1 = input('enter original string: ')
    str2 = input('enter string to check rotation: ')
    if(checkRotation(str1,str2)):
        print("Rotation exist")
    else:
        print("Rotation not exist")
