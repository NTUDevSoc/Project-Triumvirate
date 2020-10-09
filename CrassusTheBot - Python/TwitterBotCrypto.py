# Import relevant modules
import tweepy
import time
RunProgram = True

# Import our own file-handling module
import FileHandle

# Variable for GUI Status Updates
StatusText = ""

# File containing the Twitter ID of the last person the bot responded to
PreviousIDFile = "Previous_ID.txt"

# File containing all of the jokes
JokesFile = "Stored_Jokes.txt"

# File containing all of the quotes
QuotesFile = "Stored_Quotes.txt"

AuthStatus = False

# Authentication process in order to access the twitter account @Spoopy_B0t
# Access Tokens for the Accounts
auth = tweepy.OAuthHandler("Value1", 
    "Value2")
auth.set_access_token("Value3", 
    "Value4")

api = tweepy.API(auth)

# Authenticate the Tokens
try:
    api.verify_credentials()
    StatusText = "Authentication OK - Ready to go"
    AuthStatus = True
except:
    StatusText = "Error during authentication - Bot is unavailable"
    AuthStatus = False



def ReplyingToTweets():
    
    # Obtain the Authentication Status to check whether or not it was succesful
    global AuthStatus
    
    # Only run this program if AuthStatus == True
    if AuthStatus:
        print("Checking for new tweets in my @mentions")
        
        # Update the Bot's Bio to tell people they're online
        api.update_profile(description = "Hey there! I'm back online at the moment :) Feel free to try out my #commands. I take about 30 - 60 seconds to reply.")
    
        # Find the Twitter ID of the last person the bot replied to
        LastID = FileHandle.RetrieveID(PreviousIDFile)
        
        # Get the mentions timeline of the Bot
        Mentions = api.mentions_timeline(LastID, tweet_mode = "extended")
    
        # Reverse it due to how the twitter timeline is structured (Read from Bottom --> Top)
        for Mention in reversed (Mentions):
            
            # Display the Mention tweet with the User ID attached to it (For main console only NOT GUI)
            NewMention = str(Mention.id) + " --- " + Mention.full_text
            print (NewMention)
            
            # Update the Status Box with the User ID and their Tweet
            try:
                print("New Mention From: " + str(Mention.id) + " --- " + Mention.full_text)
            except:
               print("New Mention From: " + str(Mention.id) + " --- " + " Message too long")
            
            # Store the new ID as previous ID
            LastID = Mention.id
            FileHandle.StoreID(LastID, PreviousIDFile)
            
            # Say hello to some friends!
            if "#hellobot" in Mention.full_text.lower():
                try:
                    api.update_status('@' + Mention.user.screen_name + 
                                      " Heyo! Thanks for checking in on me :) Hope you're having a swell day! Checkout my pinned tweets for some cool commands.")
                    print("Saying hello!")
                    
                except:
                    print("Error: Unable to say hello")

            # Give commands
            if "#commands" in Mention.full_text.lower():
                try:
                    api.update_status('@' + Mention.user.screen_name + 
                                      " All of my commands are listed in my pinned tweet ... though I have a few secret ones that you'll have to guess.")
                    print("Give commands!")
                    
                except:
                    print("Error: Unable to give commands")
            
            # Dad Joke TIME :)
            if "#dadjoke" in Mention.full_text.lower():
                try:
                    api.update_status("Hello there " + "@" + Mention.user.screen_name + 
                                      ", I'm dad." + " Here's a joke: " + FileHandle.FileReader(JokesFile))
                    print("Dad Joke TIME - finding a joke")
                    
                except:
                    print("Error: Unable to make a dad joke")
            
            # Send a DM :)
            if "#dmtime" in Mention.full_text.lower():
                try:
                    api.send_direct_message(Mention.user.id, "Hi there! This is a DM ;)")
                    print("It's DM o'clock")
                    
                except:
                    print("Error: Unable to DM this person")
                    api.update_status("Sorry " + "@" + Mention.user.screen_name + 
                                      ", but I can't seem to DM you due to one of your privacy settings - you need to allow DM requests.s")
                    
            # Send a HINT :)
            if "#hint" in Mention.full_text.lower():
                try:
                    api.send_direct_message(Mention.user.id, "All #ProjectTriumvirate members drink Fernet. A good drink and a good cipher.")
                    print("Looks like someone needs a hint ;)")
                    
                except:
                    print("Error: Unable to DM this person")
                    api.update_status("Sorry " + "@" + Mention.user.screen_name + 
                                      ", but I can't seem to DM you due to one of your privacy settings - you need to allow DM requests.")

            # Send a HINT 2.0.1 :)
            if "#projectredacted" in Mention.full_text.lower():
                try:
                    api.send_direct_message(Mention.user.id, "Shh ... not out in the open ... you need to use the correct name so I know you are one of us.")
                    print("Looks like someone needs a hint ;)")
                    
                except:
                    print("Error: Unable to DM this person")
                    api.update_status("Sorry " + "@" + Mention.user.screen_name + 
                                      ", but I can't seem to DM you due to one of your privacy settings - you need to allow DM requests.")

            # Send a HINT 2.0.2 :)
            if "#projectredacted" in Mention.full_text.lower():
                try:
                    api.update_status("@" + Mention.user.screen_name + " I have no idea of what you're talking about ...")
                    print("Looks like someone needs another hint ;)")
                    
                except:
                    print("Error: Unable to send a hint 2.0.2")
                    
                    
            # Send a FERNET TOKEN :)
            if "#projecttriumvirate" in Mention.full_text.lower():
                try:
                    api.send_direct_message(Mention.user.id, "Ah, a fellow member of the project. Here is your TOKEN: gAAAAABfaghSISQWLZdvKcg-FPOhw1o9FkWOOCIbW94DRUKXVdL9EosuDJe8Rm3fg5dX2NlyYXFvfW-tVKXyH7tV0dYurbLzuJLHxNdDB-j86i9__FN9JV4=")
                    print("It's TOKEN Time")
                    
                except:
                    print("Error: Unable to DM this person")
                    api.update_status("Sorry " + "@" + Mention.user.screen_name + 
                                      ", but I can't seem to DM you due to one of your privacy settings - you need to allow DM requests.")
            
            # Get some inspiration
            if "#inspiration" in Mention.full_text.lower():
                try:
                    api.update_status("@" + Mention.user.screen_name + " " + FileHandle.FileReader(QuotesFile))
                    print("Providing some daily inspiration")
                    
                except:
                    print("Error: Unable to send a quote")
                    
            # Follow the user
            if "#followme" in Mention.full_text.lower():
                try:
                    api.create_friendship(Mention.user.id)
                    print("Helping them up their follower count")
                    
                except:
                    print("Error: Unable to Follow this person")
                    
        # Inform user that all mentions have been responded to
        print("No more new pending @mentions, try checking again later")
    
    # If AuthStatus == False stop user from trying to check timeline
    else:
        print("Authentication Failed - Stop Bot and Check Tokens")
    


# Run the program
def StartProgram():
    ReplyingToTweets()
    

while RunProgram == True:
    StartProgram()
    time.sleep(50)
