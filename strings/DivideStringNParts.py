import textwrap

def divideString(str,x):
    div = len(str)//x
    print(textwrap.wrap(str,div))




if __name__ == "__main__":
    str = "a_simple_divide_string_quest"
    divideString(str,4)
