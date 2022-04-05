def imprimo(*args):
    for i in range(len(args)):
        print(f'{args[i]} de tipo {type(args[i])}')

imprimo(1) 
imprimo(2, "hola")
imprimo([1,2], "hola", 3.2)