
def processline(line1):
    newlist = [(l.split(">")[1]) for l in line1[0:]]
    return newlist
    
def read_data(filename):
    file = open(filename,'r')
    data = file.readlines()
    print("21")
    lists = []
    for line in data:
        new_list = processline(line.split("</li>"))
        lists.append(new_list)
    #print("Array prints here to test ", lists)
    print("11")
    wlist = lists 
    print(wlist)
    return wlist
    

def main():
    print("11")
    water = read_data("textfile.txt")    # read in data
    print("12")  

    file1 = open("allcompanieslist.txt","a")
    k= 0 
    for i in water[0:]:
        file1.write(water[k][0])
        k = k+ 1 


if __name__ == "__main__":
    print("00")
    main() 
    print("01")       