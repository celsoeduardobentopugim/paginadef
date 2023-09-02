def minha_funcao (**kwargs):
    for chave, valor in kwargs. items():
        print(f"a chave é {chave} eo valor é {valor}")
    print(type(kwargs))

minha_funcao(nome="joao",idade=25, país="brasil")
