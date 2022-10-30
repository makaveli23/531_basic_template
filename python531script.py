import array


def roundToPlates(n):
    print("TODO")
    basenmr = n%10


def readTMs(valueArray, file):
    f = open(file, "r")
    valueArray.append(float(f.read())) 
    f.close()


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


def menu():
    print()
    print("Choose your option:")
    option = input("\t1 - Print cycle work\n\t2 - View TM and 1RPMs\n\t3 - Increase TMs(TODO)\n\t0- Exit\nValue(1, 2, 3 or 0): ")
    
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
        print("todo")
        return menu()


    print("You inserted a wrong value, only available options are 1, 2, 3 or 0, try again")
    return menu()



# --------- initialize constant values -------------------------
arrayEx = []
arrayExName = ["OHP", "CGBench", "Deadlift", "Front Squat", "Bench", "InclineB", "Squat", "RDL"]

warmupMults = [0.4, 0.5, 0.6]
repsWarmup = [5, 5, 3]

setMultML = []
repsML = []
setMultAL = []
repsAL = []

#--------------- grab training maxes from files -----------------------------
readTMs(arrayEx, "trainingMaxes/ohpTM.txt")
readTMs(arrayEx, "trainingMaxes/cgbTM.txt")
readTMs(arrayEx, "trainingMaxes/dlTM.txt")
readTMs(arrayEx, "trainingMaxes/fsquatTM.txt")
readTMs(arrayEx, "trainingMaxes/benchTM.txt")
readTMs(arrayEx, "trainingMaxes/ibenchTM.txt")
readTMs(arrayEx, "trainingMaxes/squatTM.txt")
readTMs(arrayEx, "trainingMaxes/rdlTM.txt")

# -----------------------------------------------------------------------


menu()


