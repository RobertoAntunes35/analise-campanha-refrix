
import os 
import sys

import pandas as pd
import numpy as np 

from Libs import config, relatorio, vendedores, produtosAnalise

# Leitura e tratamento das importações

name_file_clientes = "D01_Cliente.xls"
name_file_pedidos = "Pedidos_Itens.xls"

if os.path.exists(config.file_path + name_file_pedidos) and os.path.exists(config.file_path + name_file_pedidos):
    file_clientes = pd.read_excel(config.file_path + name_file_clientes)
    file_pedidos = pd.read_excel(config.file_path + name_file_pedidos)

    print(file_clientes.head())
    print(file_pedidos.head())

else:
    sys.exit("Arquivos não encontrados.")

# Renomeando Colunas, caso necessário
rename_colum_pedido = {
    'Combinação22':'codigo_vendedor',
    'Texto28':'descricao_produto',
    'QUANT':'quantidade_venda',
    'Texto14':'nome_fantasia',
}

file_pedidos = file_pedidos.rename(columns=rename_colum_pedido)

newRelatorio = relatorio.RelatorioRefrix(file_clientes, file_pedidos, vendedores.vendedores)

newRelatorio.positivacoes(produtosAnalise.produtos)
newRelatorio.convertExcel(newRelatorio.dictGeral)