def roundToPlates(n):
    print("TODO")
    basenmr = n%10


def readTMs(valueArray, fileArray, nameArray):
    valueArray.clear()
    counter = 0
    for file in fileArray:
        f = open(file, "r")
        try:
            valueArray.append(float(f.read())) 
        except ValueError:
            print("There was an error reading the file, please check if the file is empty or if it contains only numbers")
            writeOneTM(fileArray, nameArray, counter)
            break
        f.close()


def updateTMs(valueArray, valueToAdd, fileArray):
    counter = 0
    for file in fileArray:
        f = open(file, "w")
        if (counter == 0 or counter == 1 or counter == 4 or counter == 5): #matches upper body lifts
            f.write(str(valueArray[counter]+valueToAdd))
        else:                                                              #matches lower body lifts
            f.write(str(valueArray[counter]+valueToAdd*2))
        f.close
        counter+=1


def printSet(multiplierArray, tmValue, repsArray):
    print("(" + str(int(multiplierArray[0]*100)) +  "%) = " + str(round(tmValue*multiplierArray[0], 2)) + "kg x" + str(repsArray[0]))
    print("(" + str(int(multiplierArray[1]*100)) +  "%) = " + str(round(tmValue*multiplierArray[1], 2)) + "kg x" + str(repsArray[1]))
    print("(" + str(int(multiplierArray[2]*100)) +  "%) = " + str(round(tmValue*multiplierArray[2], 2)) + "kg x" + str(repsArray[2]))
    

def printWeeklyWork(arrayEx, arrayExName, setMultML, setMultAL, repsML, repsAL, warmupMults, repsWarmup, weekNmr):
    print("------------------------------------")
    print("Week " + weekNmr +":")
    print()

    counter = 0
    for ex in arrayEx:
        print("----- " + arrayExName[counter] + " Training Max = " + str(ex) + " -----")
        if (counter % 2 == 0):
            printSet(warmupMults, ex, repsWarmup) 
            printSet(setMultML, ex, repsML)
        else:
            printSet(setMultAL, ex, repsAL)
        
        print("----------------------------------------")
        print()
        counter+=1
     
    print()
    print("------------------------------------")


def printCycleWork(arrayEx, arrayExName, setMultML, setMultAL, repsML, repsAL, warmupMults, repsWarmup):
    # ------------------ calculate and show values for week1 ------------------------- 
    setMultML = [0.65, 0.75, 0.85]
    repsML = [5, 5, 5]

    setMultAL = [0.5, 0.6, 0.7]
    repsAL = [10, 10, 10]

    printWeeklyWork(arrayEx, arrayExName, setMultML, setMultAL, repsML, repsAL, warmupMults, repsWarmup, "1")
    # --------------------------------------------------------------------------------

    # ------------------ calculate and show values for week2 ------------------------- 
    setMultML = [0.7, 0.8, 0.9]
    repsML = [3, 3, 3]

    setMultAL = [0.6, 0.7, 0.8]
    repsAL = [8, 8, 6]

    printWeeklyWork(arrayEx, arrayExName, setMultML, setMultAL, repsML, repsAL, warmupMults, repsWarmup, "2")
    # --------------------------------------------------------------------------------

    # ------------------ calculate and show values for week3 ------------------------- 
    setMultML = [0.75, 0.85, 0.95]
    repsML = [5, 3, 1]

    setMultAL = [0.65, 0.75, 0.85]
    repsAL = [5, 5, 5]

    printWeeklyWork(arrayEx, arrayExName, setMultML, setMultAL, repsML, repsAL, warmupMults, repsWarmup, "3")
    # --------------------------------------------------------------------------------


def viewMaxes(arrayValue, arrayName):
    counter = 0
    for value in arrayValue:
        print()
        print("Your " + arrayName[counter] + " Training Max is: " + str(round(value, 2)))
        print("Your " + arrayName[counter] + " One Rep Max is: " + str(round(value/0.9, 2)))
        counter+=1


def changeMaxes(valueArray, nameArray, fileArray):
    print("\n\tChange TMs")
    print("Choose your option:")
    option = input("\t1 - Normal TM increse: 2.5kg for upper body lifts and 5kg for lower body (Recomended)\n\t2 - Double TM increse: 5kg for upper body lifts and 10kg for lower body\n\t3 - Reduce TMs: -2.5kg for upper body lifts and -5kg for lower body\n\t0 - Back\nValue(1, 2, 3 or 0): ")

    if (option != "0" and option != "1" and option != "2" and option != "3"):
        print("You inserted a wrong value, only available options are 1, 2, 3 or 0, try again")
        return changeMaxes(valueArray, nameArray, fileArray)

    if (option == "0"):
        return

    print ("\nOld values:")
    viewMaxes(valueArray, nameArray)
    
    if (option == "1"): 
        updateTMs(valueArray, 2.5, fileArray)

    if (option == "2"):
        updateTMs(valueArray, 5, fileArray)

    if (option == "3"):
        updateTMs(valueArray, -2.5, fileArray)

    readTMs(valueArray, fileArray, nameArray) #after writing to files, we need to read them again
    print("\nNew values:")
    viewMaxes(valueArray, nameArray)
    return changeMaxes(valueArray, nameArray, fileArray)


def writeAllTMs(valueArray, fileArray, nameArray):
    counter = 0
    for file in fileArray:
        number = input("Insert your " + nameArray[counter] + " Training Max: ")
        f = open(file, "w")
        f.write(number)
        valueArray[counter] = float(number) 
        f.close
        counter+=1
        

def writeTMs(valueArray, fileArray, nameArray):
    print("\n\tWrite TM for:")
    number = -1
    while (int(number) < 0 or int(number)) > 8: 
        number = input("1-OHP\n2-CGBench\n3-Deadlift\n4-FrontSquat\n5-Bench\n6-IBench\n7-Squat\n8-RDL\n0-Back\nValue(1, 2, 3, 4, 5, 6, 7, 8 or 0): ")
    writeOneTM(fileArray, nameArray, int(number)-1)
    readTMs(valueArray, fileArray, nameArray) #after writing to files, we need to read them again


def writeOneTM(fileArray, nameArray, index):
    TM = -1
    while (float(TM) < 0):
        print("o tm que foi passou pelo while foi: " + str(TM))
        try:
            TM = float(input("Insert your " + nameArray[index] + " Training Max: "))
        except ValueError:
            print("You inserted a wrong value, try again")
            TM = -1

    f = open(fileArray[index], "w")
    f.write(str(TM))
    f.close


def menu():
    print("\n\tMain menu")
    print("Choose your option:")
    option = input("\t1 - Print cycle work\n\t2 - View TM and 1RPMs\n\t3 - Increase TMs\n\t4 - Write TMs\n\t0 - Exit\nValue(1, 2, 3, 4 or 0): ")
    
    if (option == "0"):
        print("Goodbye") 
        return 1

    if (option == "1"):
        printCycleWork(arrayEx, arrayExName, setMultML, setMultAL, repsML, repsAL, warmupMults, repsWarmup)
        return menu()
    
    if (option == "2"):
        viewMaxes(arrayEx, arrayExName)
        return menu()
        
    if (option == "3"):
        changeMaxes(arrayEx, arrayExName, fileArray)
        return menu()

    if (option == "4"):
        writeTMs(arrayEx, fileArray, arrayExName)
        return menu()

    print("You inserted a wrong value, only available options are 1, 2, 3, 4 or 0, try again")
    return menu()




# --------- initialize constant values --------------------------
fileArray = ["trainingMaxes/ohpTM.txt", "trainingMaxes/cgbTM.txt", "trainingMaxes/dlTM.txt", "trainingMaxes/fsquatTM.txt", "trainingMaxes/benchTM.txt", "trainingMaxes/ibenchTM.txt", "trainingMaxes/squatTM.txt", "trainingMaxes/rdlTM.txt"]

arrayEx = []
arrayExName = ["OHP", "CGBench", "Deadlift", "Front Squat", "Bench", "InclineB", "Squat", "RDL"]

warmupMults = [0.4, 0.5, 0.6]
repsWarmup = [5, 5, 3]

setMultML = []
repsML = []
setMultAL = []
repsAL = []
# ---------------------------------------------------------------

# --------------- grab training maxes from files ----------------
readTMs(arrayEx, fileArray, arrayExName)
# ---------------------------------------------------------------


menu()
