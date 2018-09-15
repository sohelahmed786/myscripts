#add two binary numbers taking input in binary form
def calculate(x,y):
    
    res = bin(int(x,2)+int(y,2))
    print(res)
    


if __name__ == "__main__":
    calculate('0100','0010')
