import matplotlib.pyplot as plt 
import math as math

giro = int(math.degrees((2*math.pi) + (math.pi/180)))
# lista vazia de t
tempo = []

# A lista fazia que dps vai conter os resultados dos senos, é a nossa f(x)
eixo_y = []

# Nosso primeiro angulo, zero
x = 0


# Um for pra calcular os senos, ai eu botei 361, pra ir ate 360. Mas to na duvida se o valor do angulo tem que ser em radiano.
for t in range(0, 61):
    tempo.append(t)

# ta de 6 em 6 que é pra cada valor de tempo ter um valor de seno
for x in range(0, giro, 6):
    y = int(math.sin(x))
    # Add os resultados dos senos na lista
    eixo_y.append(y)

# Fazendo o gráfico

    plt.figure()

    plt.plot(tempo, eixo_y, "-k")

    plt.title ("Grafico_SENO")
    plt.xlabel("Tempo")
    plt.ylabel("Resultados_SENO")

    plt.savefig("fig/grafico.gif")

    plt.close()

# Ainda não rodei, se vc tiver com o jupyter, tenta rodar pra ver como ta, acho que o grafico ta sobrescrevendo, pq falta uma parte, essa aqui

# plt.savefig("fig/bubble-it-{}.png".format(A))
# A = A+1

