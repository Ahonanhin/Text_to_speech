import tkinter as tk
import pyttsx3


# using pyttsx3 module to convert text to speech
def text_to_speech_converter(text_entry):
    text_speech = pyttsx3.init()
    words = text_entry.get("1.0", tk.END)
    text_speech.say(words)
    text_speech.runAndWait()

# reset the text entry
def reset(text_entry):
    text_entry.delete("1.0", "end")

#
def main():
    # window
    app_window = tk.Tk()
    app_window.title("Text-to-speech 1.0")
    app_window.configure(width=1600, height=1200, bg="lightblue")

    main_title = tk.Label(app_window, text="Enter your text", font="Times 18", bg="light blue")
    main_title.grid(row=0, column=3)

    text_entry = tk.Text(app_window, font="Times 14")
    text_entry.grid(row=1, column=3)

    convert = tk.Button(app_window, text="Convert", bd=5, bg="light green", fg="black", font="Times",
                        command=lambda: text_to_speech_converter(text_entry))
    convert.grid(row=8, column=1)

    reset_button = tk.Button(app_window, text="Clear", bd="10", bg='Light Green',
                             command=lambda: reset(text_entry))
    reset_button.grid(row=8, column=3)

    exit_button = tk.Button(app_window, text="Exit", bd="10", bg="Light Green", command=app_window.destroy)
    exit_button.grid(row=8, column=10)

    # infinite loop to run program until user exits
    app_window.mainloop()


if __name__ == "__main__":
    main()
