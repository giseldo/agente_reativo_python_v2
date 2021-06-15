from Ambiente import Ambiente
from Agente import Agente

# cria um agente
agente=Agente()
# cria um tabuleiro com dimensões AxB
ambiente=Ambiente(3,3)
# coloca o agente no ambiente na posição AxB
ambiente.setAgente(1,1) # TODO: adicionar ele randomicamente no tabuleiro


for line in ambiente.tabuleiro:
    print (' | '.join(map(str, line)))


for i in range (10):
    EstadoQuadradoAgente = ambiente.getEstadoQuadradoAgente()
    percepcao = agente.perceber(EstadoQuadradoAgente) 
    acao = agente.agir(percepcao)
    ambiente.mudar(acao)
    print(ambiente.tabuleiro)
    



    
