class Libro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

class Usuario:
    def __init__(self, nombre: str):
        self.nombre = nombre

class Biblioteca:
    def __init__(self, libros: list = None):  
        self.libros: list = libros or []

    def agregar_libro(self, libro: Libro) -> None:
        self.libros.append(libro)
    
    def quitar_libro(self, titulo: str) -> bool:
        for i, b in enumerate(self.libros):
            if b.titulo == titulo:
                del self.libros[i]
                return True
        return False
