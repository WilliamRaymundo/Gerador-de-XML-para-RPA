import tkinter as tk
from datetime import date
import xml.etree.ElementTree as ET

def gerar_xml():
    autor = entry_autor.get()
    hoje = date.today().strftime("%Y-%m-%d")
    
    # Criação dos elementos XML
    raiz = ET.Element("root")
    comentario = ET.Comment(" {}".format(autor))
    raiz.append(comentario)
    data = ET.SubElement(raiz, "data")
    data.text = hoje
    
    # Cria o objeto ElementTree
    tree = ET.ElementTree(raiz)
    
    # Gera a string XML
    xml_string = '<?xml version="1.0" encoding="utf-8"?>\n' + ET.tostring(raiz, encoding="utf-8").decode()
    
    # Salva o XML em um arquivo
    with open("output.xml", "w") as xml_file:
        xml_file.write(xml_string)
    
    # Exibe uma mensagem de sucesso
    lbl_resultado.config(text="XML gerado com sucesso!")

# Cria a janela principal
janela = tk.Tk()
janela.title("Gerador de XML")

# Cria os elementos da interface
lbl_autor = tk.Label(janela, text="Autor:")
lbl_autor.pack()

entry_autor = tk.Entry(janela)
entry_autor.pack()

btn_ok = tk.Button(janela, text="OK", command=gerar_xml)
btn_ok.pack()

lbl_resultado = tk.Label(janela, text="")
lbl_resultado.pack()

# Inicia o loop da interface
janela.mainloop()
