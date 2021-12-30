# importing libraries 
import tkinter
import pyttsx3
import playsound

def text_to_speech_converter():
    text_speech = pyttsx3.init()
    words = text_entry.get("1.0", END)
    text_speech.say(words)
    text_speech.runAndWait()
def reset():
    text_entry.delete("1.0", "end")

# window
from tkinter import *
# declaring the window
appWindow = Tk()
# Creating the window title
appWindow.title("Text-to-speech 1.0")
# window dimensions
appWindow.configure(width = 1600, height = 1200)
# window colors
appWindow.configure(bg = "lightblue")
# App Title label
main_title = tkinter.Label(appWindow, text = "Enter your text", 
font = "Times 18", bg= "light blue").grid(row=0,column = 3)

text_entry = tkinter.Text(appWindow, font= "Times 14")
text_entry.grid(row=1, column=3)

# Creating the conversion button
convert = tkinter.Button(appWindow, text = "Convert", bd= 5, bg = "light green",
fg = "black", font = "Times",
 command= text_to_speech_converter)
convert.grid(row = 8, column =1 )

#creating the reset button
reset_button = tkinter.Button(appWindow, text = "Clear" , bd ="10", bg = 'Light Green', 
command = reset)
reset_button.grid(row = 8, column = 3)

# Creating the exit Button
exit_button = tkinter.Button(appWindow, text = "Exit", bd = "10",
 bg = "Light Green", command= appWindow.destroy)
exit_button.grid(row = 8, column =10)


appWindow.mainloop()

