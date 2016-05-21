#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://zetcode.com/gui/tkinter/dialogs/

from ttk import Frame, Button, Style
from Tkinter import Tk, BOTH
import tkMessageBox as box
from Tkinter import *
import subprocess
import tkFont
import sys
import netifaces as ni
#######################
## font=("Times", "24", "bold italic") 
## ("Helvetica", "16")
######################
#master = Tk()

class Example(Frame):
     
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def initUI(self):

        self.parent.title("MenueBildschirm")
        self.style = Style()
        self.style.theme_use("default")
        #self.pack(fill=BOTH, expand=1)
        self.pack()

############### buttons on main    
        error = Button(self, text="Foto aufnehmen" ,bg = "white",fg="blue",relief=SUNKEN,font=("Helvetica", "12"),width='20', command=self.onError) 
        error.grid(row=1, column=0)
        
        warning = Button(self, text="Video aufnehmen", bg = "white",fg="blue",relief=SUNKEN,font=("Helvetica", "12"),width='20',command=self.onWarn)
        warning.grid(row=2, column=0)
        
        question = Button(self, text="Lichtschalter", bg = "white",fg="blue",relief=SUNKEN,font=("Helvetica", "12"),width='20',command=self.onQuest)
        question.grid(row=3, column=0)
        
        inform = Button(self, text="Navit starten" ,bg = "white",fg="blue",relief=SUNKEN,font=("Helvetica", "12"), width='20',command=self.onInfo)
        inform.grid(row=4, column=0)
        
        rechner = Button(self, text="Taschenrechner", bg = "white",fg="blue",relief=SUNKEN,font=("Helvetica", "12"), width='20',command=self.rechner)
        rechner.grid(row=5, column=0)
        
        showIP = Button(self, text="IP-Adresse anzeigen", bg = "white",fg="blue",relief=SUNKEN,font=("Helvetica", "12"), width='20',command=self.onshowIP)
        showIP.grid(row=6, column=0)
        
        editor = Button(self, text="Nano-Editor", bg = "white",fg="blue",relief=SUNKEN,font=("Helvetica", "12"), width='20',command=self.oneditor)
        editor.grid(row=7, column=0)
        
        ende = Button(self, text="Verlassen", bg = "white",fg="red",relief=SUNKEN,font=("Helvetica", "12"), width='20',command=quit)
        ende.grid(row=8, column=0)
        
###################### functions for main buttons

    def oneditor(self):
       output = subprocess.Popen("./menue.sh N",shell=True)  

    def onshowIP(self):
       ni.ifaddresses('wlan0')
       ip = ni.ifaddresses('wlan0')[2][0]['addr']
       #box.showonshowIP("ip")
       box.showwarning("IP-Adresse",ip)
    def onError(self):
       output = subprocess.Popen("./menue.sh F",shell=True)  

    def rechner(self):
       output=subprocess.Popen("./menue.sh R", shell = True)

    def onInfo(self):
         output = subprocess.Popen("./menue.sh E",shell=True)  
    def quit():
         sys.exit(1)
    
        
    def onWarn(self):
       # box.showwarning("Warning", "Deprecated function call")
        output = subprocess.Popen("./menue.sh V",shell=True)  

#############     second window
###############  functions on second window
    def onQuest(self):
        global buttonVX
        def onbuttonOk():
	    output = subprocess.Popen("./menue.sh A",shell=True) 
            tkFensterFehler.destroy()    
        def onbuttonXk():
            output = subprocess.Popen("./menue.sh B",shell=True)  
            tkFensterFehler.destroy()    
        def onbuttonVX():
	    output = subprocess.Popen("./menue.sh C",shell=True)  
            tkFensterFehler.destroy()    
        def onbuttonWX():
            output = subprocess.Popen("./menue.sh D",shell=True)  
            tkFensterFehler.destroy()    
            
######### open sencond window                     

        tkFensterFehler = Toplevel()
        tkFensterFehler.title('Lichtschalter')
        tkFensterFehler.geometry('300x100+200+300')
        
        
################ button second window

        buttonOk = Button(master=tkFensterFehler, text='Lichtschalter 1 an', command=onbuttonOk)
	buttonOk.grid(row=0, column=0)

        buttonXk = Button(master=tkFensterFehler, text='Lichtschalter 1 aus', command=onbuttonXk)
	buttonXk.grid(row=1, column=0)
	
	buttonXk1 = Button(master=tkFensterFehler, text='Lichtschalter 2 an', command=onbuttonVX)
	buttonXk1.grid(row=0, column=1)
	
	buttonXk2 = Button(master=tkFensterFehler, text='Lichtschalter 2 aus', command=onbuttonWX)
	buttonXk2.grid(row=1, column=1)

def main():	
    root = Tk()
    ex = Example(root)
    root.geometry("700x500+0+0")
    root.mainloop()

if __name__ == '__main__':
    main()
