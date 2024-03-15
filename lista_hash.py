from nodo import Nodo

class ListaHash:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.size = 0
        
    def listavacia(self):
        if self.cabeza == None:
            return True
        else:    
            return False
    
    def insertar(self, codigo, nombre):
        elementoInsertar = Nodo(codigo, nombre)
        if self.listavacia():
            self.cabeza = self.ultimo = elementoInsertar
        else:
            self.ultimo.siguiente = elementoInsertar
            self.ultimo = elementoInsertar
        self.size += 1
    
    def buscar_por_nombre(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente
        return None

    def eliminar_por_nombre(self, nombre):
        actual = self.cabeza
        previo = None
        while actual:
            if actual.nombre == nombre:
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            previo, actual = actual, actual.siguiente
        return False

    def recorrer(self):
        aux = self.cabeza  
        resultado = []
        while aux:
            resultado.append(f'{aux.codigo} -> {aux.nombre}')
            aux = aux.siguiente
        return ' / '.join(resultado)

    def funcion_hash(self, codigo):
        return codigo // 5