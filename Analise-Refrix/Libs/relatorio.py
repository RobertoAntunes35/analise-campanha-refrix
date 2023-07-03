import pandas as pd
from collections import defaultdict


class RelatorioRefrix:
    def __init__(self, file_cliente, file_pedidos, vendedores) -> None:
        self.file_cliente = file_cliente
        self.file_pedidos = file_pedidos
        self.vendedores = vendedores

    def positivacoes(self, items: set) -> dict:
        self.items = items 

        if isinstance(self.items, set):
            self.dictGeral = defaultdict(dict)
            for vendedor, grupo in self.file_pedidos.groupby('codigo_vendedor'):
                produtosAnalise = dict()
                for produto in self.items:
                    # Quantidade de Venda
                    quantidadeVenda = grupo.loc[grupo['descricao_produto'] == produto]['quantidade_venda'].sum()
                    # Clientes Positivados
                    positivacao = grupo.loc[grupo['descricao_produto'] == produto]['nome_fantasia'].nunique()
                    produtosAnalise[produto] = (positivacao,quantidadeVenda)
                self.dictGeral[vendedor] = produtosAnalise
            return self.dictGeral
    
    def convertExcel(self, file):
        df = pd.DataFrame(file)
        df.to_excel('CampanhaRefrix.xlsx')

                
            
