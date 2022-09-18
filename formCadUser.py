from tkinter import *
from tkinter import ttk


class FormCadUser:
    def __init__(self, frame_CadForm):
        self.frame_CadUser = frame_CadForm
        self.frame_CadUser.title("Cadastro de Usuários")
        self.frame_CadUser.state("zoomed")


        ###instaciando os objetos
        self.frame_form = LabelFrame(self.frame_CadUser, text="Informações Usuário")
        self.frame_form.grid(row=2, column=1)

        self.nome = Label(self.frame_form, text="Primeiro Nome: ")
        self.nome.grid(row=3, column=1)

        self.sobreNome = Label(self.frame_form, text="Sobre Nome: ")
        self.sobreNome.grid(row=3, column=0)