from tkinter import *
from tkinter import messagebox
from datetime import *

from PIL import Image, ImageTk

class ApplicationX:

    def __init__(self, app):

        app = app
        ### FRAME LOGIN ###
        app.title("Login - OxR")
        app.configure(bg="#D0E6F1")


        self.logo = PhotoImage(file='logo_naz.gif')
        self.lb_logo = Label(app, image=self.logo, height=650, width=500)
        self.lb_logo.place(x=50, y=2)

        
        self.frame_down = Frame(app, height=90, width=900, bg="#0C4AB1")
        self.frame_down.place(relx=0, rely=0, y=620)

        self.copy = Label(self.frame_down, text="Development by: Jaderson Sousa & João Paulo - 2022", bg="#0C4AB1", foreground="#fff")
        self.copy.place(relx=0, rely=0)
        

        #FRAME DO FORMULARIO DE LOGIN
        self.frame_login = Frame(app, width=800, height=900, bg="#fff")

        self.heading = Label(self.frame_login, text='Entrar no sistema', bg='#57a1f8', font=('Microsoft YeHei UI Light', 23, 'bold'))
        self.heading.place(x=100, y=76)

        self.logoOxr = PhotoImage(file='logoOxr.gif')
        self.lb_logoOxr = Label(self.frame_login, image=self.logoOxr, height=65, width=150)
        self.lb_logoOxr.place(x=150, y=2)


        #    .
        #    .
        #    .
        #    .
        #    .
        #    .
        #    .
        #    .
        #    .
        #    .
        # depois termino ou tu pode terminar tambem kk

        self.frame_login.place(x=900)




            
if __name__ == '__main__':
    app = Tk()

    app.state("zoomed")
    application = ApplicationX(app)
  

    app.mainloop()
