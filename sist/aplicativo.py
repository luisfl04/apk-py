from interface import *
import backend as core

app = None

def view_command():
    rows = core.view()
    app.list_clientes.delete(0, END)
    for r in rows:
        app.list_clientes.insert(END, r)

def search_command():
    app.list_clientes.delete(0, END)
    rows = core.search(app.txtNome.get(), app.txtSobrenome.get(), app.TxtEmail.get(), app.txtCPF.get())
    for r in rows:
        app.list_clientes.insert(END, r)

def insert_command():
    core.insert(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()

def update_command():
    core.update(selected[0], app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()

def del_command():
    id = selected[0]
    core.delete(id)
    view_command()

def getSelectedRow(event):
    global selected
    index = app.list_clientes.curselection()[0]
    selected = app.list_clientes.get(index)
    app.entNome.delete(0, END)
    app.entNome.insert(END, selected[1])
    app.entSobrenome.delete(0, END)
    app.entSobrenome.insert(END, selected[2])
    app.entEmail.delete(0, END)
    app.entEmail.insert(END, selected[3])
    app.entCPF.delete(0, END)
    app.entCPF.insert(END, selected[4])
    return selected

if __name__ == "__main__":
    app = Gui()
    app.list_clientes.bind("<<listboxSelect>>", getSelectedRow)

    app.btn_allview.configure(command = view_command)
    app.btn_buscar.configure(command = search_command)
    app.btn_inserir.configure(command = insert_command)
    app.btn_update.configure(command = update_command)
    app.btn_del.configure(command = del_command)
    app.btn_close.configure(command = app.window.destroy)
    app.run()

















