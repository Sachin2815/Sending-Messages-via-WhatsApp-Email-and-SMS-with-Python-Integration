import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import pyautogui

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print(f"Error with the speech recognition service; {e}")

    return None

def set_audio_output():
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)  # Select the desired voice (change the index if needed)
    engine.setProperty("output", "auto")  # Set the audio output to the default system audio

set_audio_output()

if __name__ == "__main__":
    while True:
        recognized_text = recognize_speech()
        if recognized_text:
            if "google" in recognized_text:
                speak("Opening Google.")
                webbrowser.open("https://www.google.com")
            elif "youtube" in recognized_text:
                speak("Opening YouTube.")
                webbrowser.open("https://www.youtube.com")
                # Wait for a moment before searching for music
                speak("What music would you like to listen to?")
                time.sleep(3)  # Wait for 3 seconds to give you time to respond
                music_name = recognize_speech()
                if music_name:
                    url = f"https://www.youtube.com/results?search_query={music_name}"
                    webbrowser.open(url)
                    time.sleep(5)  # Wait for the search results page to load
                    # Click on the first video link
                    try:
                        pyautogui.click(x=800, y=380)  # Adjust the coordinates as per your screen resolution
                    except pyautogui.FailSafeException:
                        print("Failed to click the video link. Please click it manually.")

            elif "python" in recognized_text and "code" in recognized_text:
                speak("Opening Chrome and searching for Python code.")
                webbrowser.open("https://www.google.com/search?q=Python+code")
            elif "exit" in recognized_text or "stop" in recognized_text:
                speak("Goodbye!")
                break
