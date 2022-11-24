import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Now!")
    audio = r.listen(source)
    speech_text = r.recognize_google(audio)
    print(speech_text)
