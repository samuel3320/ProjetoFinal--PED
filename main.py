from classes import *
from caminho import *
import csv
from imports import *
import os

try:
    caminho = Grafo([], direcionado=False)

    for i, palavra in enumerate(lista_computadores):
        globals()['pc' + str(i)] = palavra

    for i, palavra in enumerate(lista_switches):
        globals()['sw' + str(i)] = palavra

    caminho.adiciona_arestas({((sw0, pc0))})
    caminho.adiciona_arestas({((sw0, pc1))})
    caminho.adiciona_arestas({((sw0, pc2))})
    caminho.adiciona_arestas({((sw0, pc3))})
    caminho.adiciona_arestas({((sw0, sw1))})
    caminho.adiciona_arestas({((sw2, sw3))})
    caminho.adiciona_arestas({((sw1, pc4))})
    caminho.adiciona_arestas({((sw1, pc5))})
    caminho.adiciona_arestas({((sw1, pc6))})
    caminho.adiciona_arestas({((sw1, pc7))})
    caminho.adiciona_arestas({((sw1, pc8))})
    print("Bem Vindo a Rede!")
    print()
    while True:
        print('''1. Verificar Tabela Arp
2. Verificar Tabela Roteamento
3. Verificar Caminhos
4. Verificar Configurações Gerais
5. Adicionar Arestas
6. GetMac
7. Encerrar o programa
        ''')
        n = int(input('Digite a sua opção: '))
        if n == 7:
            print()
            print("As configurações foram concluída com sucesso!")
            break

        elif n == 1:
            print(*lista_computadores)
            print('Selecione o seu computador: [inteiro - Ex: 0 = PC0] ')
            comp = int(input())
            print(lista_computadores[comp].identificador, lista_computadores[comp].tabela_arp)

        elif n == 2:
            print(*lista_switches)
            print('Selecione o seu switch: [inteiro - Ex: 0 = SW0] ')
            swi = int(input())
            assert swi < len(lista_switches), 'Digite opção correta'
            print(lista_switches[swi].tabela_roteamento)
            print()

        elif n == 3:
            print(caminho)
            print()

        elif n == 4:
            escolha = int(input('1 - Switches | 2 - PCS: '))
            assert escolha == 1 or escolha == 2, 'Digite opção correta'
            if escolha == 1:
                print(*lista_switches)
                swi = int(input('Selecione o seu switch: [inteiro - Ex: 0 = SW0] '))
                assert swi < len(lista_switches), 'Digite opção correta'
                lista_switches[swi].showRunning()
            elif escolha == 2:
                print(*lista_computadores)
                pcs = int(input('Selecione o seu computador: [inteiro - Ex: 0 = PC0] '))
                assert pcs < len(lista_computadores), 'Digite opção correta'
                lista_computadores[pcs].showRunning()

        elif n == 5:
            print(*lista_switches)
            swi = int(input('Selecione o seu switch: [inteiro - Ex: 0 = SW0] '))
            assert swi < len(lista_switches), 'Digite opção correta'
            escolha = input('SWITCH OU PC? [S/P] ').upper()
            assert escolha == 'S' or escolha == 'P', 'Digite S ou P na escolha'
            if escolha == 'P':
                print(*lista_computadores)
                pcs = int(input('Selecione o seu computador: [inteiro - Ex: 0 = PC0] '))
                assert pcs < len(lista_computadores), 'Digite opção correta'
                caminho.adiciona_arestas({(lista_switches[swi], lista_computadores[pcs])})
            else:
                print(*lista_switches)
                swi1 = int(input('Selecione o seu switch: [inteiro - Ex: 0 = SW0] '))
                assert swi1 < len(lista_switches), 'Digite opção correta'
                caminho.adiciona_arestas({(lista_switches[swi], lista_switches[swi1])})
            
        elif n == 6:
            ip = input('Digite um IP para procura: ')
            print(*lista_computadores)
            partida = int(input('Selecione o computador de partida: [inteiro - Ex: 0 = PC0] '))
            assert partida < len(lista_computadores), 'Digite opção correta'
            lista_computadores[partida].getMac(hash(ip), caminho)
            print()

except AssertionError as erro:
    print(erro)
except:
    print('Erro na execução :c')