from utils.speech import listen, speak
from commands.system import handle_system_command
from commands.web import handle_web_command
import datetime
from gpt_module import ask_gpt


def main():
    speak("Hello, I am your assistant. How can I help you today?")
    
    while True:
        command = listen()

        if not command:
            continue

        if "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        elif "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {now}")
        
        elif handle_system_command(command):
            continue
        elif handle_web_command(command):
            continue
        elif "question" in command or "explain" in command or "what is" in command:
            speak("What would you like to ask?")
            user_input = listen()
            if user_input:
                speak("Thinking...")
                response = ask_gpt(user_input)
                speak(response)

        else:
            speak("I'm not sure how to help with that yet.")

if __name__ == "__main__":
    main()

