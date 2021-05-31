from pygame import mixer
print("Welcome to Healthy programmer")

def eye_exercise():
    mixer.init()
    mixer.music.load("eye.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()
     
def water_exercise():
    mixer.init()
    mixer.music.load("water.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()
def physical_exercise():
    mixer.init()
    mixer.music.load("physical.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()
