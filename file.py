from Tkinter import Frame, Tk, BOTH, Text, Menu, END
import tkFileDialog 
import tkColorChooser 
import subprocess
import os
import sys
class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
        
    def initUI(self):
      
        self.parent.title("File auswaehlen")
        self.pack(fill=BOTH, expand=1)
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="open file", command=self.onOpen)
        menubar.add_cascade(label="click here to start", menu=fileMenu)        
        self.pack(fill=BOTH, expand=1)

        self.txt = Text(self)
        #self.txt.pack(fill=BOTH, expand=1)
        self.txt.pack()

    def onOpen(self):
      
        ftypes = [('Python files', '*.py'), ('Shell Scripts', '*.sh'),('Text Files','*.txt')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show()
        
        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)
            

    def readFile(self, filename):
        subprocess.call(["nano" , filename])
        #f = open(filename, "r")
        #text = f.read()
        #return text
        sys.exit(0)
         

def main():
  
    root = Tk()
    ex = Example(root)
    root.geometry("600x350+10+10")
    root.mainloop()  


if __name__ == '__main__':
    main()  
