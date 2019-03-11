import winsound
import tkinter as tk
def play_sound(sound):
    winsound.PlaySound(sound+'.wav', winsound.SND_FILENAME)
root = tk.Tk()
snd1 = tk.Button(root, text='Damage', command=lambda: play_sound('damage'))
snd1.pack()
snd2 = tk.Button(root, text='Oof', command=lambda: play_sound('oof'))
snd2.pack()
root.title='soundboard'
root.iconbitmap('chief.ico')
root.mainloop()
