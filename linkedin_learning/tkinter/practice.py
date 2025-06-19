from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self,master):

        self.label = ttk.Label(master, text = "Hello, Tkinter!")
        self.label.grid(row= 0, column=0, columnspan=3)

        self.malayalam_button = ttk.Button(master, text='Malayalam', command=self.malayalam_hello)
        self.malayalam_button.grid(row=1, column=0)

        self.hindi_button = ttk.Button(master, text='Hindi', command=self.hindi_hello)
        self.hindi_button.grid(row=1, column=1)

    def malayalam_hello(self):
        self.label.config(text= "Swagatham, Tkinter!")
        self.malayalam_button.config(underline=1)

    def hindi_hello(self):
        self.label.config(text= "Namaste, Tkinter!")
        self.hindi_button.config(underline=1)

def main():
    root = Tk()
    HelloApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()