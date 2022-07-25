#pip install gTTS
#pip install ttkthemes
#pip install PyPDF2


from tkinter import *
from tkinter.filedialog import askopenfilename
import ttkthemes
from tkinter import messagebox
from tkinter import ttk
from gtts import gTTS
import datetime
import PyPDF2
import threading



window = ttkthemes.ThemedTk()
window.get_themes()
window.set_theme('elegance')
window.title('Pdf to Audiobook Converter')
window.geometry("374x230")
window.config(bg="#6666ff")
window.iconbitmap(r'logo.ico')
window.resizable(0,0)

img = PhotoImage(file="logo image.png")
lab = Label(window, image=img, bg="#6666ff",
            compound=LEFT, highlightthickness=0)
lab.grid(row=0, column=0)

message_str = StringVar()
entrybox = Entry(window, borderwidth=6,
                 textvariable=message_str, font=5, width=27)
entrybox.grid(row=1, column=0)
entrybox.place(x=5, y=150)


def Openfile():
    name = askopenfilename(initialdir="Downloads",
                           filetypes=(("Pdf file", "*.pdf"),
                                      ("ALL Files", ".*")),
                           title="Choose a file"
                           )

    entrybox.insert(END, name)


file = ttk.Button(window, text="Choose PDF File", command=Openfile)
file.grid(row=1, column=0)
file.place(x=270, y=150)

text_data = ""


def play_audio():
    global text_data
    play.config(state=DISABLED)
    file.config(state=DISABLED)

    try:
        pdfile = entrybox.get()
        book = open(pdfile, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(book)
        # num_pages = pdf_reader.numPages

        # for num in range(0, num_pages): #for all pages.
        for num in range(0, 10):#for only first 10 pages.
            page = pdf_reader.getPage(num)
            data = page.extractText()
            text_data += data

        final_file = gTTS(text=text_data, lang='en')
        filename = "Audiobook-" + str(datetime.datetime.now().date())
        final_file.save(filename + ".mp3")
        messagebox.showinfo("Success", "Audiobook Created")
    except:
        messagebox.showerror("No Pdf File", "Please insert Pdf")
        play.config(state=NORMAL)
        file.config(state=NORMAL)

def startThredProcess():
    myNewThread = threading.Thread(target=play_audio)
    myNewThread.start()


play = ttk.Button(window, text="Create Audiobook",
                    width=30, command=startThredProcess)
play.grid(row=4, column=0)
play.place(x=80, y=190)


window.mainloop()