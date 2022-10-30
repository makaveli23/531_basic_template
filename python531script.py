import array


def roundToPlates(n):
    print("TODO")
    basenmr = n%10


def readTMs(array, file):
    f = open(file, "r")
    array.append(float(f.read())) 
    f.close()


def printWeeklyWork(arrayEx, arrayExName, setMultML, setMultAL, repsML, repsAL, warmupMults):
    counter = 0
    for ex in arrayEx:
        print("----- " + arrayExName[counter] + " Training Max = " + str(ex) + " -----")
        if (counter % 2 == 0):
        #if (1): #for warmup weeks, comment this and uncomment above line for normal weeks
            print("warmup 1(" + str(int(warmupMults[0]*100)) +  "%) = " + str(round(ex*warmupMults[0], 2)) + "kg x5")
            print("warmup 2(" + str(int(warmupMults[1]*100)) +  "%) = " + str(round(ex*warmupMults[1], 2)) + "kg x5")
            print("warmup 3(" + str(int(warmupMults[2]*100)) +  "%) = " + str(round(ex*warmupMults[2], 2)) + "kg x3")
            print("first set(" + str(int(setMultML[0]*100)) +  "%) = " + str(round(ex*setMultML[0], 2)) + "kg x" + str(repsML[0]))
            print("second set(" + str(int(setMultML[1]*100)) +  "%) = " + str(round(ex*setMultML[1], 2)) + "kg x" + str(repsML[1]))
            print("last set(" + str(int(setMultML[2]*100)) +  "%) = " + str(round(ex*setMultML[2], 2)) + "kg x" + str(repsML[2]))
        else:
            print("first set(" + str(int(setMultAL[0]*100)) +  "%) = " + str(round(ex*setMultAL[0], 2)) + "kg x" + str(repsAL[0]))
            print("second set(" + str(int(setMultAL[1]*100)) +  "%) = " + str(round(ex*setMultAL[1], 2)) + "kg x" + str(repsAL[1]))
            print("last set(" + str(int(setMultAL[2]*100)) +  "%) = " + str(round(ex*setMultAL[2], 2)) + "kg x" + str(repsAL[2]))
     
        print("----------------------------------------")
        print()
        counter+=1
     



#constant values

arrayEx = []
arrayExName = ["OHP", "CGBench", "Deadlift", "Front Squat", "Bench", "InclineB", "Squat", "RDL"]


warmupMults = [0.4, 0.5, 0.6]




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



#calculate and show values for week1

setMultML = [0.65, 0.75, 0.85]
repsML = [5, 5, 5]

setMultAL = [0.5, 0.6, 0.7]
repsAL = [10, 10, 10]

print("------------------------------------")
print("Week 1:")
print()
printWeeklyWork(arrayEx, arrayExName, setMultML, setMultAL, repsML, repsAL, warmupMults)
print()
print("------------------------------------")


#calculate and show values for week2

setMultML = [0.7, 0.8, 0.9]
repsML = [3, 3, 3]

setMultAL = [0.6, 0.7, 0.8]
repsAL = [8, 8, 6]

print("------------------------------------")
print("Week 2:")
print()
printWeeklyWork(arrayEx, arrayExName, setMultML, setMultAL, repsML, repsAL, warmupMults)
print()
print("------------------------------------")


#calculate and show values for week3

setMultML = [0.75, 0.85, 0.95]
repsML = [5, 3, 1]

setMultAL = [0.65, 0.75, 0.85]
repsAL = [5, 5, 5]

print("------------------------------------")
print("Week 3:")
print()
printWeeklyWork(arrayEx, arrayExName, setMultML, setMultAL, repsML, repsAL, warmupMults)
print()
print("------------------------------------")



#calculate and show values for week4

#setMultML = [0.65, 0.75, 0.85]
#repsML = [5, 5, 5]
#
#setMultAL = [0.6, 0.7, 0.8]
#repsAL = [8, 8, 6]
#
#print("------------------------------------")
#print("Week 4:")
#print()
#printWeeklyWork(arrayEx, arrayExName, setMultML, setMultAL, repsML, repsAL)
#print()
#print("------------------------------------")


