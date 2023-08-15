frase = 'Curso em Vídeo Python'
fraseSeparada = frase.split()
fraseJunta = ' '.join(fraseSeparada)
frase2 = '   Aprenda Python  '
print(frase[9])
print(frase[9:13])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(f"A frase '{frase}' têm {len(frase)} caracteres")
print(f"A letra 'o' aparece {frase.count('o')} vezes em '{frase}'")
print(f"Entre os caracteres 0 e 13, a letra 'o' aparece {frase.count('o',0,13)} vez")
print(f"Dentro da frase '{frase}', o conjunto de caracteres 'deo' começou na posição {frase.find('deo')}!")
print(f"Dentro da frase '{frase}', a string 'Android' não pode ser encontrado retornando o valor {frase.find('Android')}!")
print(f"Dentro da frase '{frase}', existe a palavra 'Curso'? {'Curso' in frase}")
print(f"Agora irei substituir 'Python' por 'Android' na frase '{frase}': '{frase.replace('Python','Android')}'")
print(f"Frase em maiúsculas: '{frase.upper()}'")
print(f"Frase em minúsculas: '{frase.lower()}'")
print(f"Frase capitalizada: '{frase.capitalize()}'")
print(f"Frase em forma de título: '{frase.title()}'")
print(f"Retirando os espaços desnecessários de '{frase2}': '{frase2.strip()}'")
print(f"Retirando os espaços do fim de '{frase2}': '{frase2.rstrip()}'")
print(f"Retirando os espaços do início de '{frase2}': '{frase2.lstrip()}'")
print(f"Dividindo a frase '{frase}' em elementos de um Array: {fraseSeparada}")
print(f"Unindo os elementos de {fraseSeparada} em uma frase: '{fraseJunta}'")
print(
"""=======================================================================================================
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam nec pretium magna, quis rutrum dolor.
sagittis nulla id finibus. Etiam vehicula lobortis sem eu dictum. In varius neque vel arcu pretium, 
id blandit leo aliquam. Fusce feugiat turpis ut lectus varius iaculis. Nam ac pulvinar magna. Nam conse
ctetur risus sed pellentesque euismod. Nullam id quam a dui dignissim eleifend quis quis diam. 
In ullamcorper mollis orci, sed cursus massa facilisis sit amet. Cras consectetur nisi purus, sit amet 
sagittis nibh feugiat pulvinar. Pellentesque sed magna purus.
=========================================================================================================="""
)

achar = 'Curso'
if frase.find(achar) == 0:
    print(f"Existe '{achar}' na seguinte frase '{frase}': \nSim, '{achar}' está em '{frase}' e começa na posição {frase.find(achar)}")
else:
    print(f"Existe '{achar}' na seguinte frase '{frase}': \nNão, a palavra '{achar}' não está em '{frase}'")

