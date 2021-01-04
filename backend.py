#definitions
global table, state, pointer, band, emptyBand
table =[["1", "#", "#", "R", "1"], 
        ["1", "B", "B", "R", "2"], 
        ["2", "B", "#", "R", "3"], 
        ["2", "#", "#", "L", "6"], 
        ["3", "B", "#", "R", "4"], 
        ["3", "#", "#", "L", "7"], 
        ["4", "B", "B", "R", "2"], 
        ["4", "#", "#", "L", "7"], 
        ["5", "#", "#", "L", "6"], 
        ["6", "B", "B", "L", "7"], 
        ["6", "#", "#", "R", "E"], 
        ["7", "#", "#", "L", "5"]]
state = "1"
pointer = 0
band = ["#", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "#"]
emptyBand = "#"

class Backend:

    class BackendException(Exception): #die Basis für alle Buntzerdefinierten Exceptions
        def getErrorMessage(self):
            pass

    class StateNotFoundException(BackendException): #wenn eine Zustand nicht übereinstimmt
        pass

    class BandOutOfBoundsException(BackendException): #wenn band nicht reicht
        def getErrorMessage(self):
            return "ERROR: band out of bounds"

    class ObjectNotFoundException(BackendException):    #wenn ein Objekt nicht gefunden wird
        pass
        
    def nextStep(self):
        global table, band, pointer, state
        for column in table: #gehe jede spalte durch
            if column[0] == state:   #wenn der aktuelle zustand stimmt
                if len(band) > pointer:
                    if column[1] == band[pointer]: #wenn man das richtige liest
                        band[pointer] = column[2] #ersetzte mit dem schreibe element
                        pointer += 1 if column[3] == "R" else -1
                        state = column[4]
                        return True
                    continue
                raise self.BandOutOfBoundsException()

        return False

    


try:
    backend = Backend()
    print("state: " + state + " position: " + str(pointer) + " band: " + str(band))
    while backend.nextStep():
        print("state: " + state + " position: " + str(pointer) + " band: " + str(band))
except Backend.BackendException() as e:
    print(e.getErrorMessage())


""" Konsole: 
The host doesn’t allow starting the debugger. If needed, ask them to enable it.

"""
