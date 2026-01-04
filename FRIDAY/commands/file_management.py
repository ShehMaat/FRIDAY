import os
from utils.speech import speak
from database.database import SessionLocal
from database.models import FileLog

def create_file(filename, content):
    try:
        with open(filename, 'w') as f:
            f.write(content)
        
        # Log to DB
        db = SessionLocal()
        new_log = FileLog(filename=filename, path=os.path.abspath(filename), action="Created", description=f"Content length: {len(content)}")
        db.add(new_log)
        db.commit()
        db.close()
        
        speak(f"File {filename} created successfully.")
        return True
    except Exception as e:
        speak(f"Error creating file: {e}")
        return False

def read_file(filename):
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                content = f.read()
            
            # Log to DB
            db = SessionLocal()
            new_log = FileLog(filename=filename, path=os.path.abspath(filename), action="Read")
            db.add(new_log)
            db.commit()
            db.close()
            
            speak(f"Reading {filename}: {content}")
            return True
        except Exception as e:
            speak(f"Error reading file: {e}")
            return False
    else:
        speak("File not found.")
        return False

def delete_file(filename):
    if os.path.exists(filename):
        try:
            os.remove(filename)
            
            # Log to DB
            db = SessionLocal()
            new_log = FileLog(filename=filename, path=os.path.abspath(filename), action="Deleted")
            db.add(new_log)
            db.commit()
            db.close()
            
            speak(f"File {filename} deleted.")
            return True
        except Exception as e:
            speak(f"Error deleting file: {e}")
            return False
    else:
        speak("File not found.")
        return False

def handle_file_command(command):
    command = command.lower()
    if "create file" in command:
        # Expected format: "create file <filename> with content <content>"
        parts = command.split("create file")
        if len(parts) > 1:
            details = parts[1].strip()
            if "with content" in details:
                filename, content = details.split("with content", 1)
                create_file(filename.strip(), content.strip())
            else:
                # simple creation with empty or default content? or ask user?
                # For now assume simple syntax "create file X"
                create_file(details.strip(), "")
        return True
    
    elif "read file" in command:
        filename = command.replace("read file", "").strip()
        read_file(filename)
        return True
        
    elif "delete file" in command:
        filename = command.replace("delete file", "").strip()
        delete_file(filename)
        return True
        
    return False
