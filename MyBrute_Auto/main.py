from create_acc import create_acc
from create_brute import create_brute
from login_acc import login_acc
from fight_brute import do_fight
from driver_setup import driver  # Importa o driver configurado
import get_usr


create_acc()

login_acc()

create_brute()

do_fight()

input("Pressione Enter para fechar o navegador...")
driver.get("https://brute.eternaltwin.org/")

driver.close()