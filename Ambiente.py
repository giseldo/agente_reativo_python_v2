from ACAO import ACAO
from ESTADO import ESTADO
import random as random

class Ambiente():
    
    tabuleiro = []
    
    def __init__(self, linha_max, coluna_max):
        matriz = [] 
        for i in range(linha_max):
            linha = [] 
            for j in range(coluna_max):
                linha.append(random.choice([ESTADO.SUJO_SEM_AGENTE.value, ESTADO.LIMPO_SEM_AGENTE.value]))
            matriz.append(linha)
        self.tabuleiro = matriz

    # coloca o agente no ambiente
    # o ambiente enxerga quem está no ambiente, sujeiro, limpo ou o agente
    def setAgente(self, posx_agente, posy_agente):
        if self.tabuleiro[posx_agente][posy_agente] == ESTADO.SUJO_SEM_AGENTE.value:
            self.tabuleiro[posx_agente][posy_agente] = ESTADO.SUJO_COM_AGENTE.value
        elif self.tabuleiro[posx_agente][posy_agente] == ESTADO.LIMPO_SEM_AGENTE.value:
            self.tabuleiro[posx_agente][posy_agente] = ESTADO.LIMPO_COM_AGENTE.value
   
    def getEstadoQuadradoAgente(self):
        
        matriz = self.tabuleiro
        linhas = len(matriz)
        colunas = len(matriz[0])

        for i in range(linhas):
            for j in range(colunas):
                if self.tabuleiro[i][j] == ESTADO.SUJO_COM_AGENTE.value:
                    return ESTADO.SUJO_COM_AGENTE.value
                elif self.tabuleiro[i][j] == ESTADO.LIMPO_COM_AGENTE.value:
                    return ESTADO.LIMPO_COM_AGENTE.value
        
        return "NÃO ENCONTREI NADA"

    ## TODO Rever o nome dessa função
    def mudar(self, acao):

        Posx_Agente = -1
        Posy_Agente = -1

        # código para retornar a posição do agente
        # TODO Refatorar para um método getPosicaoAgente
        matriz = self.tabuleiro
        linhas = len(matriz)
        colunas = len(matriz[0])
        for i in range(linhas):
            for j in range(colunas):
                if (self.tabuleiro[i][j] == ESTADO.SUJO_COM_AGENTE.value or self.tabuleiro[i][j] == ESTADO.LIMPO_COM_AGENTE.value):
                   Posx_Agente = i 
                   Posy_Agente = j

        ### AGENTE REATIVO
        if acao == ACAO.ASPIRAR:
            self.tabuleiro[Posx_Agente][Posy_Agente] = ESTADO.LIMPO_COM_AGENTE.value

        


   