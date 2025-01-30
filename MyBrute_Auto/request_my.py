# URL da API
import requests


def fights_left(name_brute):
    url = "https://brute.eternaltwin.org/api/brute/" + name_brute + "/for-hook"
    
    try:
        # Faz a requisição HTTP GET
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

        data = response.json()
        # Obtém o valor do campo 'fightsLeft'
        fights_left = data.get('fightsLeft')
        if fights_left is not None:
            print(f" {name_brute}  - Fights left:  {fights_left}")
            return fights_left
        else:
            print("O campo 'fightsLeft' não foi encontrado na resposta.")
    
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
    except ValueError:
        print("Erro ao decodificar a resposta JSON.")
        # Exibe o conteúdo da resposta
        print(response.text)

def levelup(name_brute):
    
    url = "https://brute.eternaltwin.org/api/brute/" + name_brute + "/for-hook"
    try:
        # Faz a requisição HTTP GET
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

        data = response.json()
        # Obtém o valor do campo 'fightsLeft'
        xp = data.get('xp')
        level = data.get('level')+1
        if xp >= int(1.2 * level + 3):
            print(f" {name_brute}  - Level up!")
            return True
        else:
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
    except ValueError:
        print("Erro ao decodificar a resposta JSON.")
        # Exibe o conteúdo da resposta
        print(response.text)
