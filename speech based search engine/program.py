import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print("You said:", query)
            return query
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
        except sr.RequestError:
            speak("Sorry, speech service is unavailable.")
    return ""

def search(query):
    speak("Searching on Google...")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def main():
    query = listen()
    if query:
        search(query)

if __name__ == "__main__":
    main()
