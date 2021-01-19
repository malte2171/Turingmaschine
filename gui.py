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


#------------------------------
# init
#------------------------------
def fillBand(length):   #band gets filled
    global band
    for i in range(0, length):  
        band.append("#")  

fillBand(50)   #band gets filled with 50 elements

def run(): #the running cirlce   
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


#------------------------------
# GUI
#------------------------------
class GUI(tk.Frame):
   def __init__(self, parent):
      super(GUI, self).__init__(parent)
      self.parent = parent
      parent.title("Turing")
      parent.geometry("600x475")
      parent.resizable(0, 0)
      parent.configure(bg="#36393F")


      #StartButton
      bandLeft = tk.Button(parent,fg="black", bg="#43B581",font= 50, text = "Start", command=self.start) #start button is created
      bandLeft.place(x = 50, y = 125, width = 250, height = 50)   #start button is placed

      #Pointer(von oben)
      self.pointer = tk.Label(parent, bg="#F04747", font=50, text="V")  #label is created
      self.pointer.place(x =50, y =0, width=50 , height = 25) #label is placed

      #Pointer(von unten)
      self.secondPointer = tk.Label(parent, bg="#F04747", font=50, text="Ʌ")  #Label is created
      self.secondPointer.place(x =50, y =75, width=50 , height = 25) #label is placed

      #state Pointer
      self.statePointer = tk.Label(parent, bg="#FAA61A", font=50, text="V")   #state pointer is created
      
      #Band
      bandLeft = tk.Button(parent,fg="#ffffff", bg="#2F3136",font= 50, text = "<", command=self.bandBack)   #band go-left is created
      bandLeft.place(x = 0, y = 25, width = 50, height = 50)   #band go-left is created

      self.arr = []
      for i in range (10):
         element = tk.Entry(parent, font= 60)
         element.place(x=i*50 + 50, y=25, width=50, height=50)
         self.arr.append(element)
      
      bandRight = tk.Button(parent,fg="#ffffff", bg="#2F3136",font= 50, text = ">", command=self.bandForward)
      bandRight.place(x = 550, y = 25, width = 50, height = 50)


      #Table
      self.tableElements = []

      th = ["Q", "L", "S", "B", "Q'"]
      for j in range(5):
         element = tk.Label(self.parent, text=th[j])
         element.place(x=50, y=j*50 + 225 , width=50, height=50)
         element.config(bg="#7289D9", font= 60) ##FAA61A orange #7289D9

      self.addCol = tk.Button(parent, bg="#7289D9", font= 50, text = "Add", command=self.add)
      self.addCol.place(x = 300, y = 125, width = 250, height = 50)
      self.add()
      
      tableLeft = tk.Button(parent,fg="#ffffff", bg="#2F3136", font= 60, text="<", command=self.tableLeft)
      tableLeft.place(x = 0, y = 225, width = 50, height = 250)
      
      tableRight = tk.Button(parent,fg="#ffffff", bg="#2F3136", font= 60, text=">", command=self.tableRight)
      tableRight.place(x = 550, y = 225, width = 50, height = 250)

      self.update()

   def update(self): 
      global band, bandIndex, stateIndex
      for i in range(10):
         self.arr[i].delete(0, tk.END)
         self.arr[i].insert(0, band[i + bandIndex])
      a = 50 - 50 * bandIndex + 50 * pointer
      if (a >= 0 and a <= 550):
         self.pointer.place(x = a, y =0, width=50 , height = 25) #index angezeigter Feld - links rechts 
         self.secondPointer.place(x = a, y =75, width=50 , height = 25)
      b = 100 + stateIndex * 50
      self.statePointer.place(x=b, y=200, width=50 , height = 25) 

   def start(self):
      print("start")
      run()

   def add(self):
      global tableLength
      tableLength += 1
      if (tableLength < 10):
         tableElement = []
         for j in range(5):
            element = tk.Entry(self.parent)
            element.place(x=tableLength*50 + 50, y=j*50 + 225 , width=50, height=50)
            tableElement.append(element)
         self.tableElements.append(tableElement)

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

   #deprecated
   def tableLeft(self):
      print()

   #deprecated
   def tableRight(self):
      global table, tableIndex
      self.mapTable()
      for x in range(10 if tableIndex >= 10 else tableIndex + 1):
         for y in range(5):
            self.tableElements[x][y].delete()
            self.tableElements[x][y].insert(0, table[x - tableIndex][y])

   def mapTable(self): #liest Eingabe von Tabelle aus und fügt sie in ein 2dimensionales Array ein
      global table, tableLength
      table = []
      for x in range(tableLength):
         arr = []
         for y in range(5):
            #print(" x: " + str(x) + " y: " + str(y))
            b = self.tableElements
            #print(str(b))
            a = b[x][y].get()
            #print(str(a))
            #print(type(a))
            arr.append(a)
         table.append(arr)

   def mapBand(self): #liest Eingabe von Band aus und fügt sie in ein Array ein
      global band, bandIndex
      for i in range(10):
         value = self.arr[i].get()
         band[bandIndex + i] =  value if len(value) > 0 else "#"


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
   for i in range(len(table)):  # gehe jede spalte durch
      column = table[i]
      print("checking: " + str(column) + " state: " + str(state) + " pointer: " + str(pointer))
      if column[0] == str(state):  # wenn der aktuelle zustand stimmt
         print("confirmed state " + str(column))
         if column[1] == band[pointer]:  # wenn man das richtige liest
            print("confirmed read " + band[pointer])
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


#deprecated for debug reasons only
def dumpMap():
   print("tableLength: " + str(len(table)))
   for column in table:
      string = " [ "
      for element in column:
         string += element + ", "
      print(string + " ] ")


#------------------------------
# Programm ausführen
#------------------------------

root = tk.Tk()
graphics = GUI(root)
root.mainloop()