import winsound
import tkinter as tk
import json
import re
global snds
snds = []
def play_sound(sound):
    winsound.PlaySound(sound+'.wav', winsound.SND_FILENAME)
def addSound():
    global soundPath
    global createSound
    createSound = tk.Toplevel() 
    createSound.geometry("100x40+100+100")
    soundPath = tk.Entry(createSound)
    soundPath.pack()
    sndBtn = tk.Button(createSound, command=editJson, text="Add Sound")
    sndBtn.pack(fill='x')
def editJson():
    name = soundPath.get()
    with open("data/data.json",'r') as f:
        data = json.load(f)
        sndAmount = int(data['sounds']['aos']) 
        data['sounds']['aos'] = sndAmount + 1
        print(data)
        f.close()
        data['sounds'][str(sndAmount)] = name
        writePath(data)
def writePath(data):
    with open("data/data.json",'w') as f:
        json.dump(data, f)
        f.close()
        createSound.destroy()
        loadSounds()
def loadSounds():
    snds.clear()
    with open("data/data.json") as f:
        data = json.load(f)
        #print(data['aos'])
        sndAmount = int(data['sounds']['aos'])
        for i in range(0,sndAmount):
            #print(i)
            print(len(snds))
            if len(snds) >= sndAmount:
                snds[i].destroy()
            print(i)
            print(data['sounds'][str(i)])
            sndNames = str(data['sounds'][str(i)])
            print(sndNames)
            sndNames = re.sub('[^A-Za-z0-9]+', '', sndNames)
            print(sndNames)
            snds.append(tk.Button(root, text=sndNames, command=lambda: play_sound(data['sounds'][str(i)])))
            snds[i].pack(fill='x')
            f.close()
def comingSoon():
	tkMessageBox.showinfo(title="Coming Soon", message="This feature is still in development.")
root = tk.Tk()
menubar = tk.Menu(root)
root.geometry("250x200+100+100")
root.config(menu=menubar)       
loadSounds()
menubar.add_command(label="New Sound", command=addSound)
menubar.add_command(label="Stop All Sound", command=comingSoon)
menubar.add_command(label="Help", command=comingSoon)
menubar.add_command(label="Exit", command=comingSoon)
root.config(menu=menubar)
root.title('soundboard')
root.mainloop()
