from database import conectar

print("INICIANDO TESTE...")

try:
    conexao = conectar()
    print("Conexão realizada com sucesso!")
    conexao.close()

except Exception as erro:
    print("ERRO COMPLETO:")
    print(repr(erro))