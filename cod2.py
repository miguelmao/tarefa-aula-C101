import random

r = "s"

while r =="s":
    num = random.randint(1,6)
    print(f"Valor do dado {num}!")

    if num == 1:
        print("\n[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]\n")
    
    if num == 2:
        print("\n[-----]")
        print("[    0]")
        print("[     ]")
        print("[0    ]")
        print("[-----]\n")

    if num == 3:
        print("\n[-----]")
        print("[    0]")
        print("[  0  ]")
        print("[0    ]")
        print("[-----]\n")

    if num == 4:
        print("\n[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]\n")

    if num == 5:
        print("\n[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]\n")

    if num == 6:
        print("\n[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]\n")


    print("Quer jogar novamente?")
    resposta = input("Pressione S se Sim e N se Não:  ")
    r = resposta.lower()

