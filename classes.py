from faker import Faker
import re
from tabela import *
from time import sleep
from caminho import *

class Dispositivos:
    def __init__(self, identificador, ip, mac):
        self.identificador = identificador
        self.ip = ip
        self.mac = mac

    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, ip):
        assert self.Validar_IP(ip) == True, "Ip Invalido, adicione um ip válido!"
        self.__ip = ip

    @property
    def mac(self):
        return self.__mac

    @mac.setter
    def mac(self, mac):
        assert self.Validar_MAC(mac) == True, 'MAC Inválido, adicione um MAC válido!'
        self.__mac = mac

    @property
    def identificador(self):
        return self.__identificador

    @identificador.setter
    def identificador(self, identificador):
        self.__identificador = identificador

    def Validar_IP(self,ip):
        regex = (r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
        p = re.compile(regex)
        if(re.search(p, ip)):
            return True
        else:
            return False

    def Validar_MAC(self, str):
        regex = ("^([0-9A-Fa-f]{2}[:-])" + "{5}([0-9A-Fa-f]{2})|" + "([0-9a-fA-F]{4}\\." + "[0-9a-fA-F]{4}\\." + "[0-9a-fA-F]{4})$")
        p = re.compile(regex)
        if(re.search(p, str)):
            return True
        else:
            return False

    def showRunning(self):
        print()
        print(f'Nome: {self.identificador}')
        print(f'IP: {self.ip}')
        print(f'MAC: {self.mac}')

    def __str__(self):
        return str(self.identificador)

    def __repr__(self):
        return str(self)

class Computador(Dispositivos):
    def __init__(self, identificador, ip, mac):
        super().__init__(identificador, ip, mac)
        self.tabela_arp = TabelaHash(30)

    @property
    def tabela_arp(self):
        return self.__tabela_arp

    @tabela_arp.setter
    def tabela_arp(self, tabela_arp):
        self.__tabela_arp = tabela_arp
    
    def adicionar_tabela_arp(self, ip, mac):
        assert self.Validar_MAC(mac) == True, 'MAC Inválido'
        assert self.tabela_arp.contains(ip) == False, 'IP já vinculado a um endereço MAC'
        return self.tabela_arp.put(ip, mac)
        
    def getMac(self, ip, grafo):
        if self.tabela_arp.contains(hash(ip)) == True:
            print(f'MAC: {self.tabela_arp.get(hash(ip))}')
            return 
        else:
            visitados, fila = set(), [self]
            while fila:
                vertice = fila.pop(0)
                print(f'Resposta de: {vertice.ip} bytes=32 Host: {vertice}')
                sleep(1)
                if hash(vertice.ip) == ip:
                    print(f'IP encontrado no {vertice}')
                    if self.tabela_arp.contains(hash(ip)) == False:
                        self.adicionar_tabela_arp(hash(ip), vertice.mac)
                    return
                visitados.add(vertice)
                for vizinho in grafo[vertice]:
                    if vizinho not in visitados:
                        visitados.add(vizinho)
                        fila.append(vizinho)
            print('IP não encontrado na rede :c')

    def __hash__(self):
        return hash(self.ip)

class Switch(Dispositivos):
    def __init__(self, identificador, ip, mac, qtd_portas=24):
        super().__init__(identificador, ip, mac)
        self.qtd_portas = qtd_portas
        self.tabela_roteamento = TabelaHash(60)
        self.porta_atual = 1

    @property
    def tabela_roteamento(self):
        return self.__tabela_roteamento

    @tabela_roteamento.setter
    def tabela_roteamento(self, tabela_roteamento):
        self.__tabela_roteamento = tabela_roteamento

    @property
    def qtd_portas(self):
        return self.__qtd_portas

    @qtd_portas.setter
    def qtd_portas(self, qtd_portas):
        assert qtd_portas in [4, 8, 16, 24], 'Porta Incorreta. Tente Novamente [4, 8, 16, 24]'
        self.__qtd_portas = qtd_portas

    def adicionar_tabela_roteamento(self, mac, porta=None):
        if porta is None:
            porta = self.porta_atual
            self.porta_atual += 1
        assert self.tabela_roteamento.contains(porta) == False, f'Porta {porta} já referenciada ao MAC: {self.tabela_roteamento.get(porta)}'
        assert len(self.tabela_roteamento) < self.qtd_portas, 'Portas do Switch Lotadas'
        if self.tabela_roteamento.verifica_mac_repetido(mac) == False:
            return self.tabela_roteamento.put(porta, mac)