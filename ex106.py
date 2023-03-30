# progama que assesa o help e por meiu de uma função mais decorada pro usuario
from time import sleep

c = ('\033[31m',  # 1sem cores
     )


def relp(ajuda):
    return help(c[1], ajuda)


print('.= ' * 15)
a = input('digite a função a ser analizada: ')
relp(a)
print(a)
print('.= ' * 15)

# não consegui colocar cores
