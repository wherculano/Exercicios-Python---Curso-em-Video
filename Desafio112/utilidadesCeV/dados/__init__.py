def leiaDinheiro(msg):
    while True:
        valor = input(msg).strip()
        try:
            valor = float(valor.replace(',', '.'))
            return valor
        except ValueError:
            print('\033[0;31m')
            print(f'ERRO: {valor} é um valor inválido')
            print('\033[m')
