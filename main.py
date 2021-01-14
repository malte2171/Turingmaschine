import time
import tkinter as tk
 
global table #tabelle
table = [[]]
 
global band #band
band = []
 
global pointer
pointer = 0

global state
state = 1



class Converter:
  
  def mapInput():             #fills table from user input (TODO 2)

  def mapBand():              #fills band from user input (TODO 2)

  def updateBand():           #updates the band to the GUI (TODO 1)
          
class GUI:
  
  def __init__():               #builds and openes GUI (TODO 2)
     
  def appendTable():            #adds 1 column to the table (TODO 2)
    
  def appendBand():             #adds on element to the band (TODO 2)


class Processing:
  
  def appendLeft():             #band gets appended if the pointer goes further left
 
  def appendRight():            #band gets appended if the pointer goes further right 
    
  def nextStep():               #next step from the table gets applied to our band (TODO 2 improve)

#Adrian
def scheduler():                #plays the algorithm step by step (TODO 1)




#############################
#---------------------------
# Data - Malte & Tobias
# Depricated
def filling_table():
    print("Filling Table")
    row = 0
    column = 0
    amount = 0
    print("***Important***")
    print("***If you have finished your entry type 'exit'***")
    while True:  # infinite loop
        amount = 0
        for x in range(5):  # Amount of columns (Q,L,S,B,Qn)

            if row == 5:  # Detects the last row
                column += 1  # Moves to the next column
                row = 0  # Restarts at the top of the column

            print("Column:", column + 1)  # Prints the column Number
            print("Row:", x + 1)  # Prints the row number

            user = input("Input: ")  # Asks the user for their input
            if user == "exit":  # Detects if the user enters 'exit'
                if amount < 5:
                    if (amount == 5 or amount == 0) and user == "exit":
                        if len(table) == 0:
                            print("\n")
                            print("Array is empty")
                        else:
                            print("\n")
                            output_table()
                            print("\n")
                            return
                    print("Du bist dumm")
                    print("\n")
                    while user == "exit":
                        user = input("Input: ")  # Asks the user for their input
                        if user == "exit":
                            print("Du bist immer noch dumm")
                            print("\n")
                else:
                    print(table)  # Outputs the whole table
                    print("\n") # Prints empty line
                    return  # exits the loop

            if row == 0:
                table.append([])  # Adds a new column to the list

            table[column].append(user)  # Adds the user input to the table

            row += 1  # Moves onto the next row
            amount += 1


            print("-->", table[column])  # Outputs the current numbers in the row the user is working on
            print("\n") # Prints empty line

def filling_band(): # Defining
    print("Filling Band")
    print("***Important***")
    print("***If you have finished your entry type 'exit'***")
    while True: # Infinite loop
        user = input("Input: ") # User Input
        if user == "exit": # Detects when "exit" is entered by the User
            print(band) # Outputs the band
            return # Exits loop
        else:
            band.append(user) # Adds user input to array band
            print(band) # Outputs the band
            print("\n") # Prints empty line

def output_table():

    label = ["Q", "L", "S", "B", "Qn"]
    pointer = 0
    output = []
    for i in range(5):
        output.append([])
        for element in range(len(table)):
            output[i].append(table[element][i])

    for array in output:
        print(label[pointer], array)
        pointer += 1

# Executing the functions
filling_table() # Calls function filling_table
filling_band() # Calls function filling_band











#---------------------------
# GUI
global picture

class simpleapp_tk(tk.Tk):
 
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
 
    def initialize(self):     
        self.grid()
        # Startknopf entsteht
        self.button1 = tk.Button(self, text="START", command=self.OnButtonClick, bg="red")
        self.button1.grid(column=0, row=0)
        # Textfeld
        self.labelOne = tk.Label(self, text="Drücke den Knopf")
        self.labelOne.grid(column=1, row=0)
 
    # wenn Startknopf gedrückt
    def OnButtonClick(self):
        global picture
 
        self.button1.configure(bg="grey")
        print("Startknopf gedrückt")
 
        # Zustandsanzeige
        stateGui = 3
        self.labelTwo = tk.Label(self, text=stateGui,
                                       bg='lightblue',
                                       font=('times', 40, 'bold'))
        self.labelTwo.grid(column=0, row=1)
 
        # Lese-Schreib-Kopf
        x = 5
        Bild = tk.PhotoImage(file="Pfeil.png")
        self.labelOne.configure(text="", image=picture, compound=tk.RIGHT)
        self.labelOne.grid(column=x + 1, row=0)
 
        # Band
        print("Wie lang soll das Band sein?")
        b_width = int(input())
 
        b_height = 1
        for i in range(b_height):  # Rows
            for j in range(b_width):  # Columns
                b = tk.Entry(self, text="")
                b.grid(row=i + 1, column=j + 2)
 
            # Tabelle
        print("Wie lang soll die Tabelle sein?")
        h = tk.Entry(self, text="Tabelle", bg="lightgrey")
        h.grid(row=2, column=2)
        t_width = int(input())
        t_height = 5
        for i in range(t_height):  # Rows
            for j in range(t_width):  # Columns
                b = tk.Entry(self, text="")
                b.grid(row=i + 3, column=j + 2)
 









#---------------------------
# Backend
 
 class Backend:

    def appendLeft():
        global pointer
        global band
        band.insert(0, "#")  # das band wird links um eine stelle erweitert
        pointer += 1
    
    
    def appendRight():
        global band
        band.append("#")  # das band wird rehts um eine stelle erweitert
    
    
    def nextStep():
        global table, state, pointer, band
        for column in table:  # gehe jede spalte durch
            if column[0] == state:  # wenn der aktuelle zustand stimmt
                if column[1] == band[pointer]:  # wenn man das richtige liest
                    band[pointer] = column[2]  # ersetzte mit dem schreibe element
                    move = 1 if column[3] == "R" else -1
                    pointer += move  # ändere den Pointer entsprechend der richtung
                    if move == 1:
                        appendRight()
                    elif move == -1 and band[move] is None:
                        appendLeft()
                    state = column[4]  # setzte den neuen state
                    return True
        return False











#---------------------------
# Programm
        
delay = -1
def update_gui():
    global delay
    print(2)
    if delay == -1:
        delay = int(input("Gib ein delay ein: "))
    while delay == -1:
        update_gui()
 
 
def timer():
    global delay
    x=nextStep()
    print(band)
    update_gui()
    #time.sleep(delay)
    print(x)
    if x == True:
        simpleapp_tk.after(timer,int(delay*1000), timer())  # sorgt dafür, dass der Timer immer durch läuft
update_gui()
filling_table()
filling_band()
  
 
if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Oberfäche')
    app.geometry('800x500')
    app.mainloop()
#---------------------------
############################




