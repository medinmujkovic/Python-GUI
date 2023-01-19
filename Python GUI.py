import tkinter
from tkinter import *
from tkcalendar import Calendar
from tkinter.messagebox import showerror

window = tkinter.Tk() #rootwindow, bazni prozor za sve ostalo, baza za sve ostale widgete
window.title("Sign Up")
window.geometry("250x300")

def enter_data():
    ime=ime_entry.get()
    prezime=prezime_entry.get()

    if ime=="" or prezime=="": 
        tkinter.messagebox.showwarning(title="Pogrešno uneseni podaci ",message="Unesi ponovo ime i prezime")
        tkobj.destroy()
        
    tkobj = Tk() # setting up the geomentry
    tkobj.geometry("400x400")
    tkobj.title("Rođendan")
    tkc = Calendar(tkobj,selectmode = "day",year=2022,month=1,date=1)
    tkc.pack(pady=10)
    
    def fetch_date():
        date.config(text = "Izabrani datum je: " + tkc.get_date()) 
        
    but = Button(tkobj,text="Izaberi datum",command=fetch_date, bg="black", fg='white')
    but.pack()
    date = Label(tkobj,text="",bg='black',fg='white')
    date.pack(pady=20)    

    frame1=tkinter.Frame(tkobj)
    frame1.pack()
    def kraj():
        date=tkc.get_date()
        if  date=="": 
            tkinter.messagebox.showwarning(title="Nije unesen datum rođenja",message="Molimo vas unesite datum rođenja")
        else : tkobj.destroy()
    button1=tkinter.Button(frame1,text="Submit",command=kraj)
    button1.grid(row=0,column=0,sticky="news",padx=20,pady=10) 

    window.destroy()
    tkobj.mainloop()
    
    print("\nIme: ",ime,"Prezime: ",prezime)
    
    remember=rememberstatus.get()
    print("Remember me:",remember)
    print("Izabrani datum je: " + tkc.get_date())
    
    print("\n")


frame=tkinter.Frame(window) #pravljenje frejma unutar prozora
frame.pack() #pozicioniranje

user_info_fr=tkinter.LabelFrame(frame,text="User Info:")
user_info_fr.grid(row=0,column=0,padx=20,pady=20)

ime_label=tkinter.Label(user_info_fr,text="Ime")
ime_label.grid(row=1,column=0)
prezime_label=tkinter.Label(user_info_fr,text="Prezime")
prezime_label.grid(row=3,column=0)

ime_entry=tkinter.Entry(user_info_fr)
prezime_entry=tkinter.Entry(user_info_fr)
ime_entry.grid(row=2,column=0,pady=10)
prezime_entry.grid(row=4,column=0,pady=10)

rememberstatus=tkinter.StringVar(value="Ovaj profil nije zapamcen na serveru")
rememberme_check=tkinter.Checkbutton(user_info_fr,text="Remember me",variable=rememberstatus,onvalue="Ovaj profil je zapamcen na serveru" , offvalue="Ovaj profil nije zapamcen na serveru.")
rememberme_check.grid(row=5,column=0)

button=tkinter.Button(frame,text="Sign up",command=enter_data)
button.grid(row=5,column=0,sticky="news",padx=20,pady=10)

window.mainloop() #run until exited
