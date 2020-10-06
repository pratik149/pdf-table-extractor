from pdf2image import convert_from_bytes
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from tkinter import *
import sys

input_file = (r"Citibank.pdf")
#input_file = (r"Morgan Stanley.pdf")
#input_file = (r"UBS Global.pdf")

e1=''
def show_entry_fields():
    global pagen
    inp = PdfFileReader(input_file, True)
    pagen = 0

    pagen = e1.get()
    pagen = int(pagen)

    page = inp.getPage(pagen)
    wrt = PdfFileWriter()
    wrt.addPage(page)
    r = io.BytesIO()
    wrt.write(r)

    images = convert_from_bytes(r.getvalue())
    images[0].save(input_file[:-4] + ".png")
    Label(text="\x1b The pdf has been converted into png and saved as.. {}.\x1b".format(input_file[:-4] + ".png")).place( x=20,y=150)
    r.close()


def pdf2png_gui():

    self = Tk()
    Label(self, text="Enter Page no. where table is located",font=('Cambria Math', 20, 'bold')).grid(row=0)
    e1 = Entry(self)
    e1.grid(column=2,row=0)


    Button(self, text='Enter',width=15,font=("Cambria",20),command=show_entry_fields).place(x=20,y=200)

    self.geometry("650x500")

    mainloop()






#********************************************
