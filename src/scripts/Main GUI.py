import tkinter as tk
import webbrowser
import tkfilebrowser
from tkinter import Entry
from PIL import Image, ImageTk
from win32com.client import Dispatch
from DecisionBlock import make_decision_scanned_searchable

class View(tk.Frame):
    rep = ''

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        def browse():
            View.rep = tkfilebrowser.askopenfilenames(parent=self, initialdir='/', initialfile='tmp',
                                                 filetypes=[("PDF", "*.pdf"), ["Pictures", "*.png|*.jpg|*.JPG"]])
            print(View.rep)
            label.configure(text=View.rep)

        def open_app():
            xl = Dispatch("Excel.Application")
            xl.Visible = True  # otherwise excel is hidden
            wb = xl.Workbooks.Open(r'C:\Users\TAYYABA\Desktop\March 2018 Target.xlsx')

        def Pdf_app():
            webbrowser.open_new(r'C:\SIH\css.pdf')

        def make_my_decision():
            print(View.rep, 'VIEW')
            make_decision_scanned_searchable(View.rep[0])






        img = Image.open('background.png')
        self.tkimage = ImageTk.PhotoImage(img)
        myvar = tk.Label(self, image=self.tkimage)
        myvar.pack()
        myvar.place(x=0, y=0)

        logo = tk.Label(self, text='Smart India PDF', font=("Algerian", 40, "bold"), bg="white").pack(pady=5)

        logo1 = tk.Label(self, text='Upload image or PDF file (.png or .jpg or.pdf)', bg="white",
                         font=("Lucida Fax", 12, "bold"))
        label = tk.Label(self, text='', relief='groove',font=('Lucida Fax', 12, 'bold'),bg="white")

        qut = Image.open('1-logo-agr.png')
        self.tkiqut = ImageTk.PhotoImage(qut)
        myqut=tk.Label(self,image = self.tkiqut)
        myqut.pack()


        back = tk.Button(self, text="Upload File", font=('Lucida Fax', 12, 'bold'), bg="white", command=browse)

        logo2 = tk.Label(self, text='Click the icon to convert file into  xsl',bg="white",
                         font=("Lucida Fax", 12, "bold"))

        logo1.pack()
        logo1.place(x=200, y=200)
        back.pack()
        back.place(x=600, y=200)

        label.place(x=600, y=240)
        logo2.pack()
        logo2.place(x=200, y=350)

        b = tk.Button(self, text="Start Extracting PDF", bg='white', font=('Lucida Fax', 12, 'bold'),command=make_my_decision,
                       compound="bottom")
        b.pack(side="top")
        b.place(x=600, y=350)


        D1 = tk.Button(self, text="View File with overlay", font=('Lucida Fax', 12, 'bold'), command=Pdf_app,bg="white")
        D1.pack()
        D1.place(x=300, y=490)

        D2 = tk.Button(self, text="Result", font=('Lucida Fax', 12, 'bold'),bg="white",command=open_app)
        D2.pack()
        D2.place(x=600, y=490)





if __name__ == "__main__":
    self = tk.Tk()
    view = View(self)
    self.geometry("900x900")

    #   self.resizable(0,0)
    view.pack(side="top", fill="both", expand=True)
    self.mainloop()
