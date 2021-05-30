import pyttsx3 as py

init=py.init()
init.setProperty("rate",110)
init.setProperty("volume",0.8)
init.save_to_file("Hi All, please be safe", "virus.mp3")
init.runAndWait()

#C:\Users\Mani\OneDrive\Desktop\virus.mp3
