from tkinter import *
from tkinter import messagebox
from home import *
from PIL import Image, ImageTk



class Application:

    def __init__(self, app):

        app = app
        ### FRAME LOGIN ###
        app.title("Login - OxR")
        app.configure(bg="#333")

        #frameLogin
        frame_login = Frame(app, bg="#333")
    
        #widgets
        
        my_label = Label(frame_login,image=my_img, bg="#333")
        lb_login = Label(frame_login, text="Sistema OxR", fg="#0373fc", bg="#333", font=('Segoe UI Light', 22)) 
        e_user = Entry(frame_login, font=("Arial", 13), width=25)
        lb_user = Label(frame_login, text="Usuário: ", fg="#fff", bg="#333", font=('Arial', 10, 'bold')) 
        e_password = Entry(frame_login, font=("Arial", 13), show="*", width=25)
        lb_password = Label(frame_login, text="Senha: ", fg="#fff", bg="#333", font=('Arial', 10, 'bold'))
        btn_login = Button(frame_login, text="Entrar", bg="#0373fc", fg="#fff", font=('Arial', 10, 'bold'), bd=0, width=22, command=self.login_user)
        

        #configs inputs
        my_label.grid(row=0, column=0, columnspan=2, pady=10)
        lb_login.grid(row=1, column=0, columnspan=2, sticky="news", pady=10)
        lb_user.grid(row=2, column=0)
        e_user.grid(row=2, column=1, pady=14)
        lb_password.grid(row=3, column=0)
        e_password.grid(row=3, column=1)
        btn_login.grid(row=4, column=0,  padx=(50,0), pady=(20, 0), columnspan=6)
     
        frame_login.pack()


        global user
        global password

        user = e_user
        password = e_password

    def login_user(self):

         if len(user.get()) == 0 or len(password.get()) == 0:
            messagebox.showerror('Erro Verifique', 'Preencha os campos!')       
            if user.get() != 'admin' or password.get() != 'admin':
                messagebox.showwarning('Atenção', 'Credenciais invalidas')

         if user.get() == 'admin' and password.get() == 'admin':
            
             app.destroy()

             newroot = Tk()
             application = Home(newroot)
             newroot.mainloop()


if __name__ == '__main__':
    app = Tk()
    my_img = ImageTk.PhotoImage(Image.open("img\OxR-1.png"), size="50x50")
    app.state("zoomed")
    application = Application(app)
  

    app.mainloop()
