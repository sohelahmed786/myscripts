import re

def countwords1(str):
    count = len(re.findall(r'\w+',str))
    print(count)

def countwords2(str):
    print(len(str.split()))




if __name__ == "__main__":
    str = "the quick brown fox jumps over the lazy dog."
    countwords1(str);
    countwords2(str);
