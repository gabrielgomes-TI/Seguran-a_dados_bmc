# sistemas de auditória de segurança da informação.
usuarios_sistemas = [
    {
        "nome": "Gabriel Gomes",
        "setor": "Sistemas de Informação",
        "nivel_acesso": 3,
        "status": "Ativo"
    },
    {
        "nome": "Lucas Silva",
        "setor": "Financeiro",
        "nivel_acesso": 1,
        "status": "Inativo"
    },
    {
        "nome": "Maria Costa",
        "setor": "Diretoria",
        "nivel_acesso": 5,
        "status": "Ativo"
    }
]
print("--- relatório de acesso ao sistema!")

# percorre a lista e extrai a informação de cada dicionário
for usuario in usuarios_sistemas:
	print(f"colaborado: {usuario['nome']}")
	print(f"setor: {usuario['setor']}")
	print(f"nivel: {usuario['nivel_acesso']}")
	
# vamos tomar a decisão correta
if usuario["status"] == "inativo":
	print("ALERTA: acesso suspenso pelo chefe!")

elif usuario["nivel_acesso"] >= 9:
	print("status: acesdo somente a dados confidenciais.")
	
else:
	print("status: ATENÇÃO acesso limitado.")
	
print("\n---------------------------------‐-----------------")
print("[auditória finalizada com sucesso]")
