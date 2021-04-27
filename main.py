from tkinter import *
from train import chat
import time
import pyttsx3
import threading
import tkinter.messagebox


window_size="1200x600"

class ChatInterface(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # sets default bg for top level windows
        self.tl_bg = "#EEEEEE"
        self.tl_bg2 = "#EEEEEE"
        self.tl_fg = "red"
        self.font = "Fixedsys 10"

        self.text_frame = Frame(self.master, bd=5)
        self.text_frame.pack(expand=True, fill=BOTH)

        # scrollbar for text box
        self.text_box_scrollbar = Scrollbar(self.text_frame, bd=0)
        self.text_box_scrollbar.pack(fill=Y, side=RIGHT)

        # contains messages
        self.text_box = Text(self.text_frame, yscrollcommand=self.text_box_scrollbar.set, state=DISABLED,
                             bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg=None, font="Fixedsys 5", relief=SUNKEN,
                             width=5, height=1)
        self.text_box.pack(expand=True, fill=BOTH)
        self.text_box_scrollbar.config(command=self.text_box.yview)

        # frame containing user entry field
        self.entry_frame = Frame(self.master, bd=3)
        self.entry_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # entry field
        self.entry_field = Entry(self.entry_frame, bd=1, justify=RIGHT)
        self.entry_field.pack(fill=X, padx=6, pady=6, ipady=3)

        self.send_button_frame = Frame(self.master, bd=0)
        self.send_button_frame.pack(fill=BOTH)

        # send button
        self.send_button = Button(self.send_button_frame, text="Send", width=10, height=1, relief=RAISED, bg='#519872',
                                  bd=3, command=lambda: self.send_message_insert(None), activebackground="white",
                                  activeforeground="#000000")
        self.send_button.pack(side=LEFT, ipady=8)
        self.master.bind("<Return>", self.send_message_insert)

    def playResponse(self,responce):
        x=pyttsx3.init()
        li = []
        if len(responce) > 100:
            if responce.find('--') == -1:
                b = responce.split('--')
        x.setProperty('rate',120)
        x.setProperty('volume',100)
        x.say(responce)
        x.runAndWait()

    def send_message_insert(self, message):
        user_input = self.entry_field.get()
        pr1 = "User : " + user_input + "\n"
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr1)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)
        ob=chat(user_input)
        pr="Jr. Java : " + ob + "\n"
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)
        self.entry_field.delete(0,END)
        time.sleep(0)
        t2 = threading.Thread(target=self.playResponse, args=(ob,))
        t2.start()

    def font_change_default(self):
        self.text_box.config(font="fixedsys")
        self.entry_field.config(font="fixedsys")
        self.font = "fixedsys"

    def color_theme_default(self):
        self.master.config(bg="#263b54")
        self.text_frame.config(bg="#263b54")
        self.text_box.config(bg="#1c2e44", fg="#FFFFFF")
        self.entry_frame.config(bg="#263b54")
        self.entry_field.config(bg="#1c2e44", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.send_button_frame.config(bg="#263b54")
        self.send_button.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#263b54", fg="#FFFFFF")

        self.tl_bg = "#1c2e44"
        self.tl_bg2 = "#263b54"
        self.tl_fg = "#FFFFFF"

    def default_format(self):
        self.font_change_default()
        self.color_theme_default()
root=Tk()

a = ChatInterface(root)
root.geometry(window_size)
root.title("Jr. Java")
root.mainloop()
