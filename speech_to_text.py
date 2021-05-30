import speech_recognition as sp

audio_file_path=r"C:\Users\Mani\OneDrive\Desktop\message.mp3"

r=sp.Recognizer()

#From audio file convert to text
with sp.AudioFile(audio_file_path) as audio_input:
    audio_record=r.record(audio_input)
    audio_to_text=r.recognize_google(audio_record)
    print(audio_to_text)
    
    
#Through microphone convert to text  
#with sp.Microphone() as source:
    #print("speak")
    ##audio=r.listen(source)
    #audio_to_text=r.recognize_google(audio)
    #print(audio_to_text)

