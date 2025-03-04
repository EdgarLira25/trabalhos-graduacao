import tkinter
from tkinter import ttk
from tkinter import messagebox
from connector import DB
from model import Hotel, Patrocinadores, Patrocinam

global credenciais

def TabelaCerta():
    
    if title_combobox.get() and crud_combobox.get():
        tabela = title_combobox.get()
        acao = crud_combobox.get()        
    else:
        tkinter.messagebox.showwarning(title ="ERROR", message = "Esta faltando informações")
        return 
    if tabela == "Hotel":
        hotel(acao)
    elif tabela == "Patrocinam":
        patrocinam(acao)
    elif tabela == "Patrocinadores":
        patrocinadores(acao)

def hotel(acao):

    if (acao == "Inserir"):
        hotel_insere = tkinter.Tk()
        hotel_insere.title("Inserir HOTEL")
        frame_hotel_insere = tkinter.Frame(hotel_insere)
        frame_hotel_insere.pack()

        hotel_info_frame = tkinter.LabelFrame(frame_hotel_insere, text = "Inserir Hotel")
        hotel_info_frame.grid(row = 0, column = 0, padx= 10, pady=20)

        label_Registro_Imobiliario = tkinter.Label(hotel_info_frame, text = "Registro Imobiliario(KEY)")
        label_Registro_Imobiliario.grid(row = 1, column =0, padx = 5, pady = 5)
        entry_Registro_Imobiliario = tkinter.Entry(hotel_info_frame)
        entry_Registro_Imobiliario.grid(row = 2, column = 0, padx =5, pady = 5)
        
        label_Nome_da_Fantasia = tkinter.Label(hotel_info_frame, text = "Nome da Fantasia")
        label_Nome_da_Fantasia.grid(row = 1, column =1, padx = 5, pady = 5)
        entry_Nome_da_Fantasia = tkinter.Entry(hotel_info_frame)
        entry_Nome_da_Fantasia.grid(row = 2, column = 1, padx =5, pady = 5)
        
        label_Tamanho  = tkinter.Label(hotel_info_frame, text = "Tamanho ")
        label_Tamanho.grid(row = 1, column = 2, padx = 5, pady = 5)
        entry_Tamanho = tkinter.Entry(hotel_info_frame)
        entry_Tamanho.grid(row = 2, column = 2, padx =5, pady = 5)
        
        label_Categoria = tkinter.Label(hotel_info_frame, text = "Categoria")
        label_Categoria.grid(row = 3, column = 0, padx = 5, pady = 5)
        entry_Categoria = tkinter.Entry(hotel_info_frame)
        entry_Categoria.grid(row = 4, column = 0, padx =5, pady = 5)
        
        label_Localização_Logradouro = tkinter.Label(hotel_info_frame, text = "Localização Logradouro")
        label_Localização_Logradouro.grid(row = 3, column = 1, padx = 5, pady = 5)
        entry_Localização_Logradouro = tkinter.Entry(hotel_info_frame)
        entry_Localização_Logradouro.grid(row = 4, column = 1, padx =5, pady = 5)
        
        label_Localização_Bairro  = tkinter.Label(hotel_info_frame, text = "Localização Bairro ")
        label_Localização_Bairro.grid(row = 3, column = 2, padx = 5, pady = 5)
        entry_Localização_Bairro = tkinter.Entry(hotel_info_frame)
        entry_Localização_Bairro.grid(row = 4, column = 2, padx =5, pady = 5)
        
        label_Localização_Numero = tkinter.Label(hotel_info_frame, text = "Localização Numero")
        label_Localização_Numero.grid(row = 5, column =0, padx = 5, pady = 5)
        entry_Localização_Numero = tkinter.Entry(hotel_info_frame)
        entry_Localização_Numero.grid(row = 6, column = 0, padx =5, pady = 5)
        
        label_Localização_Cidade = tkinter.Label(hotel_info_frame, text = "Localização Cidade")
        label_Localização_Cidade.grid(row = 5, column =1, padx = 5, pady = 5)
        entry_Localização_Cidade = tkinter.Entry(hotel_info_frame)
        entry_Localização_Cidade.grid(row = 6, column = 1, padx =5, pady = 5)
        
        label_Localização_CEP = tkinter.Label(hotel_info_frame, text = "Localização CEP")
        label_Localização_CEP.grid(row = 5, column = 2, padx = 5, pady = 5)
        entry_Localização_CEP = tkinter.Entry(hotel_info_frame)
        entry_Localização_CEP.grid(row = 6, column = 2, padx =5, pady = 5)
        
        label_Localização_Estado = tkinter.Label(hotel_info_frame, text = "Localização Estado")
        label_Localização_Estado.grid(row = 7, column =0, padx = 5, pady = 5)
        entry_Localização_Estado = tkinter.Entry(hotel_info_frame)
        entry_Localização_Estado.grid(row = 8, column = 0, padx =5, pady = 5)
        
        label_Registro_da_Rede = tkinter.Label(hotel_info_frame, text = "Registro da Rede(Número Padrão = 11111)")
        label_Registro_da_Rede.grid(row = 7, column =1, padx = 5, pady = 5)
        entry_Registro_da_Rede = tkinter.Entry(hotel_info_frame)
        entry_Registro_da_Rede.grid(row = 8, column = 1, padx =5, pady = 5)

        def hotel_insert():

            if (entry_Registro_Imobiliario.get() and entry_Nome_da_Fantasia.get() and entry_Tamanho.get() and entry_Categoria.get() and entry_Localização_Logradouro.get() and entry_Localização_Bairro.get() 
            and entry_Localização_Numero.get() and entry_Localização_Cidade.get() and entry_Localização_CEP.get() and entry_Localização_Estado.get() and entry_Registro_da_Rede.get()):
            
                regIM = entry_Registro_Imobiliario.get()
                nomeFant = entry_Nome_da_Fantasia.get()
                tamFant = entry_Tamanho.get()
                categ = entry_Categoria.get()
                locLogr = entry_Localização_Logradouro.get()
                locBairro = entry_Localização_Bairro.get()
                locNum = entry_Localização_Numero.get()
                locCity = entry_Localização_Cidade.get()
                locCEP = entry_Localização_CEP.get()
                locEst = entry_Localização_Estado.get()
                regRede = entry_Registro_da_Rede.get()

                hotelIn = Hotel(regIM, nomeFant, tamFant, categ, locLogr,locBairro,locNum,locCity,locCEP,locEst,regRede)
                teste = credenciais.insert_hotel(hotelIn)
                if (teste == True):
                    tkinter.messagebox.showwarning(title ="TRUE", message = "\n"+"INSERÇÃO BEM SUCEDIDA")
                else: 
                    tkinter.messagebox.showwarning(title ="FALSE", message = "\n"+"INSERÇÃO FALHOU")
            else:
                tkinter.messagebox.showwarning(title ="ERRO!!!", message = "\n"+"Falta Informação")
                return 

        button_hotel_insere = tkinter.Button(frame_hotel_insere, text = acao, command=hotel_insert)
        button_hotel_insere.grid(row=9, column=0, sticky="news", padx=20, pady=10) 

        hotel_insere.mainloop()

    elif (acao == "Remover"):
        
        hotel_remove = tkinter.Tk()
        hotel_remove.title("Remover HOTEL")
        frame_hotel_remove = tkinter.Frame(hotel_remove)
        frame_hotel_remove.pack()

        info_frame_hotel_remove = tkinter.LabelFrame(frame_hotel_remove, text = "Remover Hotel")
        info_frame_hotel_remove.grid(row = 0, column = 0, padx= 10, pady=20)

        ChaveRemove = tkinter.Label(info_frame_hotel_remove, text = "Preencha o campo com a KEY do Hotel a ser removido")    
        ChaveRemove.grid(row = 1, column = 0, padx= 10, pady= 10)

        Chave_entry = tkinter.Entry(info_frame_hotel_remove)
        Chave_entry.grid(row = 2, column=0, padx= 10, pady= 5)

        def hotel_rem():
            if (Chave_entry.get()):
                teste =credenciais.delete_hotel(Chave_entry.get())
                if (teste == True):
                    tkinter.messagebox.showwarning(title ="TRUE", message = "\n"+"REMOÇÃO BEM SUCEDIDA")
                else: 
                    tkinter.messagebox.showwarning(title ="FALSE", message = "\n"+"REMOÇÃO FALHOU")
            else:
                tkinter.messagebox.showwarning(title ="ERRO!!!", message = "\n"+"Falta Informação")
                return 

        buttonRemove = tkinter.Button(frame_hotel_remove, text = "Remover", command=hotel_rem)
        buttonRemove.grid(row=7, column=0, sticky="news", padx=20, pady=10)

        hotel_remove.mainloop()


    elif (acao == 'Atualizar'):

        hotel_atualiza = tkinter.Tk()
        hotel_atualiza.title("Atualizar HOTEL")
        frame_hotel_atualiza = tkinter.Frame(hotel_atualiza)
        frame_hotel_atualiza.pack()

        info_frame_hotel_atualiza = tkinter.LabelFrame(frame_hotel_atualiza, text = "Atualizar informação do hotel")
        info_frame_hotel_atualiza.grid(row = 0, column = 0, padx= 10, pady=20)

        label_ChaveUpdate = tkinter.Label(info_frame_hotel_atualiza, text = "Preencha com a KEY do hotel a ser alterado")    
        label_ChaveUpdate.grid(row = 1, column = 0, padx= 10, pady= 5)
        entry_ChaveUpdate = tkinter.Entry(info_frame_hotel_atualiza)
        entry_ChaveUpdate.grid(row = 2, column = 0, padx= 10, pady= 5)
        
        frame_hotel_atualiza2 = tkinter.LabelFrame(frame_hotel_atualiza, text = "Atualiza")
        frame_hotel_atualiza2.grid(row = 3, column = 0, padx= 10, pady=20)

        label_atualiza = tkinter.Label(frame_hotel_atualiza2, text = "Selecione o campo para atualizar")    
        label_atualiza.grid(row = 4, column = 0, padx= 10, pady= 5)

        campoAtualizar = ttk.Combobox(frame_hotel_atualiza2, values = ["Numero_Registro_Imobiliario", "Nome_Fantasia", "Tamanho_m2", "Categoria",
         "Loc_Logradouro", "Loc_Bairro", "Loc_Numero", "Loc_Cidade", "Loc_CEP", "Loc_Estado", "Registro_da_rede"])

        campoAtualizar.grid(row = 5, column = 0, padx= 10, pady= 5)
        
        selectUpdate = tkinter.Label(frame_hotel_atualiza2, text = "Preencha com a nova informação")    
        selectUpdate.grid(row = 6, column = 0, padx= 10, pady= 5)

        atualizar_entry = tkinter.Entry(frame_hotel_atualiza2)
        atualizar_entry.grid(row = 7, column=0, padx= 10, pady= 5)

        def hotel_att():

            if (atualizar_entry.get() and campoAtualizar.get() and entry_ChaveUpdate.get()):     
                teste = credenciais.alter_hotel(entry_ChaveUpdate.get(), campoAtualizar.get(), atualizar_entry.get())
                
                if (teste == True):
                    tkinter.messagebox.showwarning(title ="TRUE", message = "\n"+"ATUALIZAÇÃO BEM SUCEDIDA")
                else: 
                    tkinter.messagebox.showwarning(title ="FALSE", message = "\n"+"ATUALIZAÇÃO FALHOU")
            else:
                tkinter.messagebox.showwarning(title ="ERRO!!!", message = "\n"+"Falta Informação")
                return 
        
        button_hotel_atualiza = tkinter.Button(frame_hotel_atualiza, text = "Atualizar", command=hotel_att)
        button_hotel_atualiza.grid(row=8, column=0, sticky="news", padx=20, pady=10)

        hotel_atualiza.mainloop()

    elif (acao == 'Visualizar'):

        visualizar_hotel = tkinter.Tk()
        visualizar_hotel.title("Visualizar Hotel")
        frame_visualizar = tkinter.Frame(visualizar_hotel)
        frame_visualizar.pack()
        info_frame_frame_patrocinio_atualiza = tkinter.LabelFrame(frame_visualizar, text = "Hotel")
        info_frame_frame_patrocinio_atualiza.grid(row = 0, column = 0, padx= 10, pady=20)
        selectUpdate = tkinter.Label(info_frame_frame_patrocinio_atualiza, text = "Numero_Registro_Imobiliario(KEY) - Nome_Fantasia - Tamanho_m2 - Categoria - Loc_Logradouro  Loc_Bairro - Loc_Numero - Loc_Cidade - Loc_CEP - Loc_Estado - Registro_da_rede")    
        selectUpdate.grid(row = 1, column = 0, padx= 10, pady= 5)

        cont = 2
        for line in credenciais.select_all("HOTEL"):
            selectUpdate = tkinter.Label(info_frame_frame_patrocinio_atualiza, text = line)    
            selectUpdate.grid(row = cont, column = 0, padx= 10, pady= 5)
            cont  = cont + 1

        info_frame_frame_patrocinio_atualiza2 = tkinter.LabelFrame(frame_visualizar, text = "Busca especifica")
        info_frame_frame_patrocinio_atualiza2.grid(row = cont, column = 0, padx= 10, pady=20)

        selectUpdate = tkinter.Label(info_frame_frame_patrocinio_atualiza2, text = "Selecione o atributo")
        selectUpdate.grid(row = cont + 1, column = 0, padx= 30, pady= 5)
        campoVisu = ttk.Combobox(info_frame_frame_patrocinio_atualiza2, values = ["Numero_Registro_Imobiliario", "Nome_Fantasia", "Tamanho_m2", "Categoria",
         "Loc_Logradouro", "Loc_Bairro", "Loc_Numero", "Loc_Cidade", "Loc_CEP", "Loc_Estado", "Registro_da_rede"])
        campoVisu.grid(row = cont +2, column = 0, padx= 10, pady= 5)
        
        selectUpdate = tkinter.Label(info_frame_frame_patrocinio_atualiza2, text = "Preencha com o valor que deseja buscar")
        selectUpdate.grid(row = cont + 3, column = 0, padx= 30, pady= 5)
        entry_selectUp = tkinter.Entry(info_frame_frame_patrocinio_atualiza2)
        entry_selectUp.grid(row = cont + 4, column = 0, padx= 30, pady= 5)

        def buscando_hotel():
            if entry_selectUp.get() and campoVisu.get():
                patrocinadores_visu = tkinter.Tk()
                patrocinadores_visu.title("Vizualizar Hotel")
                frame_patrocinadores_visu = tkinter.Frame(patrocinadores_visu)
                frame_patrocinadores_visu.pack()
                info_frame_frame_patrocinadores_visu = tkinter.LabelFrame(frame_patrocinadores_visu, text = "Hotel")
                info_frame_frame_patrocinadores_visu.grid(row = 0, column = 0, padx= 10, pady=20)

                selectUpdate = tkinter.Label(info_frame_frame_patrocinadores_visu, text = "Numero_Registro_Imobiliario(KEY) - Nome_Fantasia - Tamanho_m2 - Categoria - Loc_Logradouro  Loc_Bairro - Loc_Numero - Loc_Cidade - Loc_CEP - Loc_Estado - Registro_da_rede")
                selectUpdate.grid(row = 1, column = 0, padx= 30, pady= 5)

                espec = credenciais.select_especific_value(campoVisu.get(), entry_selectUp.get(), "HOTEL")
                cont1 = 2
                for line in espec:
                    selectUpdate = tkinter.Label(info_frame_frame_patrocinadores_visu, text = line)
                    selectUpdate.grid(row = cont1, column = 0, padx= 30, pady= 5)
                    cont1 = cont1 + 1

                patrocinadores_visu.mainloop()

        buttonBusca = tkinter.Button(info_frame_frame_patrocinio_atualiza2, text = "buscar", command= buscando_hotel)
        buttonBusca.grid(row = cont + 5, column=0, sticky="news", padx=20, pady=10)

        visualizar_hotel.mainloop()

def patrocinadores(acao):
    
    if (acao == "Inserir"):
        patrocinadores_insere = tkinter.Tk()
        patrocinadores_insere.title("Inserir Patrocinador")
        frame_patrocinadores_insere = tkinter.Frame(patrocinadores_insere)
        frame_patrocinadores_insere.pack()

        info_frame_patrocinadores_insere = tkinter.LabelFrame(frame_patrocinadores_insere, text = "Inserir Patrocinador")
        info_frame_patrocinadores_insere.grid(row = 0, column = 0, padx= 10, pady=20)

        label_NomePatr = tkinter.Label(info_frame_patrocinadores_insere, text = "Nome do Patrocinador")
        label_NomePatr.grid(row = 1, column = 0, padx= 5, pady=5)
        entry_NomePatr = tkinter.Entry(info_frame_patrocinadores_insere)
        entry_NomePatr.grid(row = 2, column=0, padx= 5, pady=5)
        
        label_TipoPatr = tkinter.Label(info_frame_patrocinadores_insere, text = "Tipo de patrocinio")
        label_TipoPatr.grid(row = 1, column = 1, padx= 5, pady=5)
        entry_TipoPatr = tkinter.Entry(info_frame_patrocinadores_insere)
        entry_TipoPatr.grid(row = 2, column=1, padx= 5, pady=5)
        
        label_Inicio = tkinter.Label(info_frame_patrocinadores_insere, text = "Data de Início (Exemplo ano-mes-dia, 2010-10-15)")
        label_Inicio.grid(row = 3, column = 0, padx= 5, pady=5)
        entry_Inicio = tkinter.Entry(info_frame_patrocinadores_insere)
        entry_Inicio.grid(row = 4, column = 0, padx= 5, pady=5)
        
        label_CNPJ = tkinter.Label(info_frame_patrocinadores_insere, text = "CNPJ")
        label_CNPJ.grid(row = 3, column = 1, padx= 5, pady=5)
        entry_CNPJ = tkinter.Entry(info_frame_patrocinadores_insere)
        entry_CNPJ.grid(row = 4, column = 1, padx= 5, pady=5)

        def patrocinadorIn():

            if (entry_NomePatr.get() and entry_Inicio.get() and entry_TipoPatr.get() and entry_CNPJ.get()):
                
                patro = Patrocinadores(entry_NomePatr.get(), entry_TipoPatr.get(), entry_Inicio.get(), entry_CNPJ.get())
                
                teste = credenciais.insert_patrocinadores(patro)

                if (teste == True):
                    tkinter.messagebox.showwarning(title ="TRUE", message = "\n"+"INSERÇÃO BEM SUCEDIDA")
                else: 
                    tkinter.messagebox.showwarning(title ="FALSE", message = "\n"+"INSERÇÃO FALHOU")

            else:
                tkinter.messagebox.showwarning(title ="ERRO!!!", message = "\n"+"Falta Informação")
                return 
        
        button_patrocinadores_insere = tkinter.Button(frame_patrocinadores_insere, text = acao, command= patrocinadorIn)
        button_patrocinadores_insere.grid(row=4, column=0, sticky="news", padx=20, pady=10)  

        patrocinadores_insere.mainloop()

    elif (acao == "Remover"):
        
        patrocinadores_remove = tkinter.Tk()
        patrocinadores_remove.title("Remover Patrocinador")
        frame_patrocinadores_remove = tkinter.Frame(patrocinadores_remove)
        frame_patrocinadores_remove.pack()

        info_frame_patrocinadores_remove = tkinter.LabelFrame(frame_patrocinadores_remove, text = "Remover patrocinador")
        info_frame_patrocinadores_remove.grid(row = 0, column = 0, padx= 10, pady=20)

        label_Chave = tkinter.Label(info_frame_patrocinadores_remove, text = "Preencha com a chave do patrocinador a ser removido")    
        label_Chave.grid(row = 1, column = 0, padx= 10, pady= 5)

        entry_Chave = tkinter.Entry(info_frame_patrocinadores_remove)
        entry_Chave.grid(row = 2, column=0, padx= 10, pady= 5)

        def patro_rem():

            if (entry_Chave.get()):
                teste = credenciais.delete_patrocinadores(entry_Chave.get())
                if (teste == True):
                    tkinter.messagebox.showwarning(title ="TRUE", message = "\n"+"REMOÇÃO BEM SUCEDIDA")
                else: 
                    tkinter.messagebox.showwarning(title ="FALSE", message = "\n"+"REMOÇÃO FALHOU")
            else:
                tkinter.messagebox.showwarning(title ="ERRO!!!", message = "\n"+"Falta Informação")
                return 


        buttonRemove = tkinter.Button(frame_patrocinadores_remove, text = "Remover", command = patro_rem)
        buttonRemove.grid(row=7, column=0, sticky="news", padx=20, pady=10)

        patrocinadores_remove.mainloop()


    elif (acao == 'Atualizar'):

        patrocinador_atualiza = tkinter.Tk()
        patrocinador_atualiza.title("Atualizar Patrocinador")
        frame_patrocinadores_atualiza = tkinter.Frame(patrocinador_atualiza)
        frame_patrocinadores_atualiza.pack()

        info_frame_patrocinadores_atualiza = tkinter.LabelFrame(frame_patrocinadores_atualiza, text = "Atualizar Patrocinador")
        info_frame_patrocinadores_atualiza.grid(row = 0, column = 0, padx= 10, pady=20)

        ChaveUpdate = tkinter.Label(info_frame_patrocinadores_atualiza, text = "Preencha com a chave do Patrocinador a ser alterado")    
        ChaveUpdate.grid(row = 1, column = 0, padx= 10, pady= 5)

        Chave_entry_Att = tkinter.Entry(info_frame_patrocinadores_atualiza)
        Chave_entry_Att.grid(row = 2, column=0, padx= 10, pady= 5)

        info_frame_patrocinadores_atualiza2 = tkinter.LabelFrame(frame_patrocinadores_atualiza, text = "Atualiza")
        info_frame_patrocinadores_atualiza2.grid(row = 3, column = 0, padx= 10, pady=20)

        selectUpdate = tkinter.Label(info_frame_patrocinadores_atualiza2, text = "Selecione o campo para atualizar")    
        selectUpdate.grid(row = 4, column = 0, padx= 10, pady= 5)

        campoAtualizarAtt = ttk.Combobox(info_frame_patrocinadores_atualiza2, values = ["Nome","Tipo_de_patrocinio","Data_de_Inicio","CNPJ"])
        campoAtualizarAtt.grid(row = 5, column = 0, padx= 10, pady= 5)
        
        selectUpdate = tkinter.Label(info_frame_patrocinadores_atualiza2, text = "Preencha com a nova informação")    
        selectUpdate.grid(row = 6, column = 0, padx= 10, pady= 5)

        atualizar_entry_patrocinam = tkinter.Entry(info_frame_patrocinadores_atualiza2)
        atualizar_entry_patrocinam.grid(row = 7, column=0, padx= 10, pady= 5)
        
        def patrocinador_att():

            if (atualizar_entry_patrocinam.get() and campoAtualizarAtt.get() and Chave_entry_Att.get()):     
                teste = credenciais.alter_patrocinadores(Chave_entry_Att.get(), campoAtualizarAtt.get(), atualizar_entry_patrocinam.get())
                if (teste == True):
                    tkinter.messagebox.showwarning(title ="TRUE", message = "\n"+"ATUALIZAÇÃO BEM SUCEDIDA")
                else: 
                    tkinter.messagebox.showwarning(title ="FALSE", message = "\n"+"ATUALIZAÇÃO FALHOU")
            else:
                tkinter.messagebox.showwarning(title ="ERRO!!!", message = "\n"+"Falta Informação")
                return 

        buttonUpdate = tkinter.Button(frame_patrocinadores_atualiza, text = "Atualizar", command=patrocinador_att)
        buttonUpdate.grid(row=8, column=0, sticky="news", padx=20, pady=10)

        patrocinador_atualiza.mainloop()

    elif (acao == 'Visualizar'):
        patrocinador_visualiza = tkinter.Tk()
        patrocinador_visualiza.title("Visualizar Patrocinadores")
        frame_patrocinio_atualiza = tkinter.Frame(patrocinador_visualiza)
        frame_patrocinio_atualiza.pack()
        info_frame_frame_patrocinio_atualiza = tkinter.LabelFrame(frame_patrocinio_atualiza, text = "Patrocinadores")
        info_frame_frame_patrocinio_atualiza.grid(row = 0, column = 0, padx= 10, pady=20)
        
        selectUpdate = tkinter.Label(info_frame_frame_patrocinio_atualiza, text = "Nome - Tipo - Data_Inicio - CNPJ(KEY)")    
        selectUpdate.grid(row = 1, column = 0, padx= 10, pady= 5)
        
        cont = 2
        for line in credenciais.select_all("PATROCINADORES"):
            selectUpdate = tkinter.Label(info_frame_frame_patrocinio_atualiza, text = line)    
            selectUpdate.grid(row = cont, column = 0, padx= 10, pady= 5)
            cont  = cont + 1

        info_frame_frame_patrocinio_atualiza2 = tkinter.LabelFrame(frame_patrocinio_atualiza, text = "Busca especifica")
        info_frame_frame_patrocinio_atualiza2.grid(row = cont, column = 0, padx= 10, pady=20)

        selectUpdate = tkinter.Label(info_frame_frame_patrocinio_atualiza2, text = "Selecione o atributo")
        selectUpdate.grid(row = cont + 1, column = 0, padx= 30, pady= 5)
        campoVisu = ttk.Combobox(info_frame_frame_patrocinio_atualiza2, values = ["Nome","Tipo_de_patrocinio","Data_de_Inicio","CNPJ"])
        campoVisu.grid(row = cont +2, column = 0, padx= 10, pady= 5)
        
        selectUpdate = tkinter.Label(info_frame_frame_patrocinio_atualiza2, text = "Preencha com o valor que deseja buscar")
        selectUpdate.grid(row = cont + 3, column = 0, padx= 30, pady= 5)
        entry_selectUp = tkinter.Entry(info_frame_frame_patrocinio_atualiza2)
        entry_selectUp.grid(row = cont + 4, column = 0, padx= 30, pady= 5)

        def buscando_patro():
            if entry_selectUp.get() and campoVisu.get():
                patrocinadores_visu = tkinter.Tk()
                patrocinadores_visu.title("Visualizar Patrocinadores")
                frame_patrocinadores_visu = tkinter.Frame(patrocinadores_visu)
                frame_patrocinadores_visu.pack()
                info_frame_frame_patrocinadores_visu = tkinter.LabelFrame(frame_patrocinadores_visu, text = "Patrocinadores")
                info_frame_frame_patrocinadores_visu.grid(row = 0, column = 0, padx= 10, pady=20)

                selectUpdate = tkinter.Label(info_frame_frame_patrocinadores_visu, text =  "Nome - Tipo - Data_Inicio - CNPJ(KEY)")
                selectUpdate.grid(row = 1, column = 0, padx= 30, pady= 5)

                espec = credenciais.select_especific_value(campoVisu.get(), entry_selectUp.get(), "PATROCINADORES")
                cont1 = 2
                for line in espec:
                    selectUpdate = tkinter.Label(info_frame_frame_patrocinadores_visu, text = line)
                    selectUpdate.grid(row = cont1, column = 0, padx= 30, pady= 5)
                    cont1 = cont1 + 1

                patrocinadores_visu.mainloop()

        buttonBusca = tkinter.Button(info_frame_frame_patrocinio_atualiza2, text = "buscar", command= buscando_patro)
        buttonBusca.grid(row = cont + 5, column=0, sticky="news", padx=20, pady=10)

        patrocinador_visualiza.mainloop()

def patrocinam(acao):
    
    if (acao == "Inserir"):

        patrocinio_insere = tkinter.Tk()
        patrocinio_insere.title("Inserir Patrocinio")
        frame_patrocinio_insere = tkinter.Frame(patrocinio_insere)
        frame_patrocinio_insere.pack()

        info_frame_patrocinio_insere = tkinter.LabelFrame(frame_patrocinio_insere, text = "Inserir Patrocínio")
        info_frame_patrocinio_insere.grid(row = 0, column = 0, padx= 10, pady=20)
        
        label_RegImob = tkinter.Label(info_frame_patrocinio_insere, text = "Número do Registro Imobiliário(KEY)")
        label_RegImob.grid(row = 1, column = 0, padx= 5, pady=5)
        entry_RegImob = tkinter.Entry(info_frame_patrocinio_insere)
        entry_RegImob.grid(row = 2, column=0, padx= 5, pady=5)

        label_CNPJpatro = tkinter.Label(info_frame_patrocinio_insere, text = "CNPJ do Patrocinador(KEY)")
        label_CNPJpatro.grid(row = 1, column = 1, padx= 5, pady = 5)
        entry_CNPJpatro = tkinter.Entry(info_frame_patrocinio_insere)
        entry_CNPJpatro.grid(row = 2, column=1, padx= 5, pady = 5)
        
        def insere_patrocinam():
            
            if (entry_RegImob.get() and entry_CNPJpatro.get()):

                patrocinamIN = Patrocinam(entry_RegImob.get(), entry_CNPJpatro.get())
               
                teste = credenciais.insert_patrocinam(patrocinamIN)
                
                if (teste == True):
                    tkinter.messagebox.showwarning(title ="TRUE", message = "\n"+"INSERÇÃO BEM SUCEDIDA")
                else: 
                    tkinter.messagebox.showwarning(title ="FALSE", message = "\n"+"INSERÇÃO FALHOU")

            else:
                tkinter.messagebox.showwarning(title ="ERRO!!!", message = "\n"+"Falta Informação")
                return 
        
        button_patrocinio_insere = tkinter.Button(frame_patrocinio_insere, text = acao, command=insere_patrocinam)
        button_patrocinio_insere.grid(row=4, column=0, sticky="news", padx=20, pady=10)  

        patrocinio_insere.mainloop()

    elif (acao == "Remover"):
        
        patrocinio_remove = tkinter.Tk()
        patrocinio_remove.title("Remover Patrocínio")
        frame_patrocinio_remove = tkinter.Frame(patrocinio_remove)
        frame_patrocinio_remove.pack()

        info_frame_patrocinio_remove = tkinter.LabelFrame(frame_patrocinio_remove, text = "Remover Patrocínio")
        info_frame_patrocinio_remove.grid(row = 0, column = 0, padx= 10, pady=20)

        label_ChaveRemove = tkinter.Label(info_frame_patrocinio_remove, text = "Preencha com as chaves do patrocinador e do hotel")    
        label_ChaveRemove.grid(row = 1, column = 0, padx= 10, pady= 5)
        
        label_ChaveCNPJ = tkinter.Label(info_frame_patrocinio_remove, text = "CNPJ do patrocinador")    
        label_ChaveCNPJ.grid(row = 2, column = 0, padx= 10, pady= 5)
        entry_ChaveRemove = tkinter.Entry(info_frame_patrocinio_remove)
        entry_ChaveRemove.grid(row = 3, column=0, padx= 10, pady= 5)

        label_ChaveReg = tkinter.Label(info_frame_patrocinio_remove, text = "Registro Imobiliário do hotel")    
        label_ChaveReg.grid(row = 4, column = 0, padx= 10, pady= 5)
        entry_ChaveRemove2 = tkinter.Entry(info_frame_patrocinio_remove)
        entry_ChaveRemove2.grid(row = 5, column=0, padx= 10, pady= 5)
        
        def patrocinam_rem():

            if (entry_ChaveRemove2.get() and entry_ChaveRemove.get()):

                teste = credenciais.delete_patrocinam(entry_ChaveRemove2.get(), entry_ChaveRemove.get())
                if (teste == True):
                    tkinter.messagebox.showwarning(title ="TRUE", message = "\n"+"REMOÇÃO BEM SUCEDIDA")
                else: 
                    tkinter.messagebox.showwarning(title ="FALSE", message = "\n"+"REMOÇÃO FALHOU")
            
            else:
                tkinter.messagebox.showwarning(title ="ERRO!!!", message = "\n"+"Falta Informação")
                return 

        buttonRemove = tkinter.Button(frame_patrocinio_remove, text = "Remover", command=patrocinam_rem)
        buttonRemove.grid(row=6, column=0, sticky="news", padx=20, pady=10)

        patrocinio_remove.mainloop()

    elif (acao == 'Atualizar'):

        patrocinio_atualiza = tkinter.Tk()
        patrocinio_atualiza.title("Atualizar Patrocínio")
        frame_patrocinio_atualiza = tkinter.Frame(patrocinio_atualiza)
        frame_patrocinio_atualiza.pack()

        info_frame_frame_patrocinio_atualiza = tkinter.LabelFrame(frame_patrocinio_atualiza, text = "Atualizar Patrocínio")
        info_frame_frame_patrocinio_atualiza.grid(row = 0, column = 0, padx= 10, pady=20)

        ChaveUpdate = tkinter.Label(info_frame_frame_patrocinio_atualiza, text = "Preencha com as chave do patrocínio a ser alterado")    
        ChaveUpdate.grid(row = 1, column = 0, padx= 10, pady= 5)
        
        label_ChaveCNPJ = tkinter.Label(info_frame_frame_patrocinio_atualiza, text = "CNPJ do patrocinador")    
        label_ChaveCNPJ.grid(row = 2, column = 0, padx= 10, pady= 5)
        entry_ChaveRemoveP = tkinter.Entry(info_frame_frame_patrocinio_atualiza)
        entry_ChaveRemoveP.grid(row = 2, column= 1, padx= 10, pady= 5)

        label_ChaveReg = tkinter.Label(info_frame_frame_patrocinio_atualiza, text = "Registro Imobiliário do hotel")    
        label_ChaveReg.grid(row = 3, column = 0, padx= 10, pady= 5)
        entry_ChaveRemove2P = tkinter.Entry(info_frame_frame_patrocinio_atualiza)
        entry_ChaveRemove2P.grid(row = 3, column=1, padx= 10, pady= 5)
        
        info_frame_frame_patrocinio_atualiza2 = tkinter.LabelFrame(frame_patrocinio_atualiza, text = "Atualiza")
        info_frame_frame_patrocinio_atualiza2.grid(row = 4, column = 0, padx= 10, pady=20)
        
        selectUpdate = tkinter.Label(info_frame_frame_patrocinio_atualiza2, text = "Selecione o campo para atualizar")    
        selectUpdate.grid(row = 5, column = 0, padx= 10, pady= 5)

        campoAtualizarP = ttk.Combobox(info_frame_frame_patrocinio_atualiza2, values = ["CNPJ", "Numero_Registro_Imobiliario"])
        campoAtualizarP.grid(row = 6, column = 0, padx= 10, pady= 5)
        
        selectUpdate = tkinter.Label(info_frame_frame_patrocinio_atualiza2, text = "Preencha com a nova informação")    
        selectUpdate.grid(row = 7, column = 0, padx= 10, pady= 5)

        atualizar_entryP = tkinter.Entry(info_frame_frame_patrocinio_atualiza2)
        atualizar_entryP.grid(row = 8, column=0, padx= 10, pady= 5)

        def patrocinam_att():

            if (campoAtualizarP.get() and atualizar_entryP.get() and entry_ChaveRemoveP.get() and entry_ChaveRemove2P.get()):

               teste = credenciais.alter_patrocinam(entry_ChaveRemove2P.get(), entry_ChaveRemoveP.get(), campoAtualizarP.get(), atualizar_entryP.get())
               if (teste == True):
                    tkinter.messagebox.showwarning(title ="TRUE", message = "\n"+"ATUALIZAÇÃO BEM SUCEDIDA")
               else: 
                    tkinter.messagebox.showwarning(title ="FALSE", message = "\n"+"ATUALIZAÇÃO FALHOU")
                
            else:
                tkinter.messagebox.showwarning(title ="ERRO!!!", message = "\n"+"Falta Informação")
                return 

        buttonUpdate = tkinter.Button(frame_patrocinio_atualiza, text = "Atualizar", command= patrocinam_att)
        buttonUpdate.grid(row=9, column=0, sticky="news", padx=20, pady=10)

        patrocinio_atualiza.mainloop()
    
    elif (acao == 'Visualizar'):

        patrocinio_atualiza = tkinter.Tk()
        patrocinio_atualiza.title("Visualizar Patrocinam")
        frame_patrocinio_atualiza = tkinter.Frame(patrocinio_atualiza)
        frame_patrocinio_atualiza.pack()
        info_frame_frame_patrocinio_atualiza = tkinter.LabelFrame(frame_patrocinio_atualiza, text = "Patrocinam")
        info_frame_frame_patrocinio_atualiza.grid(row = 0, column = 0, padx= 10, pady=20)
        
        selectUpdate = tkinter.Label(info_frame_frame_patrocinio_atualiza, text = "REGISTRO_IMOB(KEY) - CNPJ(KEY)")
        selectUpdate.grid(row = 1, column = 0, padx= 30, pady= 5)
        
        cont = 2
        for line in credenciais.select_all("PATROCINAM"):
            selectUpdate = tkinter.Label(info_frame_frame_patrocinio_atualiza, text = line)
            selectUpdate.grid(row = cont, column = 0, padx= 30, pady= 5)
            cont  = cont + 1
        

        info_frame_frame_patrocinio_atualiza2 = tkinter.LabelFrame(frame_patrocinio_atualiza, text = "Busca especifica")
        info_frame_frame_patrocinio_atualiza2.grid(row = cont, column = 0, padx= 10, pady=20)

        selectUpdate = tkinter.Label(info_frame_frame_patrocinio_atualiza2, text = "Selecione o atributo")
        selectUpdate.grid(row = cont + 1, column = 0, padx= 30, pady= 5)
        campoVisu = ttk.Combobox(info_frame_frame_patrocinio_atualiza2, values = ["CNPJ", "Numero_Registro_Imobiliario"])
        campoVisu.grid(row = cont +2, column = 0, padx= 10, pady= 5)
        
        selectUpdate = tkinter.Label(info_frame_frame_patrocinio_atualiza2, text = "Preencha com o valor que deseja buscar")
        selectUpdate.grid(row = cont + 3, column = 0, padx= 30, pady= 5)
        entry_selectUp = tkinter.Entry(info_frame_frame_patrocinio_atualiza2)
        entry_selectUp.grid(row = cont + 4, column = 0, padx= 30, pady= 5)

        def buscando():
            if entry_selectUp.get() and campoVisu.get():
                patrocinam_visu = tkinter.Tk()
                patrocinam_visu.title("Visualizar Patrocinam")
                frame_patrocinam_visu = tkinter.Frame(patrocinam_visu)
                frame_patrocinam_visu.pack()
                info_frame_frame_patrocinam_visu = tkinter.LabelFrame(frame_patrocinam_visu, text = "Patrocinam")
                info_frame_frame_patrocinam_visu.grid(row = 0, column = 0, padx= 10, pady=20)

                selectUpdate = tkinter.Label(info_frame_frame_patrocinam_visu, text = "REGISTRO_IMOB(KEY) - CNPJ(KEY)")
                selectUpdate.grid(row = 1, column = 0, padx= 30, pady= 5)

                espec = credenciais.select_especific_value(campoVisu.get(), entry_selectUp.get(), "PATROCINAM")
                cont1 = 2
                for line in espec:
                    selectUpdate = tkinter.Label(info_frame_frame_patrocinam_visu, text = line)
                    selectUpdate.grid(row = cont1, column = 0, padx= 30, pady= 5)
                    cont1 = cont1 + 1

        buttonBusca = tkinter.Button(info_frame_frame_patrocinio_atualiza2, text = "buscar", command= buscando)
        buttonBusca.grid(row = cont + 5, column=0, sticky="news", padx=20, pady=10)

        patrocinio_atualiza.mainloop()
        


if __name__ == "__main__":

    ConectBD = tkinter.Tk()
    ConectBD.title("Banco de Dados")
    frame = tkinter.Frame(ConectBD)
    frame.pack()

    user_info_frame = tkinter.LabelFrame(frame, text = "Conectando com o Banco de Dados")
    user_info_frame.grid(row = 0, column = 0, padx = 10, pady=10)

    ChaveHost = tkinter.Label(user_info_frame, text = "Nome do Host")    
    ChaveHost.grid(row = 3, column = 0, padx = 20, pady= 5)
    ChaveHost_entry = tkinter.Entry(user_info_frame)
    ChaveHost_entry.grid(row = 4, column=0, padx = 20, pady= 5)
    
    ChavePorta = tkinter.Label(user_info_frame, text = "Porta")    
    ChavePorta.grid(row = 5, column = 0, padx = 20, pady= 5)
    ChavePorta_entry = tkinter.Entry(user_info_frame)
    ChavePorta_entry.grid(row = 6, column=0, padx = 20, pady= 5)
    
    ChaveUser = tkinter.Label(user_info_frame, text = "User")    
    ChaveUser.grid(row = 7, column = 0, padx = 20, pady= 5)
    ChaveUser_entry = tkinter.Entry(user_info_frame)
    ChaveUser_entry.grid(row = 8, column=0, padx = 20, pady= 5)

    ChaveSenha = tkinter.Label(user_info_frame, text = "Senha")    
    ChaveSenha.grid(row = 9, column = 0, padx = 20, pady= 5)
    ChaveSenha_entry = tkinter.Entry(user_info_frame)
    ChaveSenha_entry.grid(row = 10, column=0, padx = 20, pady= 5)

    ChaveDBase = tkinter.Label(user_info_frame, text = "DataBase")    
    ChaveDBase.grid(row = 11, column = 0, padx = 20, pady= 5)
    ChaveDBase_entry = tkinter.Entry(user_info_frame)
    ChaveDBase_entry.grid(row = 12, column=0, padx = 20, pady= 5)

    def ConectaEFecha():
        
        global credenciais

        if (ChaveHost_entry.get() and ChaveSenha_entry.get() and ChavePorta_entry.get() and ChaveUser_entry.get() and ChaveDBase_entry.get()):

            host = ChaveHost_entry.get() 
            senha = ChaveSenha_entry.get() 
            porta = ChavePorta_entry.get() 
            user =  ChaveUser_entry.get()
            dbase = ChaveDBase_entry.get()

            credenciais = DB(host, dbase, user, senha, porta)

        else:
            tkinter.messagebox.showwarning(title ="ERRO!!!", message = "\n"+"Falta Informação")
            return 

        tkinter.messagebox.showwarning(title ="", message = "\n"+"Configurando...")
        ConectBD.destroy()

    buttonConfirmar = tkinter.Button(frame, text = "Conectar", command=ConectaEFecha)
    buttonConfirmar.grid(row=13, column=0, sticky="news", padx=20, pady=10)

    ConectBD.mainloop()

    window = tkinter.Tk()
    window.title("Interface Banco de Dados")
    frame = tkinter.Frame(window)
    frame.pack()

    user_info_frame = tkinter.LabelFrame(frame, text = "Configurando")
    user_info_frame.grid(row = 0, column = 0, padx = 10, pady=20)

    selectTabela = tkinter.Label(user_info_frame, text = "Selecione a Tabela")    
    selectTabela.grid(row = 1, column = 0, padx = 10, pady= 5)

    title_combobox = ttk.Combobox(user_info_frame, values = ["Hotel","Patrocinadores", "Patrocinam"])
    title_combobox.grid(row = 2, column = 0, padx = 10, pady= 5)

    selectAction = tkinter.Label(user_info_frame, text = "Selecionar Ação")    
    selectAction.grid(row = 1, column = 1)

    crud_combobox = ttk.Combobox(user_info_frame, values = ["Inserir", "Remover", "Atualizar", "Visualizar"])
    crud_combobox.grid(row = 2, column = 1, padx = 10, pady= 10)

    button = tkinter.Button(frame, text = "Confirmar", command = TabelaCerta)
    button.grid(row=4, column=0, sticky="news", padx=20, pady=10)

    window.mainloop()
