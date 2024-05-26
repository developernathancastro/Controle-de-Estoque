import tkinter
from tkinter import *
import tkinter.messagebox
import pyodbc

dados_conexao = ("Driver={SQL Server};"
                 "Server=DESKTOP-5GB93JD;"
                 "Database=EstoqueMentoria")
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()


def btn_clicked0():
    nome_insumo = entry1.get()
    comando = f"""SELECT * from Insumos
                WHERE nome_insumo = '{nome_insumo}';
                """
    cursor.execute(comando)
    for linha in cursor.fetchall():
        entry0.delete("1.0", END)
        texto = f"Item: {linha.nome_insumo}\n Quantidade: {linha.qtde}\n Lote:{linha.lote}\n Validade:{linha.data_validade}"
        entry0.insert("1.0", texto)

def btn_clicked1():
    nome_insumo = entry1.get()
    comando = f"""DELETE from Insumos
                WHERE nome_insumo = '{nome_insumo}';
                """
    cursor.execute(comando)
    cursor.commit()
    tkinter.messagebox.showinfo(title="Aviso Insumo Excluído",
                                message=f"{nome_insumo} foi excluído do Banco de Dados!")

    entry1.delete(0, tkinter.END)

def btn_clicked2():
    nome_insumo = entry1.get()
    quantidade_usada = entry4.get()
    comando = f"""UPDATE Insumos
            SET qtde =qtde - {quantidade_usada}
            WHERE nome_insumo = '{nome_insumo}';
            """
    cursor.execute(comando)
    cursor.commit()
    tkinter.messagebox.showinfo(title="Aviso Uso Insumo", message=f"{quantidade_usada} unidades do {nome_insumo} foram usadas!")

def btn_clicked3():
    ##PEGAR TODOS OS CAMPO
    nome_insumo = entry1.get()
    data_validade = entry2.get()
    lote = entry3.get()
    quantidade = entry4.get()
    comando = f"""INSERT INTO Insumos(nome_insumo, data_validade,lote, qtde)
        VALUES
            ('{nome_insumo}', '{data_validade}', '{lote}', '{quantidade}')"""
    cursor.execute(comando)
    cursor.commit()
    tkinter.messagebox.showinfo(title="Aviso Adicionar Produto", message="Produto Adicionado com Sucesso!")
    entry1.delete(0, tkinter.END)
    entry2.delete(0, tkinter.END)
    entry3.delete(0, tkinter.END)
    entry4.delete(0, tkinter.END)


window = Tk()
window.title("CET")

window.geometry("711x646")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 646,
    width = 711,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    355.5, 323.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked0,
    relief = "flat")

b0.place(
    x = 479, y = 195,
    width = 178,
    height = 38)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked1,
    relief = "flat")

b1.place(
    x = 247, y = 197,
    width = 178,
    height = 36)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked2,
    relief = "flat")

b2.place(
    x = 479, y = 123,
    width = 178,
    height = 35)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked3,
    relief = "flat")

b3.place(
    x = 247, y = 125,
    width = 178,
    height = 34)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    455.0, 560.0,
    image = entry0_img)

entry0 = Text(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 250, y = 502,
    width = 410,
    height = 114)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    517.0, 294.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 377, y = 278,
    width = 280,
    height = 31)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    517.0, 340.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry2.place(
    x = 377, y = 324,
    width = 280,
    height = 31)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    517.0, 388.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry3.place(
    x = 377, y = 372,
    width = 280,
    height = 31)

entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(
    517.0, 436.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry4.place(
    x = 377, y = 420,
    width = 280,
    height = 31)

window.resizable(False, False)
window.mainloop()
