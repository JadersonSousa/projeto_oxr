from tkinter import *
from tkinter import ttk


class FormCadUser:
    def __init__(self, frame_CadForm):
        self.frame_CadUser = frame_CadForm
        self.frame_CadUser.title("Cadastro de Usuários")
        self.frame_CadUser.state("zoomed")


<<<<<<< HEAD
        ###instaciando os objetos
        self.frame_form = LabelFrame(self.frame_CadUser, text="Informações Usuário")
=======

        self.frame_form = LabelFrame(self.frame_CadUser, text="Informações do Usuário")
>>>>>>> bb5438498d1209f7b6d623b4fd25771b4f56579d
        self.frame_form.grid(row=2, column=1)

        self.nome = Label(self.frame_form, text="Primeiro Nome: ")
        self.nome.grid(row=3, column=1)

        self.sobreNome = Label(self.frame_form, text="Sobrenome: ")
        self.sobreNome.grid(row=3, column=0)