# TaskMaster
TaskMaster é o meu primeiro app, ele foi feito para um projeto da faculdade, ele é uma aplicação web simples e intuitiva para gerenciamento de tarefas diárias. Desenvolvido com Flask, ela permite que os usuários criem, visualizem, marquem como concluídas e excluam tarefas, ajudando a organizar o dia a dia de maneira prática.

FUNCIONALIDADES
Adicionar Tarefas: Permite que os usuários adicionem novas tarefas à lista.
Visualizar Tarefas: Exibe todas as tarefas cadastradas.
Marcar Tarefas como Concluídas: Usuários podem marcar tarefas como concluídas, facilitando o acompanhamento.
Excluir Tarefas: As tarefas podem ser excluídas da lista.
Validação de Entrada: Assegura que os títulos das tarefas não sejam vazios.
Design Responsivo: O layout da aplicação é responsivo, adaptando-se a diferentes tamanhos de tela, ideal para visualização em dispositivos móveis.
TECNOLOGIAS UTILIZADAS
Backend: Python com Flask
Frontend: HTML, CSS e JavaScript
Banco de Dados: SQLite (para simplicidade)
Ferramentas: Visual Studio Code, Git/GitHub para controle de versão
COMO RODAR O PROJETO

Clone o repositório:

bash
git clone https://github.com/seu-usuario/TaskMaster.git
Navegue até o diretório do projeto:

bash
cd TaskMaster
Crie e ative um ambiente virtual:

bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:

bash
pip install -r requirements.txt
Inicialize o banco de dados:

bash
flask init-db
Execute o servidor:

bash
flask run
Acesse o aplicativo em http://127.0.0.1:5000/.

Se você deseja contribuir para o projeto, fique à vontade para abrir uma issue ou enviar um pull request.
