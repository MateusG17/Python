print ('tempo do primeiro trecho: 8 min e 15 s')
minutoPrimeiroTrecho = 8 * 60
segundoPrimeiroTrecho = 15


print ('tempo do segundo trecho: 7min e 12seg')
minutoSegundoTrecho = (7 * 3) * 60
segundosSegundoTrecho = 12 * 3


print ('tempo do terceiro trecho: 8 min e 15 s')
minutoTerceiroTrecho = 8 * 60
segundoTerceiroTrecho = 15

# soma o total de minutos e converte todos os segundosve minutos
totalTempoTodosTrechosMinutos = (minutoPrimeiroTrecho + minutoSegundoTrecho + minutoTerceiroTrecho) / 60

#soma valor total em segundos
totalTempoTodosTrechosSegundos = (segundoPrimeiroTrecho + segundosSegundoTrecho + segundoTerceiroTrecho)


restanteMinutos = int(totalTempoTodosTrechosMinutos / 60)
restanteSegundos = totalTempoTodosTrechosSegundos % 60

totalMinutos = totalTempoTodosTrechosMinutos + restanteMinutos
totalSegundos = restanteSegundos

print('soma de tempo de todos os trechos: ', totalTempoTodosTrechosMinutos,
      'minutos')

print('soma de tempo de todos os trechos: ', totalTempoTodosTrechosSegundos,
      'segundos')

horainicialSegundos = (6 * 60) * 60
minutoInicialSegundos = 52 * 60
horarioInicialSegundos = horaInicialSegundos + minutoInicialSegundos

tempoTrechoMinutosSegundos = totalMinutos * 60

horaChegada = int(((horainicialSegundos + tempoTrechoMinutosSegundos) / 60) / 60)
minutoChegada = int(((minutoInicialSegundos + tempoTrechoMinutosSegundos)/60) % 60)


print('O tempo de chegada foi de:', horaChegada,':', minutoChegada, restanteSegundos)




