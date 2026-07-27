# Sistema de Controle de Estoque

# Sobre o projeto

Este projeto foi desenvolvido durante minha jornada de aprendizado em Python e Flask.

Antes de criar a versão web, desenvolvi todo o sistema utilizando apenas Python no terminal. Inicialmente, toda a lógica foi construída com estruturas de repetição (`while`) e condicionais, sem utilizar funções. O objetivo era compreender a lógica do sistema e validar seu funcionamento.

Após consolidar essa primeira versão, refatorei toda a aplicação, separando cada funcionalidade em funções específicas, como cadastro, pesquisas, entrada e saída de estoque. Essa etapa me ajudou a entender melhor a organização do código e a importância da reutilização de funções.

Com essa base consolidada, iniciei a migração para o Flask, transformando o sistema em uma aplicação web. Durante esse processo implementei autenticação de usuários, sessões, templates HTML e, posteriormente, reorganizei toda a aplicação utilizando Blueprints para deixar a arquitetura mais modular, organizada e preparada para futuras melhorias.

Este projeto representa minha evolução como desenvolvedor. Mais do que aprender uma linguagem, procurei compreender como um software evolui ao longo do tempo, passando por diferentes etapas de organização, refatoração e melhoria contínua.


#  Funcionalidades

-  Login de usuário
-  Cadastro de produtos
-  Pesquisa por categoria
-  Pesquisa por nome do produto
-  Entrada de estoque
-  Saída de estoque
-  Relatório completo dos produtos cadastrados
-  Validação de formulários
-  Organização da aplicação utilizando Blueprints



# Tecnologias utilizadas

- Python
- Flask
- HTML5
- CSS3
- Jinja2

---

# Estrutura do projeto

  text
Sistema_Estoque/
│
├── app.py
├── routes/
│   ├── login.py
│   ├── cadastro.py
│   ├── buscas.py
│   ├── painel.py
│   ├── relatorio.py
│   ├── dados.py
│   └── estoque/
│       ├── deposito.py
│       └── saida.py
│
├── templates/
├── static/


---

# O que aprendi com este projeto

Durante o desenvolvimento deste sistema consegui praticar diversos conceitos importantes para o desenvolvimento web utilizando Flask, entre eles:

. Organização de projetos utilizando Blueprints
. Criação e gerenciamento de rotas
. Utilização de sessões para autenticação
. Compartilhamento de dados entre módulos
. Manipulação de listas e dicionários
. Validação de formulários
. Refatoração de código
. Organização de pastas e responsabilidades de cada módulo
. Versionamento utilizando Git e GitHub.

Mais do que desenvolver funcionalidades, este projeto me ensinou a investigar problemas, entender a causa dos erros e buscar soluções de forma organizada.



# Próximas melhorias

Este projeto continuará sendo atualizado. Algumas funcionalidades que pretendo implementar são:

- Banco de dados SQLite
- Cadastro de usuários
- Controle de permissões
- Histórico de movimentações
- Dashboard com indicadores
- Melhorias na interface
- Deploy da aplicação



# Sobre mim :D

Sou fascinado pela tecnologia e atualmente estou em transição para a área de desenvolvimento de software.

Acredito que a melhor forma de aprender programação é construindo projetos reais, enfrentando desafios e buscando compreender o motivo de cada solução aplicada.

Este sistema representa minha evolução durante os estudos e demonstra minha dedicação em aprender cada vez mais sobre desenvolvimento utilizando Python.

Estou sempre em busca de novos conhecimentos e oportunidades para crescer profissionalmente como Desenvolvedor Python.




**Anderson da Silva Santos**

https://www.linkedin.com/in/anderson-da-silva-santos-541256339/
