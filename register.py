import tkinter
from tkinter import *
from tkinter import ttk

class Register:
    def __init__(self, frame_cadastros):
        self.frame_cadastros = frame_cadastros
        
        self.tab_register = ttk.Notebook(frame_cadastros)
        self.tab_register.pack(pady=2.9, padx=2.9)

        self.frame_sec_CadUser = Frame(self.tab_register, bg="#fff", height=1100, width=1400, bd=0)
        self.frame_sec_CadEmp = Frame(self.tab_register, bg="#fff", height=1100, width=1400)
        self.frame_sec_CadFil = Frame(self.tab_register, bg="#fff", height=1100, width=1400)
        self.frame_sec_CadCnc = Frame(self.tab_register, bg="#fff", height=1100, width=1400)
        self.frame_sec_CadCC = Frame(self.tab_register, bg="#fff", height=1100, width=1400)

        self.frame_sec_CadUser.place(relx=0.70)
        self.frame_sec_CadEmp.place(relx=0.70)
        self.frame_sec_CadFil.place(relx=0.70)
        self.frame_sec_CadCnc.place(relx=0.70)
        self.frame_sec_CadCC.place(relx=0.70)


        self.tab_register.add(self.frame_sec_CadUser, text="Usuário")
        self.tab_register.add(self.frame_sec_CadEmp, text="Empresa")
        self.tab_register.add(self.frame_sec_CadFil, text="Filial")
        self.tab_register.add(self.frame_sec_CadCnc, text="Centro de Custos")
        self.tab_register.add(self.frame_sec_CadCC, text="Contas Contábeis")
     
