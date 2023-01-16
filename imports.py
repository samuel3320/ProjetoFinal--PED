import csv
from classes import Computador, Switch

lista_computadores = []
with open('ProjetoFinal-PED/dispositivos.csv', 'r') as computadores:
        comp = computadores.readlines()
        for c in comp[1:]:
            if 'computador' in c:
                comp_atual = c.split(',')
                comp_atual = comp_atual[1:]
                lista_computadores.append(Computador(*comp_atual))

lista_switches = []
with open('ProjetoFinal-PED/dispositivos.csv', 'r') as switches:
        switch = switches.readlines()
        for s in switch[1:]:
            if 'switch' in s:
                switch_atual = s.split(',')
                switch_atual = switch_atual[1:]
                lista_switches.append(Switch(*switch_atual))