def idadeJogador(idade):
    if idade < 5:
        print('Não tem idade ')
    elif 5 <= idade <= 7:
        print('Esta no infantil A ')
    elif 8 <= idade <= 10:
        print('Esta no infantil B ')
    elif 11 <= idade <= 13:
        print('Esta no Juvenil A ')
    elif 14 <= idade <= 17:
        print('Esta no Juvenil B ')

idade = int(input('Digite sua Idade: '))

idadeJogador(idade)
