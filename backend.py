table = [["1", "#", "#", "R", "1"], ["1", "B", "B", "R", "2"], ["2", "B", "#", "R", "3"], ["2", "#", "#", "L", "6"], ["3", "B", "#", "R", "4"], ["3", "#", "#", "L", "7"], ["4", "B", "B", "R", "2"], ["4", "#", "#", "L", "7"], ["5", "#", "#", "L", "6"], ["6", "B", "B", "L", "7"], ["6", "#", "#", "R", "E"], ["7", "#", "#", "L", "5"], ["E", "#", "#", "R", "E"], ]
state = "1"
pointer = 0
band = []


#for r in table:
#    for c in r:
#        print(c,end = " ")
#    print()

#print(table)

class Error(Exception): #die Basis für alle Buntzerdefinierten Exceptions
    pass

class StateNotFound(Error): #wenn eine Zustand nicht übereinstimmt
    pass

class ObjectNotFound(Error):    #wenn ein Objekt nicht gefunden wird
    pass

def printTable(table):
    for arr in range(0, len(table)):
            print(table[arr])

def fillBand(band, length):
    for i in range (0, length): #geht band einmal durch
        band.append("X")    #band wird für jedes i um "X" erweitert
    print(band) #band wird ausgegeben
    return band

def appendBand(band, var):  
    band.insert(0, var) #das band wird links um eine Variable erweitert 
    print(band)
    return band
    
def nextStep():
    for column in table: #gehe jede spalte durch
        if column[0] == state:   #wenn der aktuelle zustand stimmt
            if column[1] == band[pointer]: #wenn man das richtige liest
                band[pointer] = column[2] #ersetzte mit dem schreibe element
                pointer += 1 if column[3] == "R" else -1
                state = column[4]
                return True
    return False

            

def cast(string):
    interger = int(string)
    return interger
    

var = 7

fillBand(band, 10)  #band wird gefüllt
appendBand(band, var)   #band wird mit var nach links erweitert
printTable(table)


