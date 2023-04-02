print('Calcule a Distância para Economizar...')
print(' ')
Distancia = float(input('Digite: Quantos Km você irá Percorer em sua viagem? '))
PrecoGasolina = float(input('Digite: Qual o valor da Gasolina? '))
AutonomiaGasolina = float(input('Digite: Qual a Autonomia da Gasolina? '))
PrecoEtanol = float(input('Digite: Qual o valor do Etanol? '))
AutonomiaEtanol = float(input('Digite: Qual a Autonomia do Etanol? '))

DistanciaGasolina = Distancia * PrecoGasolina
DistanciaEtanol = Distancia * PrecoEtanol

ConsumoGasolina = Distancia / AutonomiaGasolina * PrecoGasolina
ConsumoEtanol = Distancia / AutonomiaEtanol * PrecoEtanol

if ConsumoGasolina < ConsumoEtanol:
    menor = ConsumoGasolina

if ConsumoEtanol < ConsumoGasolina:
    menor = ConsumoEtanol


print(' ')
print('>>>>> Na viagem de {} Km, o Valor gasto utilizando Gasolina é: R$ {} reais.'.format(Distancia,  DistanciaGasolina))
print('>>>>> O consumo utilizando Gasolina com o valor de R$ {} reais, fazendo {} litros por Km é de R$ {} reais.'.format(PrecoGasolina, AutonomiaGasolina, ConsumoGasolina))
print('>>>>> Na viagem de {} Km, o valor gasto utilizando Etanol é de: R$ {} reais.'.format(Distancia, DistanciaEtanol))
print('>>>>> O consumo utilizando Etanol com  valor de R$ {} reais, fazendo {} litros por Km é de R$ {} reais.'.format(PrecoEtanol, AutonomiaEtanol, ConsumoEtanol))
print('Uhuuuu!!! O menor valor da viagem é: {} reais. Aproveite!'.format(menor))
