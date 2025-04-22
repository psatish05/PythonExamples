from gtts import gTTS
import os
mytext = input("Enter the text: ")
language= 'en'
myobj=gTTS(text=mytext,lang=language,slow=False)
filename=f"{os.path.dirname(__file__)}\\audio.mp3"
myobj.save(filename)
os.system(filename)