class AbsentKeyException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class Entry:
    """Uma classe privada utilizada para encapsular os pares chave/valor"""
    __slots__ = ( "key", "value" )
    def __init__( self, entryKey, entryValue ):
        self.key = entryKey
        self.value = entryValue
        
    def __str__(self):
        return f"{self.key}: {self.value}"
 
class TabelaHash:
    def __init__(self, size=10):
        self.size = size
        self.table = list([] for i in range(self.size))

    def hash(self, key):
        ''' Método que retorna a posição na tabela hashing conforme a chave.
            Aplicação do cálculo do hash modular
        '''
        return key % self.size

    def put(self, key, data):
        '''
        Adiciona um par chave/valor à tabela hash
        '''
        slot = self.hash(key)
        for entry in self.table[slot]:
            if key == entry.key:
                print(f'{key} já se encontra na tabela')
                return slot
        self.table[slot].append(Entry(key,data))
        return slot
    
    def verifica_mac_repetido(self, mac):
        '''
        Se algum endereço mac já referenciado a outra porta, ele não insere na tabela
        '''
        for i in self.table:
            if len(i) > 0 and i[0].value == mac:
                return True
        return False


    def get(self, key):
        '''
        Obtem o valor armazenado na entrada referente à chave "key"
        '''
        slot = self.hash(key)
        #print(f'key {key} at slot {slot}')
        for i in range(len(self.table[slot])):
            if key == self.table[slot][i].key:
                return self.table[slot][i].value
        else:
            raise AbsentKeyException(f'Chave {key} inexistente na tabela hash')

   
    def __str__(self):
        info = ""
        for items in self.table:
            # examina se o slot da tabela hash tem um list com elementos
            if items == None:
                continue
            for entry in items:
                info += str(entry)
        return info

    def __len__(self):
        count = 0
        for i in self.table:
            count += len(i)
        return count
         
    def keys(self):
        """Retorna uma lista com as chaves armazenadas na hashTable.
        """
        result = []
        for lst in self.table:
            if lst != None:
                for entry in lst:
                    result.append( entry.key )
        return result

    def contains( self, key ):
        """Return True se somente se a tabela hash tem uma entrada com a chave passada
           como argumento.
        """
        entry = self.__locate(key)
        return isinstance(entry, Entry)


    def __locate(self, key):
        '''
        Método que verifica se uma chave está presente na tabela hash e devolve a
        entrada correspondente quando a busca é realizada com sucesso
        '''
        slot = self.hash(key)
        for i in range(len(self.table[slot])):
            if key == self.table[slot][i].key:
                return self.table[slot][i]
        else:
            return None
          
    def remove(self, key):
        '''
        Método que remove a entrada correspondente à chave passada como argumento
        '''
        slot = self.hash(key)
        for i in range(len(self.table[slot])):
            if key == self.table[slot][i].key:
                entry = self.table[slot][i]
                del self.table[slot][i]
                return entry
        raise AbsentKeyException(f'Chave {key} não está presente na tabela hash') 


    def displayTable(self):
        entrada = -1
        for items in self.table:
            entrada += 1
            print(f'Entrada {entrada:2d}: ', end='') 
            if len(items) == 0:
                print(' None')
                continue
            for entry in items:
                print(f'[ {entry.key},{entry.value} ] ',end='')
            print()