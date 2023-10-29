import pyttsx3

def recursiveFunction():
    user_input = input("Ask: ")
    
    engine = pyttsx3.init()

    if "naam batayein" in user_input:
        response = "Bhupendra Jogi"
    else:
        response = "Bhupendra jogi"
    
    print(response)
    engine.say(response)
    engine.runAndWait()
    
    recursiveFunction()  # No base case, creates an Infinite Loop!

print("Interview Starts..")
recursiveFunction()  # Starting Recursion

