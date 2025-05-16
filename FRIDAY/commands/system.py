import os
from utils.speech import speak

def handle_system_command(command):
    if "open notepad" in command:
        os.system("notepad")
        speak("Opening Notepad.")
        return True
    elif "open calculator" in command:
        os.system("calc")
        speak("Opening Calculator.")
        return True
    return False
