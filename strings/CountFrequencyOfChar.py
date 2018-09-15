import collections

def countFrequency1(str):
    print(collections.Counter(str))

def countFrequency2(str):
    dict = {}
    for i in str:
        #keys = dict.keys()
        if i in dict:
            dict[i] +=1
        else:
            dict[i] = 1
    print(dict)

if __name__ == "__main__":
    #str1 = input('enter original string: ')
    countFrequency2('different')
