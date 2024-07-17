# durga.py

import speech_recognition as sr
import subprocess  # For executing external commands
import whatsapp

def main():
    while True:
        command = listen_for_command()
        
        if "hey durga" in command:
            print("Opening WhatsApp...")
            whatsapp.open_whatsapp()
        
        elif "send message" in command:
            contact_name = extract_contact_name(command)
            if contact_name:
                message = extract_message(command)
                if message:
                    whatsapp.send_message(contact_name, message)
        
        elif "exit" in command:
            print("Exiting Durga.")
            break
        
        else:
            print("Command not recognized.")

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Command received: {command}")
        return command
    except sr.UnknownValueError:
        print("Could not understand audio.")
    return ""

def extract_contact_name(command):
    # Extract contact name logic based on your specific commands
    # Example implementation:
    if "to" in command:
        parts = command.split("to")
        return parts[1].strip()
    return None

def extract_message(command):
    # Extract message logic based on your specific commands
    # Example implementation:
    if "message" in command:
        parts = command.split("message")
        return parts[1].strip()
    return None

if __name__ == "__main__":
    main()
