# Split = separar/dividir

# help(str.split)

cursos = 'Java Python JavaScript Angular Spring Excel'
lista_cursos = cursos.split()
# print(f'Cursos: {lista_cursos}')

cursos = 'Java, Python, JavaScript, Angular, Spring, Excel'
lista_cursos = cursos.split(', ')
# print(f'Cursos: {lista_cursos}')

lista_cursos = cursos.split(', ',2)
print(f'Cursos: {lista_cursos}')
print(len(lista_cursos))

