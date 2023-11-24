from tkinter import *


#classe de interface:
class Gui():
    x_pad = 5
    y_pad = 3
    width_entry = 30
    window = Tk()
    window.wm_title("Meu apk")
    
    #definindo as variáveis que recebem os dados:
    txtNome = StringVar()
    txtSobrenome = StringVar()
    txtCPF = StringVar()
    txtEmail = StringVar()
    
    # criando os labels:
    lbNome = Label(window , text = "Nome")
    lbSobrenome = Label(window, text= "Sobrenome")
    lbEmail = Label(window, text = "E-mail")
    lbCPF = Label(window, text = "CPF")
    
    # Entrada de dados e interatividade:
    entNome = Entry(window, textvariable = txtNome, width = width_entry)
    entSobrenome = Entry(window, textvariable = txtSobrenome, width = width_entry)
    entEmail = Entry(window, textvariable = txtEmail, width = width_entry)
    entCPF = Entry(window, textvariable = txtCPF, width = width_entry)
    list_clientes = Listbox(window, width = 100)
    scroll_clientes = Scrollbar(window)
    btn_allview = Button(window, text = "Ver todos")
    btn_buscar = Button(window, text = "Buscar")
    btn_inserir = Button(window, text = "Inserir")
    btn_update = Button(window, text = "Atualizar selecionados")
    btn_del = Button(window, text = "Deletar selecionados")
    btn_close = Button(window, text = "Fechar")
    
    #associando os objetos ao grid da janela:
    lbNome.grid(row = 0, column = 0)
    lbSobrenome.grid(row = 1, column = 0)
    lbEmail.grid(row = 2, column = 0)
    lbCPF.grid(row = 3, column = 0)
    entNome.grid(row = 0, column = 1, padx = 50, pady = 50)
    entSobrenome.grid(row = 1, column = 1)
    entEmail.grid(row = 2, column = 1)
    entCPF.grid(row = 3, column = 1)
    list_clientes.grid(row = 0, column = 2, rowspan = 10)
    scroll_clientes.grid(row = 0, column = 6, rowspan = 10)
    btn_allview.grid(row = 4, column = 0, columnspan = 2)
    btn_buscar.grid(row = 5, column = 0, columnspan = 2)
    btn_inserir.grid(row = 6, column = 0, columnspan = 2)
    btn_update.grid(row = 7, column = 0, columnspan = 2)
    btn_del.grid(row = 8, column = 0, columnspan = 2)
    btn_close.grid(row = 9, column = 0, columnspan = 2)
    
    # Conectando scrollbar com a listbox:
    list_clientes.configure(yscrollcommand = scroll_clientes.set)
    scroll_clientes.configure(command = list_clientes.yview)
    
    # Adionado aparência a interface:
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky = "WE", padx = x_pad, pady = y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx = 0, pady = 0, sticky = "NS")
        elif widget_class == "Scrollbar":
            child.grid_configure(padx = 0, pady = 0, sticky = "NS")
        else:
            child.grid_configure(padx = x_pad, pady = y_pad, sticky = "N")
        
    def run(self):
        Gui.window.mainloop()
    

















