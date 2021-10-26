def two_fer(name = "you"): #take input argument and store as string
    if "you" == None: #if string is empty, print a default response
        return("One for you, one for me.")

    else:        #if string contains characters, concatenate and print statement
        return("One for " + name + ", one for me.") 
