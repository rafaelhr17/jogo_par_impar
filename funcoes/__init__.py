def confere_input(lerint=False, lerstring=False, txt=''):
    """
    Confere o que o usuário digitou e verifica se bate com o tipo requisitado.
    :param lerint: Verifica se o usuário digitou números inteiros.
    :param lerstring: Verifica se o usuário digitou uma string válida.
    :param txt: Texto para informar ao usuário o que digitar.
    :return: Apenas retorna o valor que o usuário digitou caso tenha sido validado.
    """
    if lerint:
        while True:
            try:
                a = int(input(txt))
            except:
                print('Digite apenas números inteiros!')
            else:
                return a
    if lerstring:
        while True:
            try:
                b = input(txt).strip()
            except:
                print('ERRO! Tente novamente!')
            else:
                if b != '':
                    return b
                else:
                    print('ERRO! Tente novamente!')


def arquivoExiste(nome):
    """
    Verifica se o arquivo existe no mesmo diretório/ambiente.
    :param nome: Nome do arquivo passado em String (Deve ser passado a extensão do arquivo, ex: .txt).
    :return: Valor booleano conforme a verificação (Caso o arquivo exista, retornará True).
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    """
    Cria o arquivo com base no parâmetro passado.
    :param nome: Nome do arquivo passado em String (Deve ser passado a extensão do arquivo, ex: .txt).
    :return: Sem retorno.
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerPlacar(nome):
    """
    Printa o placar salvo no arquivo .txt, formatado como um placar de jogos.
    :param nome: Nome do arquivo passado em String (Deve ser passado a extensão do arquivo, ex: .txt).
    :return: Sem retorno.
    """
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        b = converterlst(nome)
        print('-' * 25)
        for item in b:
            print(f'| {item[0]:.<17}', end='')
            print(f'{item[1]:0>4} |')
        print('-' * 25)
    finally:
        a.close()


def placar(arq, player):
    """
    Salva no arquivo .txt o usuário que salvou sua pontuação.
    :param arq: Arquivo referente ao salvamento de pontuação.
    :param player: O nick e a pontuação do usuário.
    :return: Sem retorno.
    """
    try:
        a = open(arq, 'w')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{player}')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            a.close()


def converterlst(arq):
    """
    Converte todos os dados que foram escritos no arquivo, de Strings para uma lista.
    :param arq: Arquivo referente ao salvamento de pontuação.
    :return: Retorna os dados do arquivo do placar em uma lista.
    """
    lstbruta = []
    pqp = []
    player = []
    highscore = []
    lstbruta.append(open(arq, 'rt').readline())
    for item in lstbruta:
        b = item.replace('[', '')
        a = b.replace(']', '')
        pqp = a.replace("'", '').replace(' ', '').split(',')
    for k, i in enumerate(pqp):
        if i.isnumeric():
            pqp.insert(k, int(i))
            pqp.pop(k + 1)
    for k, i in enumerate(pqp):
        player.append(i)
        if k % 2 != 0:
            highscore.append(player[:])
            player.clear()
    return highscore


def mostralinha(linha, quant, alinhar,  texto):
    """
    Função que alinha títulos com linhas paralelas que acompanham o título.
    :param linha: O tipo de linha que o usuário deseja (ex. -, =, -=, >).
    :param quant: Quantidade de linha para acompanhar o título.
    :param alinhar: Alinhamento do título (esquerda, central, direita).
    :param texto: O que o usuário deseja por como título.
    :return: Sem retorno.
    """
    print(linha * quant)
    "Alinha -> esquerda, central(default/padrão), direita"
    if alinhar == 'esquerda':
        alinhar = '<'
    elif alinhar == 'direita':
        alinhar = '>'
    else:
        alinhar = '^'
    print(f'{texto:{alinhar}{quant*len(linha)}}')
    print(linha * quant)


def menu(arq):
    """
    Menu do jogo onde o usuário escolhe se deseja jogar, ver o placar ou sair do programa.
    :param arq: Arquivo referente ao salvamento de pontuação.
    :return: Retorna em um número inteiro a opção que o usuário escolheu.
    """
    while True:
        mostralinha('~', 30, 'central',
                    '\n\nJOGO DO PAR OU ÍMPAR!\n\n')
        print('[1] Jogar')
        print('[2] Ver placar')
        print('[3] Como Jogar')
        print('[4] Sair')
        while True:
            comando = confere_input(lerint=True, txt='Selecione > ')
            if comando == 1:
                print('Carregando', end='')
                for i in range(0, 3):
                    print('.', end='')
                print()
                return 1
            if comando == 2:
                print('Carregando placar', end='')
                for i in range(0, 3):
                    print('.', end='')
                print()
                lerPlacar(arq)
                r = confere_input(lerstring=True, txt='Deseja retornar ao menu? [S] para voltar > ')
                if r in 'Ss':
                    print('Retornando ao menu', end='')
                    for i in range(0, 3):
                        print('.', end='')
                    print()
                    break
                else:
                    return 4
            if comando == 3:
                print('Carregando placar', end='')
                for i in range(0, 3):
                    print('.', end='')
                print()
                mostralinha('-', 30, 'central', 'Como Jogar')
                print('Caso nunca tenha jogado par ou ímpar: No par ou ímpar, você e seu adversário primeiramente\n'
                      'escolhem qual o resultado que desejam no fim, se querem que o número final seja par ou ímpar.\n'
                      'após essa escolha, vocês escolhem quais números vão jogar, geralmente com os dedos entre 1 a 10,'
                      '\ne caso a soma do número que escolheu com o número do seu adversário der o que você escolheu'
                      '\ninicialmente (par ou ímpar), você ganha o jogo, caso contrário você perde.')
                print('-'*30)
                print('O que deve saber: leia com atenção e siga as instruções dadas, utilize apenas o teclado \n'
                      'e sempre pressione a tecla "Enter" caso tenha escolhido o comando requerido. Seu objetivo \n'
                      'é fazer o maxímo de pontos possíveis, e você ganha 1 ponto a cada rodada ganha, o jogo \n'
                      'continuará até você perder, e caso queira, poderá salvar sua pontuação ao criar um nickname \n'
                      '(apelido) de três caracteres que ficará salvo no placar junto da sua pontuação.\n'
                      'Caso queira jogar novamente, seus dados da rodada anterior serão apagados e você voltará \n'
                      'à estaca zero. Desafie-se a ultrapassar o seu recorde pessoal ou compita com seus amigos \n'
                      'para saber quem consegue ganhar mais pontos!')
                print('-' * 30)
                r = confere_input(lerstring=True, txt='Deseja retornar ao menu? [S] para voltar > ')
                if r in 'Ss':
                    print('Retornando ao menu', end='')
                    for i in range(0, 3):
                        print('.', end='')
                    print()
                    break
                else:
                    return 4
            if comando == 4:
                print('Saindo', end='')
                for i in range(0, 3):
                    print('.', end='')
                return 3
            else:
                print('Selecione as opções existentes!')

