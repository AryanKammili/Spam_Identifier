import tkinter as tk
import numpy as np
from ExtractInfo import ExtractInfo
from Identifier import Identifier

identifier = Identifier()

x_train, x_test, y_train, y_test = identifier.getLists()

identifier.train(x_train, y_train)

window = tk.Tk()

window.attributes("-fullscreen", True)

window.title("Spam Identifier")

icon = tk.PhotoImage(file='stop_spam.png')

window.iconphoto(True, icon)

window.config(background="black")

window.geometry("360x360")

light_Blue = "#4E7CAD"
navy = "#004080"
blue_Blush = "#6C8CA9"
black = "#040401"

mid = 0.5

all = our = remove = receive = credit = 0
freq000 = free = email = george = data = 0
freq415 = original = edu = semicolon = 0
exclamation = capital_Average = capital_Longest = 0
capital_Total = 0

x_list = []

result = string = None

button_height = 4
button_width = 15


def toggle_Screen(event):
    # Toggle fullscreen mode
    window.attributes('-fullscreen', not window.attributes('-fullscreen'))


def Close():
    window.destroy()


def Submit():
    text = entry.get()
    extract = ExtractInfo(text)

    global all, our, remove, receive, credit, freq000, free, email, george, data
    global freq415, original, edu, semicolon, exclamation, capital_Average
    global capital_Longest, capital_Total
    global x_list, result, string

    all = extract.getFreqAll()
    our = extract.getFreqOur()
    remove = extract.getFreqRemove()
    receive = extract.getFreqReceive()
    credit = extract.getFreqCredit()
    freq000 = extract.getFreq000()
    free = extract.getFreqFree()
    email = extract.getFreqEmail()
    george = extract.getFreqGeorge()
    data = extract.getFreqData()
    freq415 = extract.getFreq415()
    original = extract.getFreqOriginal()
    edu = extract.getFreqEdu()
    semicolon = extract.getFreqSemicolon()
    exclamation = extract.getFreqExclamation()
    capital_Average = extract.getCapital_run_length_average()
    capital_Longest = extract.getCapital_run_length_longest()
    capital_Total = extract.getCapital_run_length_total()

    x_list = np.array([
        all, our, remove, receive, credit,
        freq000, free, email, george, data,
        freq415, original, edu, semicolon,
        exclamation, capital_Average, capital_Longest,
        capital_Total])

    x_list = x_list.reshape(1, -1)

    result = identifier.predict(x_list)

    string = "Result: " + result

    status.config(text=string)


def Reset():
    status.config(text="Result: ")
    Delete()
    entry.insert(0, "Insert Text Here")

    global all, our, remove, receive, credit, freq000, free, email, george, data
    global freq415, original, edu, semicolon, exclamation, capital_Average
    global capital_Longest, capital_Total
    global x_list, result, string

    all = our = remove = receive = credit = 0
    freq000 = free = email = george = data = 0
    freq415 = original = edu = semicolon = 0
    exclamation = capital_Average = capital_Longest = 0
    capital_Total = 0

    x_list = []

    result = string = None


def Delete():
    text = entry.get()
    entry.delete(0, len(text))


window.bind('<Escape>', toggle_Screen)

title = tk.Label(window,
    background=light_Blue,
    foreground=black,
    activebackground=navy,
    activeforeground=blue_Blush,
    highlightthickness=2,
    highlightcolor='WHITE',
    width=button_width,
    height=button_height,
    text="Spam Detector",
    font=("Arial", 35, "bold"))

title.pack(fill=tk.X, side=tk.TOP)

buttonSubmit = tk.Button(window,
    background=light_Blue,
    foreground=black,
    activebackground=navy,
    activeforeground=blue_Blush,
    highlightthickness=2,
    highlightcolor='WHITE',
    command=Submit,
    width=button_width,
    height=button_height,
    text="Submit Text",
    font=("Arial", 16, "bold"))

buttonSubmit.place(x=100, rely=mid)

buttonExit = tk.Button(window,
    background=light_Blue,
    foreground=black,
    activebackground=navy,
    activeforeground=blue_Blush,
    highlightthickness=2,
    highlightcolor='WHITE',
    command=Close,
    width=button_width,
    height=button_height,
    text="Exit",
    font=("Arial", 16, "bold"))

buttonExit.place(x=400, rely=mid)

buttonDelete = tk.Button(window,
    background=light_Blue,
    foreground=black,
    activebackground=navy,
    activeforeground=blue_Blush,
    highlightthickness=2,
    highlightcolor='WHITE',
    command=Delete,
    width=button_width,
    height=button_height,
    text="Delete",
    font=("Arial", 16, "bold"))

buttonDelete.place(x=700, rely=mid)

buttonReset = tk.Button(window,
    background=light_Blue,
    foreground=black,
    activebackground=navy,
    activeforeground=blue_Blush,
    highlightthickness=2,
    highlightcolor='WHITE',
    command=Reset,
    width=button_width,
    height=button_height,
    text="Reset",
    font=("Arial", 16, "bold"))

buttonReset.place(x=1000, rely=mid)

entry = tk.Entry(window,
    width=30,
    background=light_Blue,
    foreground=black,
    highlightthickness=2,
    highlightcolor='WHITE',
    font=("Arial", 14, "bold"))

entry.insert(0, "Insert Text Here")
entry.pack(fill=tk.X, side=tk.TOP)

status = tk.Label(window,
    background=light_Blue,
    foreground=black,
    activebackground=navy,
    activeforeground=blue_Blush,
    highlightthickness=2,
    highlightcolor='WHITE',
    width=10,
    height=2,
    text="Result: ",
    font=("Arial", 35, "bold"))

status.pack(fill=tk.X, side=tk.BOTTOM)

window.mainloop()
