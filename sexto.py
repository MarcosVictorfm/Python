numero_placa = input("Digite o ultímo número da placa do seu veiculo:")

match numero_placa:
    case "1" | "2": print("Não pode trafegar na segunda")
    case "3" | "4": print("Não pode trafegar na terça")
    case "5" | "6": print("Não pode trafegar na quarta")
    case "7" | "8": print("Não pode trafegar na quinta")
    case "9" | "0": print("Não pode trafegar na sexta")
    case _: print("Final da placa inválido")
   
