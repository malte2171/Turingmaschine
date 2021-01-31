table = ([["1", "B", "B", "R", "2"],  # überspringe den erstn Baum
          ["2", "B", "B", "R", "3"],  # überspringe den zweiten Baum
          ["3", "B", "#", "R", "1"],  # lösche den dritten Baum
          ])
state = "1"
pointer = 0
band = []


def fillBand(length):
    global band
    for i in range(0, length):  # geht band einmal durch
        band.append("B")  # band wird für jedes i um "B" erweitert


def appendLeft():
    global band
    global pointer
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
                if move == 1 and pointer >= len(band):
                    appendRight()
                elif move == -1 and pointer < 0:
                    appendLeft()
                state = column[4]  # setzte den neuen state
                return True
    return False


fillBand(10)  # band wird gefüllt
print(band)
try:
    while nextStep():
        print(band)
finally:
    print("Done")