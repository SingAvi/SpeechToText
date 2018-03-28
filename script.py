import speech_recognition as sr
import pyaudio

r = sr.Recognizer()

# audio='Recording.wav'  uncomment to insert a audio file

with sr.Microphone() as source:
    # with sr.AudioFile(audio) as source:   comment the above method and uncomment this line to enable read AudioFile
    print('Audio analysed')
    #   audio = r.record(source)    comment the next two line and uncomment
    r.adjust_for_ambient_noise(source, duration=5)
    audio = r.listen(source)

# print('Analysation done')  Random print method

try:
    print('Dellavi thinks you said \n' + r.recognize_google(audio))
# text =r.recognize_google(audio)                                    comment the above line and uncomment the followinf lines
#   print(text)

except Exception as e:
    print(e)


