# Sistema de Auditoria de Acessos e Governança de SI 🛡️💻

Este é um sistema desenvolvido em Python focado em automação, governança de dados e auditoria de segurança da informação. O objetivo do projeto é processar uma base de dados estruturada (utilizando listas e dicionários) para monitorar e validar permissões de acesso baseadas no perfil de cada colaborador.

## 🚀 Funcionalidades

- **Estruturação de Dados Avançada:** Armazenamento e manipulação de registros de usuários utilizando listas compostas por dicionários (`Chave: Valor`).
- **Automação de Auditoria:** Varredura automática (`Laço For`) em toda a base de usuários cadastrados.
- **Lógica de Decisão em Segurança (IAM):** Verificação de status e níveis de privilégios (`if/elif/else`), identificando de forma automática acessos suspensos ou restritos a dados confidenciais.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Ambiente de Desenvolvimento:** Pydroid 3 (Mobile IDE)

## 📋 Estrutura do Código

O projeto mapeia as seguintes entidades críticas para cada colaborador:
- `nome`: Identificação do usuário.
- `setor`: Área de atuação dentro da organização.
- `nivel_acesso`: Mapeamento numérico de privilégios no sistema.
- `status`: Condição atual da conta (Ativo/Inativo).

## 🔧 Como Executar o Projeto

1. Certifique-se de ter o Python 3 instalado no seu computador ou dispositivo móvel (como o app Pydroid 3).
2. Crie um arquivo chamado `main.py`.
3. Copie o código-fonte do repositório e cole dentro do arquivo criado.
4. Execute o programa. A saída exibirá o relatório consolidado de auditoria sem a necessidade de intervenções manuais.

---
Desenvolvido por **Gabriel Gomes** como parte dos estudos práticos em Sistemas de Informação e automação voltada à Segurança.
