import tkinter as tk

#------------------------------
# GLOBAL variables
#------------------------------

global band
band = []
 
global table
table = []
 
global bandIndex
bandIndex = 0
 
global tableIndex
tableIndex = 0
 
global tableLength
tableLength = 0
 
global state
state = 1
 
global pointer
pointer = 0
 
global stateIndex
stateIndex = 0

global graphics

global root
 
global running
running = False

#------------------------------
# init
#------------------------------
def fillBand(length):   #band gets filled
    global band
    for i in range(0, length):  
        band.append("#")  

fillBand(50)   #band gets filled with 50 elements

   

def run(): #the running cirlce 
    if not running:
        return
    print("next run") 
    graphics.mapBand()
    graphics.mapTable()
    dumpMap()
    b = nextStep()
    graphics.update()
    if (b):
        root.after(2500, func=run)
    else:
        print("DONE")

def reset():
    global graphics, root
    print("reset")
    root.destroy()
    root = tk.Tk()
    graphics = GUI(root)
    root.mainloop()
 
class GUI(tk.Frame):
 
    def __init__(self, parent):
        super(GUI, self).__init__(parent)
        self.parent = parent
        parent.title("Turing")
        parent.geometry("600x475")
        parent.configure(bg="#36393F")
 
        # StartButton
        self.startButton = tk.Button(parent, fg="black", bg="#43B581", font=50, text="Start", command=self.start)
        self.startButton.place(x=50, y=125, width=250, height=50)
 
        # Pointer for band
        self.pointer = tk.Button(parent, bg="#F04747", font=50, text="V", command=self.moveCenter)
        self.pointer.place(x=50 - bandIndex, y=0, width=50, height=25)  # index angezeigter Feld - links rechts
 
        # Second Pointer for band
        self.secondPointer = tk.Button(parent, bg="#F04747", font=50, text="Ʌ", command=self.moveCenter)
        self.secondPointer.place(x=50, y=75, width=50, height=25)
 
        # state pointer for table
        self.statePointer = tk.Button(parent, bg="#FAA61A", font=50, text="V", command=self.centerTable)
 
        # Band
        bandLeft = tk.Button(parent, fg="#ffffff", bg="#2F3136", font=50, text="<", command=self.bandBack)
        bandLeft.place(x=0, y=25, width=50, height=50)
 
        self.arr = []
        for i in range(10):
            element = tk.Entry(parent)
            element.place(x=i * 50 + 50, y=25, width=50, height=50)
            self.arr.append(element)
 
        bandRight = tk.Button(parent, fg="#ffffff", bg="#2F3136", font=50, text=">", command=self.bandForward)
        bandRight.place(x=550, y=25, width=50, height=50)
 
        #Table
        self.tableElements = []

        th = ["Q", "L", "S", "B", "Q'"]
        for j in range(5):
            element = tk.Label(self.parent, text=th[j])
            element.place(x=50, y=j*50 + 225 , width=50, height=50)
            element.config(bg="#7289D9", font= 60) ##FAA61A orange #7289D9

        self.addCol = tk.Button(parent, bg="#7289D9", font= 50, text = "Add", command=self.add)
        self.addCol.place(x = 300, y = 125, width = 125, height = 50)
        self.add()
        
        self.reset = tk.Button(parent, bg="gray", font= 50, text = "Reset", command=self.reset)
        self.reset.place( x = 425, y = 125, width = 125, height = 50)

        tableLeft = tk.Button(parent,fg="#ffffff", bg="#2F3136", font= 60, text="<", command=self.tableLeft)
        tableLeft.place(x = 0, y = 225, width = 50, height = 250)
        
        tableRight = tk.Button(parent,fg="#ffffff", bg="#2F3136", font= 60, text=">", command=self.tableRight)
        tableRight.place(x = 550, y = 225, width = 50, height = 250)

        self.update()
        self.updateTable()
            
    def update(self):
        global band, bandIndex, stateIndex, tableIndex, running
        for i in range(10):
            self.arr[i].delete(0, tk.END)
            self.arr[i].insert(0, band[i + bandIndex])
        a = 50 - 50 * bandIndex + 50 * pointer
        c=bandIndex+pointer
        if (a < 0):
            a = 0
        elif (a > 550):
            a = 550
        self.pointer['text'] = "V"
        self.pointer.place(x=a, y=0, width=50, height=25)  # index angezeigter Feld - links rechts
        self.secondPointer.place(x=a, y=75, width=50, height=25)
        if(c > 0):
            self.pointer['text'] = str(-c)
        elif(c < -9):
            self.pointer['text'] = str(c+9)
        else:
            self.pointer['text'] = "V"
        if (running):
            self.startButton["text"] = "Stop"
        else:
            self.startButton["text"] = "Start"
 
   
    def start(self):
        global running
        print("start/stop")
        running = not running
        if (running):
            run()
  
    def add(self):
        global tableLength
        tableLength += 1
        print(tableLength)
        print("table length += 1")
        table.append(["", "", "", "", ""])
        print("table was appended")
        if (tableLength < 10):
            print("table length is under 10")
            tableElement = []
            for j in range(5):
                element = tk.Entry(self.parent)
                element.place(x=tableLength * 50 + 50, y=j * 50 + 225, width=50, height=50)
                tableElement.append(element)
            self.tableElements.append(tableElement)
            print("created new column")
    
    def bandForward(self):        #index + 1 -->  bewegt nach rechts
        global bandIndex
        self.mapBand()
        bandIndex += 1
        self.update()

    def bandBack(self):           #index - 1 -->  bewegt nach links
        global bandIndex
        self.mapBand()
        bandIndex -= 1
        self.update()
    
    def moveCenter(self):
        global bandIndex
        bandIndex = -2
        print("moved bandindex to center")
        print(bandIndex)
        self.update()

    def tableLeft(self):
        global table, tableIndex, tableLength
        if tableLength >= 10 and tableIndex <0:
            self.mapTable()
            tableIndex += 1
            self.updateTable()

    def tableRight(self):
        global table, tableIndex, tableLength
        if tableLength >= 10 and tableIndex > 9-tableLength:
            self.mapTable()
            tableIndex -= 1
            self.updateTable()
            
    def mapTable(self):
        global table, tableLength, tableIndex
        print("mapping table")
        print("tableIndex: " + str(tableIndex))
        print("tableLength: " + str(tableLength))
        for x in range(9 if tableLength >= 9 else tableLength):
            column = []
            print("old position: " + str(x))
            print("new position: " + str(x - tableIndex))
            for y in range(5):
                print(" x: " + str(x) + " y: " + str(y))
                column.append(self.tableElements[x][y].get())
            table[x - tableIndex] = column

    def updateTable(self):
        global table, tableLength, tableIndex
        print("update table")
        print("tableIndex: " + str(tableIndex))
        print("tableLength: " + str(tableLength))
        for x in range(9 if tableLength >= 9 else tableLength):
            for y in range(5):
                print(" x: " + str(x) + " y: " + str(y))
                self.tableElements[x][y].delete(0, tk.END)
                self.tableElements[x][y].insert(0, table[x - tableIndex][y])       
        b = 100 + stateIndex * 50 + tableIndex * 50
        if (b < 50):
            b = 0
        elif (b > 550):
            b = 550
        print("B:" + str(b))
        self.statePointer.place(x=b, y=200, width=50, height=25)

    def centerTable(self):
        global tableIndex
        tableIndex = 0
        self.updateTable()

    def mapBand(self): #liest Eingabe von Band aus und fügt sie in ein Array ein
        global band, bandIndex
        for i in range(10):
            value = self.arr[i].get()
            band[bandIndex + i] =  value if len(value) > 0 else "#"

    def reset(self):
        global bandIndex, band, tableIndex, table, tableLength, state, pointer, stateIndex
        bandIndex = 0
        band = []
        fillBand(10)
        tableIndex = 0
        table = []
        tableLength = 0
        state = 1
        pointer = 0
        stateIndex = 0
        reset()

 
#deprecated for debug reasons only
def dumpMap():
   print("tableLength: " + str(len(table)))
   for column in table:
      string = " [ "
      for element in column:
         string += element + ", "
      print(string + " ] ")

#------------------------------
# Backend
#------------------------------
def appendLeft():
    global band, pointer
    band.insert(0, "#")  # das band wird links um eine stelle erweitert
    pointer += 1
 
 
def appendRight():
    global band
    band.append("#")  # das band wird rehts um eine stelle erweitert
 
 
def nextStep():
    global table, state, pointer, band, stateIndex
    print(str(len(table)))
    for i in range(len(table)):  # gehe jede spalte durch
        column = table[i]
        print("checking: " + str(column) + " state: " + str(state) + " pointer: " + str(pointer))
        if column[0] == str(state):  # wenn der aktuelle zustand stimmt
            print("confirmed state " + str(column))
            if column[1] == band[pointer]:  # wenn man das richtige liest
                print("confirmd read " + band[pointer])
                stateIndex = i
                band[pointer] = column[2]  # ersetzte mit dem schreibe element
                move = 1 if column[3] == "R" else -1
                pointer += move  # ändere den Pointer entsprechend der richtung
                if move == 1 and pointer >= len(band):
                    appendRight()
                elif move == -1 and pointer < 0:
                    appendLeft()
                state = column[4]  # setzte den neuen state
                return True
            else:
                print("failed read " + band[pointer])
        else:
            print("failed state " + str(column))
    return False



#------------------------------
# Programm ausführen
#------------------------------

root = tk.Tk()
graphics = GUI(root)
root.mainloop()
