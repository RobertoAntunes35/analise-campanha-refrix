import os 
import sys

# Diretório Absoluto
caminho_absoluto = os.path.abspath(__file__)
print(caminho_absoluto)

# Diretório Pai
diretorio_pai = os.path.dirname(os.path.dirname(caminho_absoluto))
print(diretorio_pai)

# Pasta de Arquivos
nome_arquivo = "static-files/"

# Arquivo Final
file_path = os.path.join(diretorio_pai, nome_arquivo)