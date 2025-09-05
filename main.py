import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary  # ensure this file exists

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif c.startswith("play"):
        song = c.replace("play", "").strip()
        link = musiclibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}")

if __name__ == "__main__":
    speak("Initializing hello ...")
    while True:
        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                word = recognizer.recognize_google(audio)

                if word.lower() == "hello":
                    speak("How can I help you?")
                    with sr.Microphone() as source:
                        print("hello Active...")
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        processCommand(command)

        except Exception as e:
            print("Error:", e)
