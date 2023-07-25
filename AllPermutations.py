def allPermute(numberStr, comboList = [],addString = ''):
    
    if type(numberStr) == int or float:
        numberStr = str(numberStr)
    if len(numberStr) == 1: #Base case. If length is 1 only combo is itself
        return numberStr
    
    #Recursive step
    else:
        for i in range(len(numberStr)):
            #Checks if the number string is 2
            if len(numberStr) == 2:
                tempStr = addString #Set a temporary variable that takes addString current value
                addString += numberStr[i]

                #Part of the recursive step. This shortens the string by one character to get a single character.
                #allPermute then returns that single number and appends it onto the list
                comboList.append(addString + allPermute(numberStr[0:i] + numberStr[i+1:],
                                                      comboList,addString))
                addString = tempStr #Reset addString to tempStr such that it won't keep growing everytime we add a chracter

            #numberStr must be bigger than two
            else:
                tempStr1 = addString #Sets the current value of addString to tempStr1
                addString += numberStr[i] #Add the ith string of numberString to addString
                allPermute(numberStr[0:i] + numberStr[i+1:],
                         comboList,addString) #Shortens the numberStr inputed by 1 and run allPermute.
                addString = tempStr1 #Reset addString to tempStr1 such that it won't keep growing everytime we add a character to it
    return comboList


#Writes all the permutations into a file
customStr = str(input("Enter the number or string you want all combinations of: "))#Input and cast it as a str
outFile = open("AllPermute_of_" + customStr + ".txt","w") #Open a file with a custom name
comList = allPermute(customStr) #Run allPermute
for element in range(len(comList)): #Write each element into the file
    if element != len(comList) -1:
        outFile.write(comList[element] + "\n")
    else:
        outFile.write(comList[element])
outFile.close() #Close the file
test
