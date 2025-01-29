
def current_usr():
    with open('usr_atu.txt', 'r') as arq_usr: 
        return arq_usr.read().strip()
def next_usr():
    with open('usr_brute.txt', 'a+') as arq_usr:
        usr_brute = arq_usr.read()  # Lê todo o conteúdo do arquivo
        usr_brute = usr_brute[:-2] + str(int(usr_brute[-2:]) + 1).zfill(2)  # Pega os últimos 2 caracteres, soma 1 e coloca de volta
        arq_usr.seek(0, 2)
        arq_usr.write(usr_brute+";")
        