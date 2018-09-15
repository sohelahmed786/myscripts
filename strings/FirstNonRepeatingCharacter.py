
def firstNonRptChar1(str):
    order = []
    counts = {}
    for x in str:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    #for x in order:
     #   if counts[x] == 1:
      #      print(x)
       #     break;

    for key,value in counts.items():
       if counts[key] == 1:
           print(key)
           break;
    
def firstNonRptChar2(str):
    l = [x for x in str if str.count(x) == 1][0]
    print(l)




if __name__ == "__main__":
    str = "geeksforgeeks"
    firstNonRptChar1(str);
    #firstNonRptChar2(str);
