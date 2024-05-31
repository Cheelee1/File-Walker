"""
Aurelio R Amparo III
Program: File Walker
"""
import os
def Main():
    while True:
        userInput = input("Please input directory (0)to quit: ")
        if os.path.isdir(userInput):
            print("----"+os.path.basename(userInput)+"----")
            FileWalker(userInput)
            break
        elif (userInput == "0"):
            break
        else:
            continue




def FileWalker(fileDir, count = 1):
    # cheack is input is a directory
    if os.path.isdir(fileDir):
        # loops what is inside directory
        for i in os.listdir(fileDir):
            filename = os.path.join(fileDir,i)
            # is it is a dir it will call itself
            # each time it walks through a subdir it adds |*count(level of recusion)
            if os.path.isdir(filename):
                print("|"*count + os.path.basename(i))
                FileWalker(os.path.join(fileDir,i),count+1)

            else:
                print("|"*(count) +os.path.basename(i))

    else:
        return None
Main()
