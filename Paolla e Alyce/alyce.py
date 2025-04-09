def main():
    nome=" "
    idade=0
    email=" "
    cidade=" "
    profissão=" "
    while True:
        print("\n===MENU===")
        print("1.Cadastrar usuário")
        print("2.Ver dados cadastrados")
        print("3.Sair do sistema")
        print("======================")
        opcao=int(input("escolha uma opção:"))
        if opcao==1:
            nome=input("Digite seu nome:")
            idade=int(input("Digite sua idade:"))
            email=input("Digite seu email:")
            cidade=input("Digite sua cidade:")
            profissão=input("Digite sua profissão:")
            print("Usuário cadastrado com sucesso!")
        elif opcao==2:
            print("\n===DADOS CADASTRADOS===")
            print(f"nome:{nome}")
            print(f"idade:{idade}")
            print(f"email:{email}")
            print(f"cidade:{cidade}")
            print("profissão:{profissão}")
        elif opcao==3:
             print("\nSaindo do sistema...")
             break
        else:
         print("Opção inválida!")
if  __name__=="__main__":
   main( )
            
            

