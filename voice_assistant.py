import speech_recognition as sr
import pyttsx3

recognizer  = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        
        except sr.UnknownValueError:
            print("SORRY, I COULDN'T UNDERSTAND")
            return ""
        
        except sr.RequestError:
            print("API unavailable.")
            return ""
while True:
    command = listen()
    if "hello" in command:
        speak("hello! how can I help you?")
    elif "exit" in command:
        speak("Goodbye!")
        break                