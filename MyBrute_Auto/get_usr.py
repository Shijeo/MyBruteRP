def current_usr(): # Retorna o valor do usuário atual
    try:
        with open('usr_atu.txt', 'r') as arq_usr:
            usr_brute = (arq_usr.read().strip())
            return usr_brute  # Remove espaços em branco extras

    
    except FileNotFoundError:
        with open('usr_atu.txt', 'w') as arq_usr:
            usr_curr = arq_usr.write('higtst001')  # Escreva um valor padrão
        return usr_curr

def next_usr(usr_brute):
    usr_brute = usr_brute[:-2] + str(int(usr_brute[-2:]) + 1).zfill(2)  # Pega os últimos 2 caracteres, soma 1 e coloca de volta
    with open('usr_brute.txt', 'a') as arq_usr:
        arq_usr.write(usr_brute + ";")
    with open('usr_atu.txt', 'w') as arq_usr:
            arq_usr.write(usr_brute)  # Escreva um valor padrão 
    
def next_brute(usr_brute):      
    name_brute = usr_brute[:-2] + str(int(usr_brute[-2:]) + 1).zfill(2)
    return name_brute