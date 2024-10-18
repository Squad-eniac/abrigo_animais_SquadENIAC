# Sistema de Gerenciamento de Abrigo de Animais 🐾🐾

## Visão Geral do Projeto
Este projeto é o desafio final do **Bootcamp Back-End Python e Django** da WoMakersCode. O objetivo é desenvolver um **Sistema de Gerenciamento de Abrigo de Animais Responsivo** utilizando **Django**, que permitirá aos usuários visualizar animais disponíveis para adoção e gerenciar solicitações de adoção.

## O Que Vamos Fazer
- Configurar um **ambiente de desenvolvimento Django**.
- Implementar um **design responsivo** usando **HTML5, CSS3 e Bootstrap**.
- Criar **páginas de detalhes dos animais** com nome, idade, espécie e histórico de saúde.
- Desenvolver um **sistema de gerenciamento de adoções**, com fluxo de aprovação.
- Integrar uma **barra de pesquisa** para filtrar animais por palavras-chave.
- Construir uma **interface administrativa** com Django para a gestão do abrigo.

## 👥 SQUAD ENIAC - Integrantes 

- Ana Julia Rauber - [GitHub](https://github.com/anajuliarauber) - [Likedin](https://www.linkedin.com/in/ana-julia-rauber/);
- Angelica Conceição Salvino da Silva - [GitHub](https://github.com/AngelicaSalvino) - [Likedin](https://www.linkedin.com/in/angelica-salvino/);
- Caroline Souza Camargo - [GitHub](https://github.com/Caroline-Camargo) - [Likedin](https://www.linkedin.com/in/caroline-souza-camargo-023b54164/);
- Fabiana Maria Ignácio da Silva - [GitHub](https://github.com/Ignacio-fabianamaria) - [Likedin](https://www.linkedin.com/in/fabianaignacio/);
- Kassia do Espirito Santo - [GitHub](https://github.com/KassiaES) - [Likedin](https://www.linkedin.com/in/kassia-es);
- Laysa Alexia Lima Cipriano - [GitHub](https://github.com/LayCipriano) - [Likedin](https://www.linkedin.com/in/lay-cipriano/);
- Marina Cesconeto dos Santos (líder do squad) - [GitHub](https://github.com/marina6coneto) - [Likedin](https://www.linkedin.com/in/marina-cesconeto-dos-santos-a17563216/);
- Rosana de Souza Brito - [GitHhub](https://github.com/RosanaBrito) - [Likedin](https://www.linkedin.com/in/rosanadesouzabrito/);

### 🤝 Divisão das Tarefas

- **Configurações iniciais e Django Admin** - Fabiana
- **Models**
- **Views**
- **Templates**
- **Apresentação**


### 📥 Download do Projeto

1. **Clonando o Repositório**
Primeiro, faça o clone do repositório para sua máquina local utilizando o comando:

```bash
   git clone https://github.com/Squad-eniac/abrigo_animais_SquadENIAC.git
   cd abrigo_animais_SquadENIAC/
```

2. **Criando e Ativando o Ambiente Virtual**
Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv .venv 
```

Ative o ambiente virtual:

- Para Linux ou macOS

```bash
source .venv/bin/activate
```

- Para Windows

```bash
.\.venv\Scripts\activate
```

3. **Instalando as Dependências**
Com o ambiente virtual ativado, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

4. **Executando as Migrações:**
Navegue até o diretório do projeto base e execute as migrações:

```bash
cd animal_shelter/
python manage.py migrate
```

8. **Criando um Superusuário**
Para acessar o painel administrativo, crie um superusuário:

```bash
python manage.py createsuperuser
```

9. **Executando a aplicação**
Execute o servidor local para rodar o projeto:

```bash
python manage.py runserver
```
