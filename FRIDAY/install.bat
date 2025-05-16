@echo off
echo Setting up your AI Virtual Assistant environment...

:: Install pipwin first to make pyaudio installation easier
pip install pipwin
pipwin install pyaudio

:: Install other dependencies
pip install pyttsx3 speechrecognition wikipedia pywhatkit requests openai beautifulsoup4 lxml

echo ✅ All dependencies installed successfully.
pause
