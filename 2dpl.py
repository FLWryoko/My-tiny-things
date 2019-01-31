from pathlib import Path
from array import array
import csv
import matplotlib.pyplot as pyplot
import numpy as np
from tkinter import Toplevel, filedialog, Tk

from tkinter.ttk import Frame, Button

fname = None
file = None
dreader = None
def fselect():
   idir,ifile = './'
   pathname = filedialog.askopenfilename(filetypes=[('CSV files','*.csv'),('All files','*'),],
           initialdir=idir,initialfile=ifile)
          
   global file,dreader,fname
   print('Selected File: '+pathname)
   fname = Path(pathname)
   print(fname)
   file = Path.open(fname)
   dreader = csv.DictReader(file)

def run():
 
  x =array('f')
  y =array('f')
  for row in dreader:
     try:
       str(row['x'])
       str(row['y'])
     except KeyError:
       print('Error:Labels needs "x,y" .')
     print(dreader.line_num)
     print('row:x  '+row['x'])
     print('row:y  '+row['y'])
     x.append(float(row['x']))
     y.append(float(row['y']))
  fig,ax = pyplot.subplots()
  ax.plot(x,y)
  pyplot.show()




class MenuFrame(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.pack()
        self.parent.geometry("+%d+%d" % (self.parent.winfo_rootx()+600,self.parent.winfo_rooty()+400))
        self.file = Button(self)
        self.file["text"] = "File"
        self.file["command"] = fselect
        self.file.pack(side="top")

        self.run = Button(self)
        self.run["text"] = "Run"
        self.run["command"] = run
        self.run.pack(side="top")
root = Tk()
app = MenuFrame(parent = root)
app.mainloop()
