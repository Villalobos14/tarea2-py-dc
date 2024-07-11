class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

class Estudiante(Persona):
    estudiantes = 0
    def __init__(self, nombre, apellido, edad, matricula):
        super().__init__(nombre, apellido, edad)
        self.matricula = matricula
        self.cursos = []
        Estudiante.estudiantes += 1

    @classmethod
    def contar_estudiantes(cls):
        return cls.estudiantes

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def eliminar_curso(self, curso):
        if curso in self.cursos:
            self.cursos.remove(curso)

class Profesor(Persona):
    profesores = 0
    def __init__(self, nombre, apellido, edad, departamento):
        super().__init__(nombre, apellido, edad)
        self.departamento = departamento
        self.asignaturas = []
        Profesor.profesores += 1

    @classmethod
    def contar_profesores(cls):
        return cls.profesores

class Curso:
    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor

class SistemaGestion:
    def __init__(self):
        self.estudiantes = []
        self.profesores = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def eliminar_estudiante(self, estudiante):
        if estudiante in self.estudiantes:
            self.estudiantes.remove(estudiante)

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)

    def eliminar_profesor(self, profesor):
        if profesor in self.profesores:
            self.profesores.remove(profesor)

    def contar_estudiantes(self):
        return Estudiante.contar_estudiantes()

    def contar_profesores(self):
        return Profesor.contar_profesores()

def menu():
    sistema = SistemaGestion()
    
    while True:
        print("\n--- Menú de Gestión de Estudiantes ---")
        print("1. Agregar estudiante")
        print("2. Eliminar estudiante")
        print("3. Agregar profesor")
        print("4. Eliminar profesor")
        print("5. Contar estudiantes")
        print("6. Contar profesores")
        print("7. Agregar curso a estudiante")
        print("8. Eliminar curso de estudiante")
        print("9. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = int(input("Edad: "))
            matricula = input("Matrícula: ")
            estudiante = Estudiante(nombre, apellido, edad, matricula)
            sistema.agregar_estudiante(estudiante)
            print(f'Estudiante {nombre} {apellido} agregado.')
        
        elif opcion == '2':
            matricula = input("Matrícula del estudiante a eliminar: ")
            estudiante = next((e for e in sistema.estudiantes if e.matricula == matricula), None)
            if estudiante:
                sistema.eliminar_estudiante(estudiante)
                print(f'Estudiante con matrícula {matricula} eliminado.')
            else:
                print(f'Estudiante con matrícula {matricula} no encontrado.')
        
        elif opcion == '3':
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = int(input("Edad: "))
            departamento = input("Departamento: ")
            profesor = Profesor(nombre, apellido, edad, departamento)
            sistema.agregar_profesor(profesor)
            print(f'Profesor {nombre} {apellido} agregado.')
        
        elif opcion == '4':
            nombre = input("Nombre del profesor a eliminar: ")
            profesor = next((p for p in sistema.profesores if p.nombre == nombre), None)
            if profesor:
                sistema.eliminar_profesor(profesor)
                print(f'Profesor {nombre} eliminado.')
            else:
                print(f'Profesor {nombre} no encontrado.')
        
        elif opcion == '5':
            print(f'Número de estudiantes: {sistema.contar_estudiantes()}')
        
        elif opcion == '6':
            print(f'Número de profesores: {sistema.contar_profesores()}')
        
        elif opcion == '7':
            matricula = input("Matrícula del estudiante: ")
            nombre_curso = input("Nombre del curso: ")
            codigo_curso = input("Código del curso: ")
            nombre_profesor = input("Nombre del profesor: ")
            profesor = next((p for p in sistema.profesores if p.nombre == nombre_profesor), None)
            if profesor:
                curso = Curso(nombre_curso, codigo_curso, profesor)
                estudiante = next((e for e in sistema.estudiantes if e.matricula == matricula), None)
                if estudiante:
                    estudiante.agregar_curso(curso)
                    print(f'Curso {nombre_curso} agregado al estudiante {estudiante.nombre} {estudiante.apellido}.')
                else:
                    print(f'Estudiante con matrícula {matricula} no encontrado.')
            else:
                print(f'Profesor {nombre_profesor} no encontrado.')
        
        elif opcion == '8':
            matricula = input("Matrícula del estudiante: ")
            codigo_curso = input("Código del curso a eliminar: ")
            estudiante = next((e for e in sistema.estudiantes if e.matricula == matricula), None)
            if estudiante:
                curso = next((c for c in estudiante.cursos if c.codigo == codigo_curso), None)
                if curso:
                    estudiante.eliminar_curso(curso)
                    print(f'Curso {codigo_curso} eliminado del estudiante {estudiante.nombre} {estudiante.apellido}.')
                else:
                    print(f'Curso {codigo_curso} no encontrado en el estudiante.')
            else:
                print(f'Estudiante con matrícula {matricula} no encontrado.')
        
        elif opcion == '9':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")


# Ejecutar el menú
menu()
