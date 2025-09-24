from random import randint
from funcoes import *
'''
# Pra fazer:
1º Colocar no Github
2º Opção no menu "Como jogar"
3º interface
'''
vc = pc = par = imp = vitconsec = vit = 0
highscore = []
arq = 'placar.txt'
# Verificando se o arquivo existe e, caso exista, convertendo os dados do arquivo para a lista highscore
if not arquivoExiste(arq):
    criarArquivo(arq)
if arquivoExiste(arq) and open(arq, 'r').readline() != '':
    highscore.clear()
    highscore = converterlst(arq)
try:
    while True:
        comando = menu(arq)
        if comando == 1:
            while True:
                if len(highscore) > 0:
                    if vitconsec > highscore[0][1]:
                        print(f'Parabéns!!! Você Ultrapassou o recorde atual'
                              f' por {vitconsec - highscore[0][1]} ponto(s)!')
                mostralinha('-', 30, 'central', 'Par ou Ímpar?')
                print('[0] para par\n[1] para ímpar')
                print('-' * 30)
                while True:
                    vc = confere_input(lerint=True, txt='Faça sua escolha: ')
                    if vc < 0 or vc > 1:
                        print('Escolha Par [0] ou Ímpar [1]')
                    else:
                        break
                # Caso o usuário tenha escolhido Par.
                if vc == 0:
                    print('Você escolheu Par!')
                    while True:
                        par = confere_input(lerint=True, txt='Escolha o número de 1 a 10: ')
                        if par < 1 or par > 10:
                            print('Número inválido!')
                        else:
                            break
                    pc = randint(1, 10)
                    soma = par + pc
                    if soma % 2 == 0:
                        mostralinha('*.', 30, 'esquerda',
                                    f'Resultado: Você {par} - PC {pc} -> Par, você ganhou!')
                        vitconsec += 1
                        vit = 1
                    else:
                        mostralinha('*.', 30, 'esquerda',
                                    f'Resultado: Você {par} - PC {pc} -> Ímpar, você perdeu!\n'
                                    f'Vitórias consecutivas até perder: {vitconsec}')
                        vit = 0
                # Caso o usuário tenha escolhido Ímpar.
                elif vc == 1:
                    print('Você escolheu Ímpar!')
                    while True:
                        imp = confere_input(lerint=True, txt='Escolha o número de 1 a 10: ')
                        if imp < 1 or imp > 10:
                            print('Número inválido!')
                        else:
                            break
                    pc = randint(1, 10)
                    soma = imp + pc
                    if soma % 2 != 0:
                        mostralinha('*.', 30, 'esquerda',
                                    f'Resultado: Você {imp} - PC {pc} -> Ímpar, você ganhou!')
                        vitconsec += 1
                        vit = 1
                    else:
                        mostralinha('*.', 30, 'esquerda',
                                    f'Resultado: Você {imp} - PC {pc} -> Par, você perdeu!\n'
                                    f'Vitórias consecutivas até perder: {vitconsec}')
                        vit = 0

                if vit == 0:
                    while True:
                        while True:
                            # Decisão do usuário de salvar sua pontuação no placar.
                            r = confere_input(lerstring=True,
                                              txt='Deseja salvar sua pontuação? [S/N]: ')
                            if r.strip().upper()[0] not in 'SN':
                                print('ERRO! Digite apenas S ou N.')
                            else:
                                break
                        if r.strip().upper()[0] in 'N':
                            if vit == 0:
                                vitconsec = 0
                            break
                        else:
                            while True:
                                # Salvando a pontuação do usuário. Só ficará salvo 10 pontuações.
                                player = []
                                nick = confere_input(lerstring=True, txt='Digite o seu nickname (3 dígitos): ').upper()
                                used = 0
                                if len(highscore) > 0:
                                    for i in highscore:
                                        if nick.strip().upper()[:3] in i[0]:
                                            used += 1
                                            print('Este nickname já foi utilizado, escolha outro!')
                                    if used == 0:
                                        break
                                else:
                                    break
                            score = vitconsec
                            player.append(nick)
                            player.append(score)
                            # Inserindo a pontuação atual do usuário com base no placar.
                            if len(highscore) > 0:
                                for k, i in enumerate(highscore):
                                    if i[1] <= player[1]:
                                        highscore.insert(k, player[:])
                                        break
                                for item in highscore:
                                    if nick in item[0]:
                                        used += 1
                                if used == 0:
                                    highscore.append(player[:])
                            else:
                                highscore.append(player[:])
                            if len(highscore) > 10:
                                highscore.pop()
                            print('Pontuação Salva.')
                            placar(arq, highscore)
                            vitconsec = 0
                        lerPlacar(arq)
                        break

                if vitconsec == 0:
                    res = confere_input(lerstring=True, txt='Deseja Jogar novamente? [S] para continuar: ')
                    if res not in 'Ss':
                        break

        elif comando == 3:
            break

except (ValueError, TypeError, KeyboardInterrupt):
    print('\nHouve um problema, por favor rode novamente e siga o programa corretamente!')
except Exception as erro:
    print(f'\nErro do tipo: {erro.__class__}, o Erro foi: {erro.__cause__}')
