
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize listener and engine
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set voice to a female one


def talk(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()


def take_command():
    """Listen for voice input and process it."""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except Exception as e:
        print("Error:", e)
        command = ""
    return command


def run_alexa():
    """Main function to execute commands."""
    command = take_command()
    print(f"Command: {command}")
    if 'play' in command:
        song = command.replace('play', '').strip()
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'Current time is {time}')
    elif 'who is' in command or 'who the heck is' in command:
        person = command.replace('who is', '').replace('who the heck is', '').strip()
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry, I have a headache.')
    elif 'are you single' in command:
        talk('I am in a relationship with WiFi.')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


# Run Alexa continuously
if __name__ == "__main__":
    while True:
        run_alexa()

