import random as random

from ACAO import ACAO
from ESTADO import ESTADO
from PERCEPCAO import PERCEPCAO

class Agente():

    def perceber(self, percepcao):
        if percepcao == ESTADO.SUJO_COM_AGENTE.value:
            return PERCEPCAO.SUJO
        elif percepcao == ESTADO.LIMPO_SEM_AGENTE.value:
            return PERCEPCAO.LIMPO


    def agir(self, percepcao):
        if percepcao == PERCEPCAO.SUJO:
            acao = ACAO.ASPIRAR
        else:
           acao = random.choice([ACAO.ESQUERDA.value, ACAO.DIREITA.value, ACAO.CIMA.value, ACAO.BAIXO.value]) 
        return acao
            
