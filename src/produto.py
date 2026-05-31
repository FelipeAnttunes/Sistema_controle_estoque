from database import conectar

# cadastro de produtos 

def cadastrar_produto():
    try: 
        nome = input("Nome do produto: ")
        marca = input("Marca: ")
        quantidade = int(input("Quantidade: "))
        valor = float(input("Valor: ").replace(",","."))


        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            Insert into produtos (nome, marca, quantidade, valor)
            VALUES(%s, %s, %s, %s)""" ,
            (nome, marca, quantidade, valor))
        
        conn.commit()
        print("\n Produto cadastrado com sucesso!")

    except Exception as e:
        print(f"Erro ao cadastrar: {e}")

    finally: 
        if 'conn' in locals():
            conn.close()


# Listar produtos cadastrados

def listar_produtos():
    try:
        conn = conectar()
        cur = conn.cursor()

        cur.execute("SELECT * FROM produtos ORDER BY id")
        produtos = cur.fetchall()

        print("\n===== LISTA DE PRODUTOS =====")

        if not produtos:
            print("Nenhum produto encontrado.")
            return
        
        for id, nome, marca, quantidade, valor, data in produtos:
            print(f"""
            ID: {id}
            Nome: {nome}
            Marca: {marca}
            Quantidade: {quantidade}
            Valor: R$ {valor}
            Data de Cadastro: {data}
            ------------------------
            """)

    except Exception as e:
        print(f"Erro ao listar produtos: {e}")

    finally:
        if 'conn' in locals():
            conn.close()


# Atualizar produto

def atualizar_produto():
    try:
        id_produto = int(input("ID do produto: "))
        nome = input("Novo nome do produto: ")
        marca = input("Nova marca: ")
        quantidade = int(input("Nova quantidade: "))
        valor = float(input("Novo valor: ").replace(",","."))

        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            UPDATE produtos
            SET nome = %s, marca = %s, quantidade = %s, valor = %s
            WHERE id = %s
        """, (nome, marca, quantidade, valor, id_produto))

        conn.commit()

        if cur.rowcount > 0:
            print("\nProduto atualizado com sucesso!")
        else:
            print("\nProduto não encontrado.")

    except Exception as e:
        print(f"Erro ao atualizar produto: {e}")

    finally:
        if 'conn' in locals():
            conn.close()    


# Deletar produto

def deletar_produto():
    try:
        id_produto = int(input("ID do produto: "))

        conn = conectar()
        cur = conn.cursor()

        cur.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
        conn.commit()

        if cur.rowcount > 0:
            print("\nProduto deletado com sucesso!")
        else:
            print("\nProduto não encontrado.")

    except Exception as e:
        print(f"Erro ao deletar produto: {e}")

    finally:
        if 'conn' in locals():
            conn.close()


# Menu de opções para o usuário

def menu():
    while True:
        print("""
              
        ===== SISTEMA DE ESTOQUE =====
              
        1. Cadastrar Produto
        2. Listar Produtos
        3. Atualizar Produto
        4. Deletar Produto
        5. Sair
        """)

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            atualizar_produto()
        elif opcao == '4':
            deletar_produto()
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# executar o menu
if __name__ == "__main__":
    menu()   


   



                  
                  



                    
                    
                    
                    
                    
