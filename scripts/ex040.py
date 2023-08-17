# Cores no Terminal (sem bibliotecas)
# \033['style';'text';'background'm
# style pode ser 0(none), 1(bold), 4(underline), 7(negative)
# text pode ser 30(branco), 31(vermelho), 32(verde), 33(amarelo), 34(azul), 35(magenta), 36(ciano) e 37(cinza)
# background pode ser 40(branco), 41(vermelho), 42(verde), 43(amarelo), 44(azul),45 (magenta), 46(ciano) e 47(cinza)
# também é possível atribuir cores a variáveis para usar
cores = {
    'limpa': '\033[m',
    'textoBranco': '\033[30m',
    'textoVermelho': '\033[31m',
    'textoVerde': '\033[32m',
    'textoAmarelo': '\033[33m',
    'textoAzul': '\033[34m',
    'textoMagenta': '\033[35m',
    'textoCiano': '\033[36m',
    'textoCinza': '\033[37m'
}
# Sem usar variáveis:
print('\033[0;30;41mTexto Colorido\033[m')
print('\033[4;33;44mTexto Colorido\033[m')
print('\033[1;34;43mTexto Colorido\033[m')
print('\033[30;42mTexto Colorido\033[m')
print('\033[mTexto Colorido\033[m')
print('\033[7;30mTexto Colorido\033[m')

# Usando variáveis:
print(f"{cores['textoBranco']}Olá, esse texto está na cor branca.{cores['limpa']}")
print(f"{cores['textoVermelho']}Olá, esse texto está na cor vermelha.{cores['limpa']}")
print(f"{cores['textoVerde']}Olá, esse texto está na cor verde.{cores['limpa']}")
print(f"{cores['textoAmarelo']}Olá, esse texto está na cor amarelo.{cores['limpa']}")
print(f"{cores['textoAzul']}Olá, esse texto está na cor azul.{cores['limpa']}")
print(f"{cores['textoMagenta']}Olá, esse texto está na cor magenta.{cores['limpa']}")
print(f"{cores['textoCiano']}Olá, esse texto está na cor ciano.{cores['limpa']}")
print(f"{cores['textoCinza']}Olá, esse texto está na cor cinza.{cores['limpa']}")