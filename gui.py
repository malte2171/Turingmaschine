import tkinter as tk

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

def fillBand(length):
    global band
    for i in range(0, length):  
        band.append("#")  

fillBand(50)

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

class GUI(tk.Frame):
   
   def __init__(self, parent):
      super(GUI, self).__init__(parent)
      self.parent = parent
      parent.title("Turing")
      parent.geometry("600x475")
      parent.configure(bg="#36393F")


      #StartButton
      bandLeft = tk.Button(parent,fg="black", bg="#43B581",font= 50, text = "Start", command=self.start)
      bandLeft.place(x = 50, y = 125, width = 250, height = 50)

      #Pointer
      self.pointer = tk.Label(parent, bg="#F04747", font=50, text="V")
      self.pointer.place(x =50-bandIndex, y =0, width=50 , height = 25) #index angezeigter Feld - links rechts 

      #Second Pointer
      self.secondPointer = tk.Label(parent, bg="#F04747", font=50, text="Ʌ")
      self.secondPointer.place(x =50, y =75, width=50 , height = 25) 

      #state Pointer
      self.statePointer = tk.Label(parent, bg="#FAA61A", font=50, text="V")
      
      #Band
      bandLeft = tk.Button(parent,fg="#ffffff", bg="#2F3136",font= 50, text = "<", command=self.bandBack)
      bandLeft.place(x = 0, y = 25, width = 50, height = 50)

      self.arr = []
      for i in range (10):
         element = tk.Entry(parent)
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
      table.append([])
      if (tableLength < 10):
         tableElement = []
         for j in range(5):
            element = tk.Entry(self.parent)
            element.place(x=tableLength*50 + 50, y=j*50 + 225 , width=50, height=50)
            tableElement.append(element)
         self.tableElements.append(tableElement)

   def bandForward(self):
      global bandIndex
      self.mapBand()
      bandIndex += 1
      self.update()

   def bandBack(self):
      global bandIndex
      self.mapBand()
      bandIndex -= 1
      self.update()

   def tableLeft(self):
      global table, tableLength, tableIndex
      print("if: " + str(tableLength + tableIndex))
      if (tableLength + tableIndex) < 9: 
         self.mapTable()
         tableIndex += 1
         self.updateTable()
       
   def tableRight(self):
      global table, tableLength, tableIndex
      print("if: " + str(tableLength - tableIndex))
      if (tableLength - tableIndex) >= 9: 
         self.mapTable()
         tableIndex -= 1
         self.updateTable()
         
   def mapTable(self):
      global table, tableLength, tableIndex
      print("mapping table")
      print("tableIndex: " + str(tableIndex))
      print("tableLength: " + str(tableLength))
      for x in range(9 if tableLength >= 9 else tableLength - 1): #TODO change
         column = []
         print("old position: " + str(x))
         print("new position: " + str(x-tableIndex))
         for y in range(5):
            print(" x: " + str(x) + " y: " + str(y))
            column.append(self.tableElements[x][y].get())
         print("index: " + str(x-tableIndex))
         table[x-tableIndex] = column
   
   def updateTable(self):
      global table, tableLength
      print("update table")
      print("tableIndex: " + str(tableIndex))
      print("tableLength: " + str(tableLength))
      for x in range(9 if tableLength >= 9 else tableLength):
         for y in range(5):
            print(" x: " + str(x) + " y: " + str(y))
            self.tableElements[x][y].delete(0, tk.END)
            self.tableElements[x][y].insert(0, table[x-tableIndex][y])
    


# TODO fix 
#   def checkTable(self):
#      #Missing - Implementation to mapTable
#          
#      #Zustand: Qn
#      #Checking for end state
#      endzustand = False
#      for _ in range(x):
#         if y == 0 and (a == 'e' or a == 'E') :
#            endzustand = True
#         elif y == 4 and (a == 'e' or a == 'E') :
#            endzustand = True
#      #Zustand: L
#      #Checking if read is in band
#      for _ in range(x):
#         if y == 1:
#            if a in band:
#                  print("L - is accepted")
#            else:
#                  print("This should not be accepted as an input - L")
#                  print(x, y)
#                  #break
#      #Zustand: B
#      #Checking that movments are defined
#      leftright = ["r", "R", "l", "L"]
#      for _ in range(x):
#         if y == 3:
#            if a in leftright:
#                  print("B - is accepted")
#            else:
#                  print("This should not be accepted as an input - B")
#                  print(x, y)
#                  #break
#                  
#      arr.append(a)
#
#   #Checking state of endzustand
#   if endzustand == True:
#      print("Endzustand gefunden")
#   elif endzustand == False:
#      print("Endzustand nicht gefunden")
#      # break
#
#   table.append(arr)


   def mapBand(self):
      global band, bandIndex
      for i in range(10):
         value = self.arr[i].get()
         band[bandIndex + i] =  value if len(value) > 0 else "#"
         





#Backend
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


#deprecated for debug reasons only
def dumpMap():
   print("tableLength: " + str(len(table)))
   for column in table:
      string = " [ "
      for element in column:
         string += element + ", "
      print(string + " ] ")
root = tk.Tk()
graphics = GUI(root)
root.mainloop()

   
