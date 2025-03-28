import numpy as np
import matplotlib.pyplot as fig
from matplotlib import animation, cm
import random

fig.close('all')

n = 80  #numero de linhas
m = 80  #numero de colunas

a = np.zeros((n+1,m+1))
novo_a = np.zeros((n+1,m+1))

# a[4,1] = 1
# a[4,2] = 1
# a[6,2] = 1
# a[5,3] = 1
# a[5,4] = 1
# a[4,5] = 1
# a[6,5] = 1
# a[6,1] = 1
# a[5,6] = 1

#automato que entra em loop de 3 sqs girando, parece um reator no começo
#mas esta cortado pelo tamanho da tela e disposiçao das celulas iniciais
a[10,1] = 1
a[10,2] = 1
a[10,3] = 1
a[11,3] = 1
a[11,4] = 1
a[7,5] = 1
a[6,5] = 1
a[6,4] = 1
a[6,7] = 1
a[7,6] = 1
a[7,7] = 1
a[7,8] = 1
a[8,8] = 1

# a[15,1] = 1      #GLIDER
# a[13,2] = 1
# a[15,2] = 1
# a[14,3] = 1
# a[15,3] = 1

# a[2,10] = 1         #SpaceShip
# a[4,10] = 1
# a[3,10] = 1
# a[1,11] = 1
# a[4,11] = 1
# a[4,12] = 1
# a[4,13] = 1
# a[1,14] = 1
# a[3,14] = 1


for ger in range(50):            # iteração das gerações
    for i in range(1,n):        # percorre linhas
        for j in range(1,m):    # percorre colunas
            vizinho = 0

            if a[i-1, j-1] == 1:    #verifica os qnt de vizinhos
                vizinho += 1

            if a[i, j-1] == 1:
                vizinho += 1

            if a[i+1, j-1] == 1:
                vizinho += 1

            if a[i+1, j] == 1:
                vizinho += 1

            if a[i+1, j+1] == 1:
                vizinho += 1

            if a[i, j+1] == 1:
                vizinho += 1

            if a[i-1, j+1] == 1:
                vizinho += 1

            if a[i-1, j] == 1:
                vizinho += 1

            #verifica a quantidade de vizinhos e se vai nascer/morrer/manter
            if a[i,j] == 1:
                if (vizinho == 2) or (vizinho ==3):
                    novo_a[i,j] = 1
                else:
                    novo_a[i,j] = 0
            else:
                if vizinho == 3:
                    novo_a[i,j] = 1
                else:
                    novo_a[i,j] = 0

    a = novo_a
    novo_a = np.zeros((n+1,m+1))

    fig.title('GERAÇÃO %d' % ger, fontsize = 20)
    fig.xticks([])      #esconde o numeros do eixo x
    fig.yticks([])      #
    im = fig.imshow(a, interpolation = "nearest", cmap = 'Greys', animated = True)
    mgr = fig.get_current_fig_manager()
    mgr.window.setGeometry = (20,20,1000, 1000) #janela fixa
    fig.pause(0.1)      #pausa para ver as celulas se mover
            