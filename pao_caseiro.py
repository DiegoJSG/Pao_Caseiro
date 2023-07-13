import time
import textwrap

#deixar os cabeçalhos centralizado e (com cores opcional)
# "30" para preto / "31" para vermelho /"32" para verde /"33" para amarelo
# "34" para azul / "35" para magenta / "36" para ciano / "37" para branco

def print_centered_header(text, color_code):
    print()
    header_length = 50
    header = f"\033[1;{color_code}m{'#' * header_length}\n{textwrap.fill(text, header_length).center(header_length)}\n{'#' * header_length}\033[0m"
    print(header)

def print_recipe(language):
    if language == "1":
        # Receita em português
        preparar_massa()
        misturar_amassar_massa()
        fermentar_massa()
        assar_pao()
        
    elif language == "2":
        # Receita em inglês
        print_english_recipe()
    elif language == "3":
        # Receita em espanhol
        print_spanish_recipe()
    else:
        print("Opção inválida. Tente novamente.")

def preparar_massa():
    print_centered_header("🍞  Bem-Vindos à receita de Pão caseiro! 🍞", "33")
    time.sleep(2)
    print("\nPreparando a massa do pão...")
    time.sleep(1)

    ingredientes = [
        "1kg de farinha de trigo sem fermento",
        "20g de fermento biológico seco",
        "300ml de água e leite quente ... não é fervendo! apenas quente"
    ]
    for ingrediente in ingredientes:
        time.sleep(2)
        print(ingrediente)

    time.sleep(2.5)  # Intervalo de 2.5 segundos

    print("125g de açúcar")
    time.sleep(1)

    outros_ingredientes = [
        "125ml de óleo vegetal ou banha de porco derretida",
        "2 ovos",
        "uma colher de sopa de sal"
    ]
    for ingrediente in outros_ingredientes:
        time.sleep(2)
        print(ingrediente)
    time.sleep(2)

def misturar_amassar_massa():
    time.sleep(2)
    print_centered_header("👩‍🍳 Misturando a Massa 👨‍🍳", "34")
    print("\nMisture a farinha e fermento manualmente em uma tigela grande...")
    time.sleep(2)
    print("E deixe agir por pelo menos 1 minuto.")
    time.sleep(2)

    print("\nColoque o sal, açúcar, ovos e óleo e novamente misture...")
    time.sleep(3)

    print("Se quiser, pode usar a batedeira, mas é possível fazer tudo manualmente.")
    time.sleep(3)
    print("Adicione a água e o leite gradualmente enquanto mistura os ingredientes.")
    time.sleep(3)
    print("\nMisture a massa até obter uma consistência homogênea.")
    time.sleep(2)
    print("Se necessário, adicione um pouco de farinha para obter uma consistência maior.")
    time.sleep(3)

def fermentar_massa():
    time.sleep(2)
    print_centered_header("🌡️ Fermentando a Massa 🌡️", "35")
    print("\nUse um rolo de madeira para dar forma ao nosso pão.")
    time.sleep(2)
    print("É possível rechear se quiser, o recheio fica a sua preferência...")
    time.sleep(2)
    print("\nColoque a massa em uma forma já devidamente untada.")
    time.sleep(2)
    print("Cubra a massa com um pano limpo e deixe descansar em um local por pelo menos uma hora.")
    time.sleep(3)

def assar_pao():
    time.sleep(2)
    print_centered_header("🔥 Assando o Pão 🔥", "31")
    time.sleep(2)

    print("\nColoque o pão no forno a \033[1;32m160°C\033[0m por 10 minutos. Não é necessário pré-aquecer o forno.")
    time.sleep(3)
    print("Após os 10 minutos iniciais, aumente para \033[1;32m180°C\033[0m.")
    time.sleep(2)
    print("Asse por mais 20-25 minutos aproximadamente.")
    time.sleep(2)
    print_centered_header(" 😋 Bom Apetite 😋 ", "32")

def print_english_recipe():
    # Receita em inglês
    print_centered_header("🍞 Welcome to our Homemade Bread Recipe! 🍞", "33")
    time.sleep(2)
    print("\nPreparing the bread dough...")
    time.sleep(1)

    ingredients = [
        "1kg of all-purpose flour",
        "20g of dry yeast",
        "300ml of warm water and milk mixture ... not boiling! just warm"
    ]
    for ingredient in ingredients:
        time.sleep(2)
        print(ingredient)

    time.sleep(2.5)  # Intervalo de 2.5 segundos

    print("125g of sugar")
    time.sleep(1)

    other_ingredients = [
        "125ml of vegetable oil or melted lard",
        "2 eggs",
        "1 tablespoon of salt"
    ]
    for ingredient in other_ingredients:
        time.sleep(2)
        print(ingredient)
    time.sleep(3)

    print_centered_header("👩‍🍳 Mixing and Kneading the Dough 👨‍🍳", "34")
    print("\nPlace the flour and yeast in a large bowl...")
    time.sleep(2)
    print("Let it rest for at least 1 minute.")
    time.sleep(2)

    print("\nAdd the salt, sugar, eggs, and oil and mix again...")
    time.sleep(3)

    print("You can use a mixer if you want, but it can be done manually.")
    time.sleep(3)
    print("Gradually add the water and milk mixture while mixing the ingredients.")
    time.sleep(3)
    print("\nKnead the dough until it reaches a homogeneous consistency.")
    time.sleep(2)
    print("If necessary, add a little more flour to achieve a firmer consistency.")
    time.sleep(3)

    print_centered_header("🌡️ Fermenting the Dough 🌡️", "35")
    print("\nCover the dough with a clean cloth and let it rest in a warm place for at least one hour.")
    time.sleep(2)
    print("After that, the dough should have risen and doubled in size.")
    time.sleep(3)

    print_centered_header("🔥 Baking the Bread 🔥", "31")
    print("\nPreheat the oven to \033[1;32m180°C\033[0m.")
    time.sleep(2)
    print("Shape the dough as desired and place it on a baking sheet.")
    time.sleep(2)
    print("Bake for approximately 30-35 minutes until golden brown.")
    time.sleep(2)
    print_centered_header(" 😋 Enjoy Your Bread ! 😋 ", "32")

def print_spanish_recipe():
    # Receita em espanhol
    print_centered_header("🍞 ¡Bienvenidos a nuestra receta de Pan Casero! 🍞", "33")
    time.sleep(2)
    print("\nPreparando la masa del pan...")
    time.sleep(1)

    ingredients = [
        "1kg de harina de trigo sin fermento",
        "20g de levadura biológica seca",
        "300ml de agua y leche caliente ... ¡no hirviendo! solo caliente"
    ]
    for ingredient in ingredients:
        time.sleep(2)
        print(ingredient)

    time.sleep(2.5)  # Intervalo de 2.5 segundos

    print("125g de azúcar")
    time.sleep(1)

    other_ingredients = [
        "125ml de aceite vegetal o manteca de cerdo derretida",
        "2 huevos",
        "una cucharada de sal"
    ]
    for ingredient in other_ingredients:
        time.sleep(2)
        print(ingredient)
    time.sleep(3)

    print_centered_header("👩‍🍳 Mezclando y Amasando la Masa 👨‍🍳", "34")
    print("\nColoca la harina y levadura en un recipiente grande...")
    time.sleep(2)
    print("Deja reposar durante al menos 1 minuto.")
    time.sleep(2)

    print("\nAñade la sal, azúcar, huevos y aceite y vuelve a mezclar...")
    time.sleep(3)

    print("Puedes usar una batidora si quieres, pero también se puede hacer a mano.")
    time.sleep(3)
    print("Agrega gradualmente el agua y la leche caliente mientras mezclas los ingredientes.")
    time.sleep(3)
    print("\nAmasa la masa hasta obtener una consistencia homogénea.")
    time.sleep(2)
    print("Si es necesario, agrega un poco más de harina para obtener una consistencia más firme.")
    time.sleep(3)

    print_centered_header("🌡️ Fermentando la Masa 🌡️", "35")
    print("\nCubre la masa con un paño limpio y déjala reposar en un lugar cálido durante al menos una hora.")
    time.sleep(2)
    print("Después de eso, la masa debería haber crecido y duplicado su tamaño.")
    time.sleep(3)

    print_centered_header("🔥 Horneando el Pan 🔥", "31")
    print("\nPrecalienta el horno a \033[1;32m180°C\033[0m.")
    time.sleep(2)
    print("Dale forma a la masa como desees y colócala en una bandeja para hornear.")
    time.sleep(2)
    print("Hornea durante aproximadamente 30-35 minutos hasta que esté dorado.")
    time.sleep(2)
    print_centered_header("😋 ¡Buen Provecho! 😋 ", "32")

# Função para exibir o menu e obter a escolha do idioma
def selecionar_idioma():
    print("Selecione o idioma:")
    print("1 - Português")
    print("2 - English")
    print("3 - Español")
    idioma = input("Escolha o idioma da receita: ")
    return idioma

idioma = selecionar_idioma()
print_recipe(idioma)
