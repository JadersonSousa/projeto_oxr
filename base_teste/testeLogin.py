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


        self.logo = PhotoImage(file='C:\\Users\positivo\Desktop\projeto_oxr\img\logo_naz.png')
        self.lb_logo = Label(app, image=self.logo, height=650, width=500)
        self.lb_logo.place(x=50, y=2)

        
        self.frame_down = Frame(app, height=50, width=900, bg="#0a66c2")
        self.frame_down.place(relx=0, rely=0, y=670)


        self.copy = Label(self.frame_down, text="Development by: Jaderson Sousa & João Paulo - 2022", bg="#0a66c2", foreground="#fff")
        self.copy.place(relx=0, rely=0)
        

        #FRAME DO FORMULARIO DE LOGIN
        self.frame_login = Frame(app, width=800, height=900, bg="#f7f9fc")

        self.heading = Label(self.frame_login, text='Entrar no sistema', foreground="#0a66c2",  bg='#f7f9fc', font=('Segoe UI Light', 23, 'bold'))
        self.heading.place(x=100, y=76)

        self.logoOxr = PhotoImage(file='C:\\Users\positivo\Desktop\projeto_oxr\img\logo_oxr.png')
        self.lb_logoOxr = Label(self.frame_login, image=self.logoOxr, height=65, width=150, bg="#f7f9fc")
        self.lb_logoOxr.place(x=150, y=2)

        #####################--------------------entry do usuário--------------------#####################
        self.lb_usuario = Label(self.frame_login, text="Usuário", width=6, bg="#0a66c2", foreground="#fff").place(x=10, y=170)     
        self.e_usuario = Entry(self.frame_login, width=36, fg='black', border=0, bg='#f7f9fc', font=('Microsoft YeHei UI Light', 11))
        self.e_usuario.place(x=59, y=169)
        self.border_usuario = Frame(self.frame_login, width=295, height=1, bg='#0a66c2').place(x=50, y=190)

        #####################--------------------entry da senha--------------------#####################
        self.lb_senha = Label(self.frame_login, text="Senha", width=6, bg="#0a66c2", foreground="#fff").place(x=10, y=250)  
        self.e_senha = Entry(self.frame_login, width=36, fg='black', border=0, bg='#f7f9fc', font=('Microsoft YeHei UI Light', 11), show="*")
        self.e_senha.place(x=59, y=250)
        self.border_senha = Frame(self.frame_login, width=295, height=1, bg='#0a66c2').place(x=50, y=270)

        #####################--------------------Botão de entrar--------------------#####################
        self.btn_login = Button(self.frame_login, width=42, pady=7, text="Entrar", bg='#0a66c2', fg='#f7f9fc', border=0, cursor='hand2').place(x=50, y=290)


        self.frame_login.place(x=900)




            
if __name__ == '__main__':
    app = Tk()

    app.state("zoomed")
    application = ApplicationX(app)
  

    app.mainloop()
