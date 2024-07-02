import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import smtplib,ssl
import base64
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from twilio.rest import Client






listener = sr.Recognizer()
engine = pyttsx3.init()
emaildict = {"roshni":"roshninekkanti@gamil.com","swarupa":"nekkantiswarupa@gamil.com"}
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say('I am your rishi')
engine.say('what can I do for you')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print("rishi is Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'rishi' in command:
                command = command.replace('rishi', '')
                print(command)
    except:
        pass
    return command




def run_rishi():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play','')
        talk('playing '+ song)
        pywhatkit.playonyt(song)

    elif 'hello' in command:
        talk('helloo beautiful')

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%p')
        print(time)
        talk('current time is '+ time)

    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,2) #number of lines in summary
        print(info)
        talk(info)

    elif 'about a date' in command:
        repl1 = command.replace('how about a date','')
        talk('hello')

    elif 'are you single' in command:
        reply2 = command.replace('are you single','')
        talk('not everyone are single and useless like you')

    elif 'marry me' in command:
        reply3 = command.replace('marry me','')
        talk('i hate you')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    #elif 'open youtube' in command:
    #    webbrowser.open("youtube.com")
    elif 'open google' in command:
        webbrowser.open("google.com")
    elif 'open stackoverflow' in command:
        webbrowser.open("stackoverflow.com")



    #elif 'play music' in query:
        #music_dir = 'D:\\non critical\\songs\\favourite songs'
        #songs = os.listdir(music_dir)
        #print(songs)
        #os.startfile(os.path.join(music_dir,songs[0]))
    
    #elif 'open code' in command:
    #    codepath = "C:\Users\roshn\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk"
    #    os.startfile(codepath)
    
    
    elif 'email to roshni' in command:
        try:
            talk("what should i say?")
            content = take_command()
            talk("whom to send ?")
            to = emaildict[take_command()]


            creds = Credentials.from_authorized_user_file('credentials.json', ['https://www.googleapis.com/auth/gmail.send'])
            message = MIMEMultipart()
            message['to'] = to
            message.attach(MIMEText(content, 'plain'))
            raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
            service = build('gmail', 'v1', credentials=creds)
            message = service.users().messages().send(userId='me', content={'raw': raw_message}).execute()

            talk("email has been sent!")
        except Exception as e:
            print(e)
            talk("not able to send email")

    elif 'call' in command:
        account_sid = 'AC60c907348cfdc8dbb23f5bd9af36269e'
        auth_token = '8603053c99829507ddc2577ec539741a'
        from_number = '+91 77999 09775'  # Your Twilio phone number
        to_number = '+91 93980 99131'
        client = Client(account_sid, auth_token)
        call = client.calls.create(
        twiml='<Response><Say> heloooooooo brotherrr... </Say></Response>',
        to=to_number,
        from_=from_number
        )
        talk("called sucessfully")

    else:
        talk('please say the command  again.')

run_rishi()


