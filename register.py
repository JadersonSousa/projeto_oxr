import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.tix import ButtonBox


bg_register = '#0d151a'

class Register:
    def __init__(self, frame_cadastros):
        self.frame_cadastros = frame_cadastros
        
        self.tab_register = ttk.Notebook(frame_cadastros)
        self.tab_register.pack()


        #FRAMES#
        self.frame_sec_CadUser = Frame(self.tab_register, bg=bg_register, height=1100, width=1400)
        self.frame_sec_CadEmp = Frame(self.tab_register, bg=bg_register, height=1100, width=1400)
        self.frame_sec_CadFil = Frame(self.tab_register, bg=bg_register, height=1100, width=1400)
        self.frame_sec_CadReg = Frame(self.tab_register, bg=bg_register,height=1100, width=1400)
        self.frame_sec_CadCdc = Frame(self.tab_register, bg=bg_register, height=1100, width=1400)
        self.frame_sec_CadCC = Frame(self.tab_register, bg=bg_register, height=1100, width=1400)

        self.frame_CadUser = Frame(self.frame_sec_CadUser)
        self.frame_CadEmp = Frame(self.frame_sec_CadEmp)
        self.frame_CadFil = Frame(self.frame_sec_CadFil)
        self.frame_CadReg = Frame(self.frame_sec_CadReg)
        self.frame_CadCdc = Frame(self.frame_sec_CadCdc)
        self.frame_CadCC = Frame(self.frame_sec_CadCC)

        self.frame_CadUser.place(relx=0.005, rely=0.01, relwidth=0.905, relheight=0.98)
        self.frame_CadEmp.place(relx=0.005, rely=0.01, relwidth=0.905, relheight=0.98)
        self.frame_CadFil.place(relx=0.005, rely=0.01, relwidth=0.905, relheight=0.98)
        self.frame_CadReg.place(relx=0.005, rely= 0.01, relwidth=0.905, relheight=0.98)
        self.frame_CadCdc.place(relx=0.005, rely=0.01, relwidth=0.905, relheight=0.98)
        self.frame_CadCC.place(relx=0.005, rely=0.01, relwidth=0.905, relheight=0.98)

        self.frame_CadUser.configure(background='snow')
        self.frame_CadEmp.configure(background='snow')
        self.frame_CadFil.configure(background='snow')
        self.frame_CadReg.configure(background='snow')
        self.frame_CadCdc.configure(background='snow')
        self.frame_CadCC.configure(background='snow')

        # BOTÕES #
        # Botões Usuários #
        self.bt_CadUser_Novo = Button(self.frame_sec_CadUser, text="Novo", bd=2, bg='snow', fg='black')
        self.bt_CadUser_Novo.place(relx=0.915, rely=0.01, relwidth=0.08, relheight=0.04)               
        self.bt_CadUser_Editar = Button(self.frame_sec_CadUser, text="Editar", bd=2, bg='snow', fg='black')
        self.bt_CadUser_Editar.place(relx=0.915, rely=0.05, relwidth=0.08, relheight=0.04)
        self.bt_CadUser_Salvar = Button(self.frame_sec_CadUser, text="Salvar", bd=2, bg='snow', fg='black')
        self.bt_CadUser_Salvar.place(relx=0.915, rely=0.09, relwidth=0.08, relheight=0.04)
        self.bt_CadUser_Excluir = Button(self.frame_sec_CadUser, text="Excluir", bd=2, bg='snow', fg='black')
        self.bt_CadUser_Excluir.place(relx=0.915, rely=0.13, relwidth=0.08, relheight=0.04)
        # Botões Empresa #
        self.bt_CadEmp_Novo = Button(self.frame_sec_CadEmp, text="Novo", bd=2, bg='snow', fg='black')
        self.bt_CadEmp_Novo.place(relx=0.915, rely=0.01, relwidth=0.08, relheight=0.04)               
        self.bt_CadEmp_Editar = Button(self.frame_sec_CadEmp, text="Editar", bd=2, bg='snow', fg='black')
        self.bt_CadEmp_Editar.place(relx=0.915, rely=0.05, relwidth=0.08, relheight=0.04)
        self.bt_CadEmp_Salvar = Button(self.frame_sec_CadEmp, text="Salvar", bd=2, bg='snow', fg='black')
        self.bt_CadEmp_Salvar.place(relx=0.915, rely=0.09, relwidth=0.08, relheight=0.04)
        self.bt_CadEmp_Excluir = Button(self.frame_sec_CadEmp, text="Excluir", bd=2, bg='snow', fg='black')
        self.bt_CadEmp_Excluir.place(relx=0.915, rely=0.13, relwidth=0.08, relheight=0.04)
        # Botões Filial #
        self.bt_CadFil_Novo = Button(self.frame_sec_CadFil, text="Novo", bd=2, bg='snow', fg='black')
        self.bt_CadFil_Novo.place(relx=0.915, rely=0.01, relwidth=0.08, relheight=0.04)               
        self.bt_CadFil_Editar = Button(self.frame_sec_CadFil, text="Editar", bd=2, bg='snow', fg='black')
        self.bt_CadFil_Editar.place(relx=0.915, rely=0.05, relwidth=0.08, relheight=0.04)
        self.bt_CadFIl_Salvar = Button(self.frame_sec_CadFil, text="Salvar", bd=2, bg='snow', fg='black')
        self.bt_CadFIl_Salvar.place(relx=0.915, rely=0.09, relwidth=0.08, relheight=0.04)
        self.bt_CadFIl_Excluir = Button(self.frame_sec_CadFil, text="Excluir", bd=2, bg='snow', fg='black')
        self.bt_CadFIl_Excluir.place(relx=0.915, rely=0.13, relwidth=0.08, relheight=0.04)
         # Botões Regional #
        self.bt_CadReg_Novo = Button(self.frame_sec_CadReg, text="Novo", bd=2, bg='snow', fg='black')
        self.bt_CadReg_Novo.place(relx=0.915, rely=0.01, relwidth=0.08, relheight=0.04)               
        self.bt_CadReg_Editar = Button(self.frame_sec_CadReg, text="Editar", bd=2, bg='snow', fg='black')
        self.bt_CadReg_Editar.place(relx=0.915, rely=0.05, relwidth=0.08, relheight=0.04)
        self.bt_CadReg_Salvar = Button(self.frame_sec_CadReg, text="Salvar", bd=2, bg='snow', fg='black')
        self.bt_CadReg_Salvar.place(relx=0.915, rely=0.09, relwidth=0.08, relheight=0.04)
        self.bt_CadReg_Excluir = Button(self.frame_sec_CadReg, text="Excluir", bd=2, bg='snow', fg='black')
        self.bt_CadReg_Excluir.place(relx=0.915, rely=0.13, relwidth=0.08, relheight=0.04)
        # Botões Centro de Custos #
        self.bt_CadCdc_Novo = Button(self.frame_sec_CadCdc, text="Novo", bd=2, bg='snow', fg='black')
        self.bt_CadCdc_Novo.place(relx=0.915, rely=0.01, relwidth=0.08, relheight=0.04)               
        self.bt_CadCdc_Editar = Button(self.frame_sec_CadCdc, text="Editar", bd=2, bg='snow', fg='black')
        self.bt_CadCdc_Editar.place(relx=0.915, rely=0.05, relwidth=0.08, relheight=0.04)
        self.bt_CadCdc_Salvar = Button(self.frame_sec_CadCdc, text="Salvar", bd=2, bg='snow', fg='black')
        self.bt_CadCdc_Salvar.place(relx=0.915, rely=0.09, relwidth=0.08, relheight=0.04)
        self.bt_CadCdc_Excluir = Button(self.frame_sec_CadCdc, text="Excluir", bd=2, bg='snow', fg='black')
        self.bt_CadCdc_Excluir.place(relx=0.915, rely=0.13, relwidth=0.08, relheight=0.04)
        # Botões Conta Contábil #
        self.bt_CadCC_Novo = Button(self.frame_sec_CadCC, text="Novo", bd=2, bg='snow', fg='black')
        self.bt_CadCC_Novo.place(relx=0.915, rely=0.01, relwidth=0.08, relheight=0.04)               
        self.bt_CadCC_Editar = Button(self.frame_sec_CadCC, text="Editar", bd=2, bg='snow', fg='black')
        self.bt_CadCC_Editar.place(relx=0.915, rely=0.05, relwidth=0.08, relheight=0.04)
        self.bt_CadCC_Salvar = Button(self.frame_sec_CadCC, text="Salvar", bd=2, bg='snow', fg='black')
        self.bt_CadCC_Salvar.place(relx=0.915, rely=0.09, relwidth=0.08, relheight=0.04)
        self.bt_CadCC_Excluir = Button(self.frame_sec_CadCC, text="Excluir", bd=2, bg='snow', fg='black')
        self.bt_CadCC_Excluir.place(relx=0.915, rely=0.13, relwidth=0.08, relheight=0.04)

        # DADOS #
        ## Dados Usuários ##
        self.dados_CadUser = ttk.Treeview(self.frame_CadUser, height=8, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))

        self.dados_CadUser.heading("#0", text="Usuário")
        self.dados_CadUser.heading("#1", text="Login")
        self.dados_CadUser.heading("#2", text="Senha")
        self.dados_CadUser.heading("#3", text="Nível de Acesso")
        self.dados_CadUser.heading("#4", text="Gerência")
        self.dados_CadUser.heading("#5", text="Empresa")
        self.dados_CadUser.heading("#6", text="Filial / Regional")

        self.dados_CadUser.column("#0", width=250)
        self.dados_CadUser.column("#1", width=200)
        self.dados_CadUser.column("#2", width=160)
        self.dados_CadUser.column("#3", width=100)
        self.dados_CadUser.column("#4", width=150)
        self.dados_CadUser.column("#5", width=200)
        self.dados_CadUser.column("#6", width=150)


        self.dados_CadUser.place(relx=0, rely=0, relwidth=0.985, relheight=1)

        self.scroll_dados_CadUser = Scrollbar(self.frame_CadUser, orient='vertical')
        self.dados_CadUser.configure(xscrollcommand=self.scroll_dados_CadUser.set)
        self.scroll_dados_CadUser.place(relx=0.985, rely=0, relwidth=0.015, relheight=1)
        self.scroll_dados_CadUser = Scrollbar(self.frame_CadUser, orient='horizontal')
        self.dados_CadUser.configure(yscrollcommand=self.scroll_dados_CadUser.set)
        self.scroll_dados_CadUser.place(relx=0, rely=0.97, relwidth=0.985, relheight=0.03)        

        ## Dados Empresa ##
        self.dado_CadEmp = ttk.Treeview(self.frame_CadEmp, height=3, columns=("col1", "col2", "col3"))

        self.dado_CadEmp.heading("#0", text="Emp")
        self.dado_CadEmp.heading("#1", text="Empresa")
        self.dado_CadEmp.heading("#2", text="Apelido")

        self.dado_CadEmp.column("#0", width=50)
        self.dado_CadEmp.column("#1", width=300)
        self.dado_CadEmp.column("#2", width=50)
        self.dado_CadEmp.column("#3", width=810)

        self.dado_CadEmp.place(relx=0, rely=0, relwidth=0.985, relheight=1)

        self.scroll_dados_CadEmp = Scrollbar(self.frame_CadEmp, orient='vertical')
        self.dado_CadEmp.configure(xscrollcommand=self.scroll_dados_CadEmp.set)
        self.scroll_dados_CadEmp.place(relx=0.985, rely=0, relwidth=0.015, relheight=1)

        ## Dados Regional ##
        self.dado_CadReg = ttk.Treeview(self.frame_CadReg, height=2, columns=("col1", "col2"))

        self.dado_CadReg.heading("#0", text="UF")
        self.dado_CadReg.heading("#1", text="Regional")

        self.dado_CadReg.column("#0", width=50)
        self.dado_CadReg.column("#1", width=300)
        self.dado_CadReg.column("#2", width=860)

        self.dado_CadReg.place(relx=0, rely=0, relwidth=0.985, relheight=1)

        self.scroll_dados_CadReg = Scrollbar(self.frame_CadFil, orient='vertical')
        self.dado_CadReg.configure(xscrollcommand=self.scroll_dados_CadReg.set)
        self.scroll_dados_CadReg.place(relx=0.985, rely=0, relwidth=0.015, relheight=1)

        ## Dados Filial ##
        self.dado_CadFil = ttk.Treeview(self.frame_CadFil, height=5, columns=("col1", "col2", "col3","col4", "col5"))

        self.dado_CadFil.heading("#0", text="FL")
        self.dado_CadFil.heading("#1", text="Filial")
        self.dado_CadFil.heading("#2", text="Empresa")
        self.dado_CadFil.heading("#3", text="Regional")
        self.dado_CadFil.heading("#4", text="Gerência")

        self.dado_CadFil.column("#0", width=50)
        self.dado_CadFil.column("#1", width=300)
        self.dado_CadFil.column("#2", width=300)
        self.dado_CadFil.column("#3", width=200)
        self.dado_CadFil.column("#4", width=150)
        self.dado_CadFil.column("#5", width=210)

        self.dado_CadFil.place(relx=0, rely=0, relwidth=0.985, relheight=1)

        self.scroll_dados_CadFil = Scrollbar(self.frame_CadFil, orient='vertical')
        self.dado_CadFil.configure(xscrollcommand=self.scroll_dados_CadFil.set)
        self.scroll_dados_CadFil.place(relx=0.985, rely=0, relwidth=0.015, relheight=1)

        ## Dados Centro de Custos ##
        self.dado_CadCdc = ttk.Treeview(self.frame_CadCdc, height=4, columns=("col1", "col2", "col3", "col4"))

        self.dado_CadCdc.heading("#0", text="CC")
        self.dado_CadCdc.heading("#1", text="Centro de Custos")
        self.dado_CadCdc.heading("#2", text="Regional")
        self.dado_CadCdc.heading("#3", text="Gerência")

        self.dado_CadCdc.column("#0", width=50)
        self.dado_CadCdc.column("#1", width=500)
        self.dado_CadCdc.column("#2", width=200)
        self.dado_CadCdc.column("#3", width=150)
        self.dado_CadCdc.column("#4", width=310)

        self.dado_CadCdc.place(relx=0, rely=0, relwidth=0.985, relheight=1)

        self.scroll_dados_CadCdc = Scrollbar(self.frame_CadCdc, orient='vertical')
        self.dado_CadCdc.configure(xscrollcommand=self.scroll_dados_CadCdc.set)
        self.scroll_dados_CadCdc.place(relx=0.985, rely=0, relwidth=0.015, relheight=1)

        ## Dados Contas Contábeis ##
        self.dado_CadCC = ttk.Treeview(self.frame_CadCC, height=3, columns=("col1", "col2", "col3"))

        self.dado_CadCC.heading("#0", text="Red")
        self.dado_CadCC.heading("#1", text="Calssificação")
        self.dado_CadCC.heading("#2", text="Conta Contábil")

        self.dado_CadCC.column("#0", width=50)
        self.dado_CadCC.column("#1", width=100)
        self.dado_CadCC.column("#2", width=500)
        self.dado_CadCC.column("#3", width=560)

        self.dado_CadCC.place(relx=0, rely=0, relwidth=0.985, relheight=1)

        self.scroll_dados_CadCC = Scrollbar(self.frame_CadCC, orient='vertical')
        self.dado_CadCC.configure(xscrollcommand=self.scroll_dados_CadCC.set)
        self.scroll_dados_CadCC.place(relx=0.985, rely=0, relwidth=0.015, relheight=1)
        self.scroll_dados_CadCC = Scrollbar(self.frame_CadCC, orient='horizontal')
        self.dado_CadCC.configure(yscrollcommand=self.scroll_dados_CadCC.set)
        self.scroll_dados_CadCC.place(relx=0, rely=0.97, relwidth=0.985, relheight=0.03)

        self.frame_sec_CadUser.place(relx=0.70)
        self.frame_sec_CadEmp.place(relx=0.70)
        self.frame_sec_CadFil.place(relx=0.70)
        self.frame_sec_CadCdc.place(relx=0.70)
        self.frame_sec_CadCC.place(relx=0.70)

        self.tab_register.add(self.frame_sec_CadUser, text=" Usuário ")
        self.tab_register.add(self.frame_sec_CadEmp, text=" Empresa ")
        self.tab_register.add(self.frame_sec_CadReg, text=" Regional ")
        self.tab_register.add(self.frame_sec_CadFil, text=" Filial ")
        self.tab_register.add(self.frame_sec_CadCdc, text=" Centro de Custos ")
        self.tab_register.add(self.frame_sec_CadCC, text=" Contas Contábeis ")
     
