priorityList={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,
't':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,'H':34,'I':35,'J':36,'K':37,'L':38,
'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52}

def findPriority(element):
    global priorityList
    return priorityList.get(element)

with open("input.txt", "r") as txt_file:
        input = txt_file.readlines()
def findValue(input):
    priority=0
    for line in input:
        half = (len(line))//2
        firstHalf=line[0:half]
        secondHalf=line[half:len(line)]
        for element in firstHalf:
            if element in secondHalf :
                priority += findPriority(element)
                break
    return priority
def findBadge(input):
    i = 0
    priority = 0
    while i < len(input):
        line1= input[i]
        line2= input[i+1]
        line3= input[i+2]
        lines=[line1,line2,line3]
        listMax = max(lines, key=len)
        lines.remove(listMax)
        lineT1=lines[0]
        lineT2=lines[1]
        for element in listMax:
            if element in lineT1 and element in lineT2:
                priority += findPriority(element)
                break
        i=i+3
        

    return priority

# print(findValue(input))
print(findBadge(input))