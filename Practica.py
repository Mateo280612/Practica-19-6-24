class Day:
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return f'Nombre: {self.name}'

day_1 = Day('Lunes')
day_2 = Day('Martes')
day_3 = Day('Miercoles')

day_1.next = day_2
day_2.next = day_3
day_3.next = None
secuencia = day_1

while secuencia is not None:
    print(secuencia, end = '-> ' if secuencia.next is not None else '\n')
    secuencia = secuencia.next

class Node:
    def __init__(self,data= None):
        self.data = data
        self.next = None  #Atributo Estático

node_1 = Node('Lunes')
node_2 = Node ('Martes')


class SingleList:
    def __init__(self):
        self.head = None
    
    def append_final(self,data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    
    def append_inicio(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def Remove_last(self):
        if not self.head:
            print('La lista esta vacia')
            return
    
        if not self.head.next:
            self.head = None
            return
    
        current = self.head

        while current.next.next:
            current = current.next
        
        current.next = None
    def show(self):
        current = self.head
        while current is not None:
            print(current.data, end = '-> ' if current.next is not None else '\n')
            current = current.next

lista_1 = SingleList()

lista_1.append_final('Martes')
lista_1.show()
lista_1.append_final('Miercoles')
lista_1.show()
lista_1.append_inicio('Lunes')
lista_1.Remove_last()
lista_1.show()
