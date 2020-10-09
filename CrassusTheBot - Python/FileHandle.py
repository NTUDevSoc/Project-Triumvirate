# Module - File Handling for the Bot
import random

# Function: Retrieve the Previous ID 
def RetrieveID (FileName):
    ReadPreviousID = open(FileName, "r")
        
    #Use .strip() to ensure it's only the numeric ID value stored
    PreviousID = int(ReadPreviousID.read().strip()) 
    ReadPreviousID.close()
        
    # Return the Twitter ID that was last responded to
    return PreviousID

# Function: Store the new value for the Previous ID      
def StoreID (IDNum, FileName):
    WritePreviousID = open(FileName, "w")
    WritePreviousID.write(str(IDNum))
    WritePreviousID.close()
    return

# Function: Get a random line form a file (Dad Jokes + Inspiration)
def FileReader(FileName):
    
    # Store the lines in a Dictionary 
    FileData = {"1" : "", "2" : "", "3" : "", "4" : "", 
                "5" : "", "6" : "", "7" : "", "8" : ""}
    
    Count = 1
    ReadFile = open(FileName, "r")
    
    # Go through each of the 8 keys
    for Line in ReadFile:
        Key = str(Count)
        FileData[Key] = Line
        Count += 1
        
    # Get a random key value to pick a random line from the file's contents
    RandKey = str(random.randint(1,8))
    Output = FileData[RandKey]
    return Output