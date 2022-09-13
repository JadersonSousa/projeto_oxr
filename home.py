import tkinter
from tkinter import *
from tkinter import ttk
from turtle import title
from register import *
from formCadUser import *
from main import *
from logs import *


bg_main = '#D0E6F1'
color_text='#111'

class Home:
    def __init__(self, app):
        self.app = app
        self.app.state("zoomed")
        self.app.title("Sistema OxR")
        self.app.configure(bg=bg_main)

        usuarioLog = inforUserLog()[2]
        
        barraDeMenus=Menu(app)
        
        menuOxR=Menu(barraDeMenus,tearoff=0)
        menuOxR.add_command(label="Análise OxR",command=self.analiseOxR)
        barraDeMenus.add_cascade(label="Orçado x Realizado",menu=menuOxR)

        menuCadastros=Menu(barraDeMenus,tearoff=0)
        menuCadastros.add_command(label="Usuário",command=self.cadUser)
        menuCadastros.add_command(label="Empresa",command=self.cadEmp)
        menuCadastros.add_command(label="Filial",command=self.cadFil)
        menuCadastros.add_command(label="Regional",command=self.cadReg)
        menuCadastros.add_command(label="Centro de Custos",command=self.cadCdc)
        menuCadastros.add_command(label="Plano de Contas",command=self.cadCC)
        barraDeMenus.add_cascade(label="Cadastros",menu=menuCadastros)
        
        menuRelatorio=Menu(barraDeMenus,tearoff=0)
        #menuRelatorio.add_command(label="Análise",command=semComando)
        barraDeMenus.add_cascade(label="Relatório",menu=menuRelatorio)

        menuSuporte=Menu(barraDeMenus,tearoff=0)
        #menuSuporte.add_command(label="Análise",command=semComando)
        barraDeMenus.add_cascade(label="Suporte",menu=menuSuporte)                

        app.config(menu=barraDeMenus)


       
    def analiseOxR(self):
        self.frame_main = self.app
        self.frame_main = Frame(width=1900,  height=700, bg=bg_main, bd=0)
        self.frame_main.pack(fill='both', expand=0)
           
            # Campo Análise #
        self.frame_1 = Frame(self.frame_main)
        self.frame_1.place(relx=0.01, rely=0.10, relwidth=0.98, relheight=0.55)
        self.frame_1.configure(background='snow')
            # Campo Lançamentos #
        self.frame_2 = Frame(self.frame_main)
        self.frame_2.place(relx=0.01, rely=0.70, relwidth=0.51, relheight=0.28)
        self.frame_2.configure(background='snow')
            # Campo Comentários #
        self.frame_3 = Frame(self.frame_main)
        self.frame_3.place(relx=0.53, rely=0.70, relwidth=0.37, relheight=0.28)
        self.frame_3.configure(background='snow')

            # BOTÕES #
            # botão de filtragem do campo superior #
        self.bt_Mostrar = Button(self.frame_main, text="Mostrar", bd=2, bg='snow', fg='black')
        self.bt_Mostrar.place(relx=0.91, rely=0.02, relwidth=0.08, relheight=0.055)
            
            # botões do campo comentário #
        self.bt_Novo = Button(self.frame_main, text="Novo", bd=2, bg='snow', fg='black')
        self.bt_Novo.place(relx=0.91, rely=0.70, relwidth=0.08, relheight=0.05)

        self.bt_Salvar = Button(self.frame_main, text="Salvar", bd=2, bg='snow', fg='black')
        self.bt_Salvar.place(relx=0.91, rely=0.75, relwidth=0.08, relheight=0.05)

        self.bt_Enviar = Button(self.frame_main, text="Enviar", bd=2, bg='snow', fg='black')
        self.bt_Enviar.place(relx=0.91, rely=0.80, relwidth=0.08, relheight=0.05)

            

            # Label dos campos #

        self.lb_Analise = Label(self.frame_main, text="Análise", bg=bg_main, fg=color_text, font=('Arial Norrow', 9, 'bold'))
        self.lb_Analise.place(relx=0.01, rely=0.08, relheight=0.02)

        self.lb_Lancamento = Label(self.frame_main, text="Lançamentos", bg=bg_main, fg=color_text, font=('Arial Norrow', 9, 'bold'))
        self.lb_Lancamento.place(relx=0.01, rely=0.68, relheight=0.02)

        self.lb_Cometario = Label(self.frame_main, text="Comentários", bg=bg_main, fg=color_text, font=('Arial Norrow', 9, 'bold'))
        self.lb_Cometario.place(relx=0.53, rely=0.68, relheight=0.02)

            # Campo superior = Label e filtros #

        self.lb_Ano = Label(self.frame_main, text="Ano", bg=bg_main, fg=color_text, font=('Arial Norrow', 9, 'bold'))
        self.lb_Ano.place(relx=0.01, rely=0.01)
        self.ano_entry = Entry(self.frame_main)
        self.ano_entry.place(relx=0.01, rely=0.04, relwidth=0.05)

        self.lb_Mes = Label(self.frame_main, text="Mês", bg=bg_main, fg=color_text, font=('Arial Norrow', 9, 'bold'))
        self.lb_Mes.place(relx=0.07, rely=0.01)
        self.mes_entry = Entry(self.frame_main)
        self.mes_entry.place(relx=0.07, rely=0.04, relwidth=0.10)

        self.lb_Gerencia = Label(self.frame_main, text="Gerência", bg=bg_main, fg=color_text, font=('Arial Norrow', 9, 'bold'))
        self.lb_Gerencia.place(relx=0.18, rely=0.01)
        self.gerencia_entry = Entry(self.frame_main)
        self.gerencia_entry.place(relx=0.18, rely=0.04, relwidth=0.10)

        self.lb_Unidade = Label(self.frame_main, text="Unidade/Setor", bg=bg_main, fg=color_text, font=('Arial Norrow', 9, 'bold'))
        self.lb_Unidade.place(relx=0.29, rely=0.01)
        self.unidade_entry = Entry(self.frame_main)
        self.unidade_entry.place(relx=0.29, rely=0.04, relwidth=0.30)

        self.lb_Responsavel = Label(self.frame_main, text="Responsável", bg=bg_main, fg=color_text, font=('Arial Norrow', 9, 'bold'))
        self.lb_Responsavel.place(relx=0.60, rely=0.01)
        self.responsavel_entry = Entry(self.frame_main)
        self.responsavel_entry.place(relx=0.60, rely=0.04, relwidth=0.25)

            # Dados campo Análise #
        self.dados_analise = ttk.Treeview(self.frame_1, height=13, columns=("col1", "col2", "col3", "col4", "col5",
                                                                                "col6", "col7", "col8", "col9", "col10",
                                                                                "col11", "col12", "col13"))
        self.dados_analise.heading("#0", text="FL/CC")
        self.dados_analise.heading("#1", text="Filial/Centro de Custos")
        self.dados_analise.heading("#2", text="Red.")
        self.dados_analise.heading("#3", text="Descrição da Conta")
        self.dados_analise.heading("#4", text="Orçado Mensal")
        self.dados_analise.heading("#5", text="Realizado Mensal")
        self.dados_analise.heading("#6", text="Variação Mensal R$")
        self.dados_analise.heading("#7", text="Variação Mensal %")
        self.dados_analise.heading("#8", text="Total Ano Orçado")
        self.dados_analise.heading("#9", text="Acumulado Realizado")
        self.dados_analise.heading("#10", text="Saldo R$ Restante")
        self.dados_analise.heading("#11", text="Saldo % Restante")
        self.dados_analise.heading("#12", text="Situação")

        self.dados_analise.column("#0", width=45)
        self.dados_analise.column("#1", width=200)
        self.dados_analise.column("#2", width=45)
        self.dados_analise.column("#3", width=250)
        self.dados_analise.column("#4", width=90)
        self.dados_analise.column("#5", width=90)
        self.dados_analise.column("#6", width=90)
        self.dados_analise.column("#7", width=90)
        self.dados_analise.column("#8", width=90)
        self.dados_analise.column("#9", width=90)
        self.dados_analise.column("#10", width=90)
        self.dados_analise.column("#11", width=90)
        self.dados_analise.column("#12", width=90)
            
        self.dados_analise.place(relx=0, rely=0, relwidth=0.9855, relheight=1)

            # Barra de rolagem do campo análise #
        self.scroolAnalise = Scrollbar(self.frame_1, orient='vertical')
        self.dados_analise.configure(xscrollcommand=self.scroolAnalise.set)
        self.scroolAnalise.place(relx=0.985, rely=0, relwidth=0.015, relheight=1)

            # Dados campo Lançamento #
        self.dados_lancamento = ttk.Treeview(self.frame_2, height=3, columns=("col1", "col2", "col3"))
        self.dados_lancamento.heading("#0", text="Data")
        self.dados_lancamento.heading("#1", text="Histórico")
        self.dados_lancamento.heading("#2", text="Valor")

        self.dados_lancamento.column("#0", width=80)
        self.dados_lancamento.column("#1", width=450)
        self.dados_lancamento.column("#2", width=125)

        self.dados_lancamento.place(relx=0, rely=0, relwidth=0.97, relheight=1)

            # Barra de rolagem do campo lançamentos #
        self.scrollLancamento = Scrollbar(self.frame_2, orient='vertical')
        self.dados_lancamento.configure(xscrollcommand=self.scrollLancamento.set)
        self.scrollLancamento.place(relx=0.97, rely=0, relwidth=0.03, relheight=1)
 
    def cadUser(self):
                FormCadUser(frame_CadForm=Tk())

    def cadEmp(self):
                Register(frame_CadUserteste=Tk())

    def cadFil(self):
                Register(frame_CadUserteste=Tk())

    def cadReg(self):
                Register(frame_CadUserteste=Tk())

    def cadCdc(self):
                Register(frame_CadUserteste=Tk())

    def cadCC(self):
                Register(frame_CadUserteste=Tk())                                                            


if __name__ == '__main__':
    app = Tk()
    
    application = Home(app)
    app.mainloop()
