import wikipedia
import pywhatkit
from utils.speech import speak

def handle_web_command(command):
    if "search" in command:
        query = command.replace("search", "")
        pywhatkit.search(query)
        speak(f"Searching {query} on Google.")
        return True
    elif "youtube" in command:
        query = command.replace("youtube", "")
        pywhatkit.playonyt(query)
        speak(f"Playing {query} on YouTube.")
        return True
    elif "who is" in command or "what is" in command:
        try:
            summary = wikipedia.summary(command, sentences=2)
            speak(summary)
        except:
            speak("Sorry, I couldn't find any information.")
        return True
    return False
