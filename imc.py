print('////////////////////////////////////////////////////////////// \n')

nome = input('Insira seu nome:  ').upper()
sexo = input('Insira seu Sexo/F- Feminino /M- Masculino:  ').upper()
altura = float(input('Insira sua altura em M (metros):  '))
peso = float(input('Insira seu peso atual:  '))

print('\n//////////////////////////////////////////////////////////////')

imc = peso / (altura * altura)

print('\n', ' Seu Indice de Massa Corporal : ', imc, ' IMC', '\n')

fem = 'Até 19,1 | Abaixo do peso\n19,1 a 26,8 | Peso ideal\n25,9 a 27,3 | Pouco acima do peso\n27,4 a 32,3 | Acima do peso\n32,4 e acima | Obesidade '
masc = 'Até 20,7 | Abaixo do peso\n20,7 a 26,4 | Peso ideal\n26,5 a 27,8 | Pouco acima do peso\n27,9 a 31,3 | Acima do peso\n31,1 e acima | Obesidade '

dieta = [
    [  # 0
        'Para ter um ganho de peso saudável:',
        [  # 1           
            'Alimente-se de 3 em 3 horas',
            'Alimentos ricos em proteína (frango, peixe, ovos, etc.) ',
            'Aumente o consumo de pães, bolos, massas, mandioca, batata, milho e cereais (arroz, farinha de trigo, fubá, aveia), lembrando sempre de optar pelas versões integrais.',
            'Coma amendoim, nozes, amêndoa, avelã, castanhas, azeite de oliva, linhaça e abacate.',
            'Beba uma boa quantidade de água durante o dia, no mínimo 7 a 8 copos. ',
        ]
    ],
    [  # 0
        'Para ter uma perda de peso:',
        [  # 1
            'Alimente-se de 3 em 3 horas',
            'Busque carnes magras (carnes brancas como peixe e frango) ',
            'Reduza o consumo de pães, bolos, massas, mandioca, batata, milho e cereais (arroz, farinha de trigo, fubá, aveia), lembrando sempre de optar pelas versões integrais.',
            'Beba uma boa quantidade de água durante o dia, no mínimo 10 a 13 copos.',
        ]
    ],
]

exercicio = [
    [  # 0
        'Para Ganhar Massa: ',
        [  # 1
            'Agachamento ',
            'Flexão de braço',
            'Afundo',
            'Abdominal ',
            'Panturrilha em pé',
        ]
    ],
    [  # 0
        'Para Perder Massa: ',
        [  # 1
            'Caminhar',
            'Pular Corda',
            'Agachamento',
            'Abdominal',
            'Polichinelo',
        ]
    ],
]

def GetIMCName(sex, imc):
    if sex == 'F':
        print(fem)
        if imc < 19.1:
            return 'Abaixo do peso'
        elif imc > 19.1 and imc < 25.8:
            return 'Peso ideal'
        elif imc > 25.9 and imc < 27.3:
            return 'Pouco acima do peso'
        elif imc > 27.4 and imc < 32.3:
            return 'Acima do peso'
        else:
            return 'Obesidade'
    elif sex == 'M':
        print(masc)
        if imc < 20.7:
            return 'Abaixo do peso'
        elif imc > 20.7 and imc < 26.4:
            return 'Peso ideal'
        elif imc > 26.5 and imc < 27.8:
            return 'Pouco acima do peso'
        elif imc > 27.9 and imc < 31.1:
            return 'Acima do peso'
        else:
            return 'Obesidade'

print(f" \n A sua categoria é: {GetIMCName(sexo, imc)} \n")

while(True):
    print('////////////////////////////////////////////////////////////// \n')
    print('\n- Proxima area :')
    print('1- Dietas')
    print('2- Exercícios ')
    decisao = int(input('Selecione uma opção: '))
    print('////////////////////////////////////////////////////////////// \n')

    list_index = -1

    if decisao == 1:
        if fem:
            if imc <= 19.1:
                for x in range(len(dieta[0][1])):
                    print(f"{x} - {dieta[0][1][x]}")

                list_index = 0
            elif imc > 19.1 and imc < 25.8:
                print('Você está no peso ideal !!! ')
                break
                
            elif imc >= 25.8:
                for x in range(len(dieta[1][1])):
                    print(f"{x} - {dieta[1][1][x]}")
                
                list_index = 1
            else:
                print('error')
        elif masc:
            if imc <= 20.7:
                for x in range(len(dieta[0][1])):
                    print(f"{x} - {dieta[0][1][x]}")
                list_index = 0
            elif imc > 20.7 and imc < 26.4:
                print('você está no peso ideal !!! ')
                break
            elif imc >= 26.4:
                for x in range(len(dieta[1][1])):
                    print(f"{x} - {dieta[1][1][x]}")
                list_index = 1
            else:
                print('error')
        else:
            print('error ')

        alterar = input('Deseja alterar algo na Dieta? S- Sim / N- Não  ').upper()

        if alterar == 'S' or alterar == 'SIM':
            print('-------------')
            lista_alterar=input("Digite 'remover' para remover um item da dieta e 'adicionar' para adicionar um item na dieta?: ").lower()
            if lista_alterar == 'adicionar':
                lista_adicionar = input('Informe a sua dica: ')

                print(f"Você adicionou a dica: {lista_adicionar} à sua dieta!")
                dieta[list_index][1].append(lista_adicionar)
            elif lista_alterar == 'remover':
                lista_remover = int(input('Informe o índice do item que você deseja remover: '))

                print(f"Você removeu o item: {dieta[list_index][1][lista_remover]}\n")
                dieta[list_index][1].pop(lista_remover)
            else:
                print('ERROR')
        else:
            print('Obrigado!')

        voltar = input("Deseja voltar ao menu inicial? (S ou N): ").upper()
        if voltar == 'N':
            break       

    elif decisao == 2:
        if fem:
            if imc <= 19.1:
                list_index = 0
                for x in range(len(exercicio[0][1])):
                    print(x,'-',exercicio[0][1][x])
            elif imc > 19.1 and imc < 25.8:
                print('você está no peso ideal !!! ')
                break
            elif imc >= 25.8:
                list_index = 1
                for x in range(len(exercicio[1][1])):
                    print(x,'-',exercicio[1][1][x])
            else:
                print('error')
        elif masc:
            if imc <= 20.7:
                list_index = 0
                for x in range(len(exercicio[0][1])):
                    print(x,'-',exercicio[0][1][x])
            elif imc > 20.7 and imc < 26.4:
                print('você está no peso ideal !!! ')
                break
            elif imc >= 26.4:
                list_index = 1
                for x in range(len(exercicio[1][1])):
                    print(x,'-',exercicio[1][1][x])
            else:
                print('ERROR')

        
        alterar = input('Deseja alterar algo nos exercicios? S- Sim / N- Não  ').upper()

        if alterar == 'S' or alterar == 'SIM':
            print('-------------')
            lista_alterar = input("Digite 'remover' para remover um item dos exercicios e 'adicionar' para adicionar um item nos exercicios: ").lower()

            if lista_alterar == 'adicionar':
              lista_adicionar = input('Informe o seu exercicio: ')
              print(f"Você adicionou a dica: {lista_adicionar} ao seus exercicios!")
              exercicio[list_index][1].append(lista_adicionar)
          
            elif lista_alterar == 'remover':
              lista_remover = int(input('Informe o índice do item que você deseja remover: '))

              print(f"Você removeu o item: {exercicio[list_index][1][lista_remover]}\n")
              exercicio[list_index][1].pop(lista_remover)
            else:
              print('ERROR')

        elif alterar == 'N' or alterar == 'Nao' or alterar == 'Não':
          print('Obrigado!')
          break      

        voltar = input("Deseja voltar ao menu inicial? (S ou N): ").upper()
        if voltar == 'N':
            break 
