import tkinter as tk
from datetime import date
import xml.etree.ElementTree as ET
import os

def gerar_xml():
    desenvolvedor = entry_desenvolvedor.get() or "desenvolvedor"  # Obtém o texto do campo de entrada ou define como "desenvolvedor" se estiver vazio
    hoje = date.today().strftime("%Y-%m-%d")
    
    # Criação dos elementos XML
    raiz = ET.Element("root")
    comentario = ET.Comment(" {}".format(desenvolvedor))
    raiz.append(comentario)
    data = ET.SubElement(raiz, "data")
    data.text = hoje
    
    # Cria o objeto ElementTree
    tree = ET.ElementTree(raiz)
    
    # Gera a string XML
    xml_string = '<?xml version="1.0" encoding="utf-8"?>\n' + ET.tostring(raiz, encoding="utf-8").decode()
    
    # Obtém o diretório atual onde o script está sendo executado
    diretorio_atual = os.getcwd()
    
    # Define o caminho para a pasta RPA
    caminho_rpa = os.path.join(diretorio_atual, "RPA")
    
    # Cria a pasta RPA se ela ainda não existir
    if not os.path.exists(caminho_rpa):
        os.mkdir(caminho_rpa)
    
    # Define o caminho para a pasta Documentos dentro de RPA
    caminho_documentos = os.path.join(caminho_rpa, "Documentos")
    
    # Cria a pasta Documentos se ela ainda não existir
    if not os.path.exists(caminho_documentos):
        os.mkdir(caminho_documentos)
    
    # Define o caminho para a pasta Config dentro de RPA
    caminho_config = os.path.join(caminho_rpa, "Config")
    
    # Cria a pasta Config se ela ainda não existir
    if not os.path.exists(caminho_config):
        os.mkdir(caminho_config)
    
    # Define o caminho completo para o arquivo XML de configuração
    caminho_xml = os.path.join(caminho_config, "config.xml")
    
    # Salva o XML no caminho correto
    with open(caminho_xml, "w") as xml_file:
        xml_file.write(xml_string)
    
    # Exibe uma mensagem de sucesso
    lbl_resultado.config(text="XML gerado com sucesso!")

# Cria a janela principal
janela = tk.Tk()
janela.title("Gerador de XML")

# Cria os elementos da interface
lbl_desenvolvedor = tk.Label(janela, text="Desenvolvedor:")
lbl_desenvolvedor.pack()

entry_desenvolvedor = tk.Entry(janela)
entry_desenvolvedor.pack()

btn_ok = tk.Button(janela, text="OK", command=gerar_xml)
btn_ok.pack()

lbl_resultado = tk.Label(janela, text="")
lbl_resultado.pack()

# Inicia o loop da interface
janela.mainloop()
