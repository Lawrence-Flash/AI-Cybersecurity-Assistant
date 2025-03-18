import speech_recognition as sr
import pyttsx3
import subprocess



def speak(text):
    """ this function converts text to speech"""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    """ this function recognizes text to speech"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source) # reduce background noise
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You sad: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return None
    except sr.RequestError:
        print("Couldn't not connect tp speech recognition service.")
        return None

def run_nmap_scan(target):
    try:
        speak(f"Scanning {target} with Nmap...")
        result = subprocess.run(["Nmap", "-F", target], capture_output=True, text=True)
        print(result.stdout)
        speak("Scan complete. Check the terminal for results.")
    except Exception as e:
        speak("An error occured while scanning.")
        print("Error: ", e)

def main():
    speak("Hello! i am your AI cybersecurity assistant. How Can i help you?")
    while True:
        command = listen()
        if "Scan network" in command:
            speak("Please provide the target IP or domain.")
            target = listen()
            if target:
                run_nmap_scan(target)
        elif "exit" in command or "stop" in command:
            speak("Goodbye")
            break


if __name__ == "__main__":
    main()

