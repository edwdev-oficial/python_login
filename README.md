# Aplicação de Login com Streamlit

Este é um projeto simples de uma aplicação de login desenvolvida com Python e Streamlit, implementando uma camada de segurança usando `secrets.toml`.

## Funcionalidades

- Tela de login com validação de usuário e senha.
- Páginas simples para teste: Home e About.

## Instalação e Uso

### Pré-requisitos

- Python 3.x instalado.
- Instalação do Streamlit via pip.

### Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/edwdev-oficial/python_login.git
   cd seu-repositorio
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

### Execução

Para iniciar a aplicação, execute o seguinte comando:

```bash
streamlit run app.py
```

Abra o navegador e vá para `http://localhost:8501` para visualizar a aplicação em execução.

Claro, aqui está uma versão melhorada da seção de Configuração:

## Configuração

Antes de executar a aplicação, é necessário configurar o arquivo `.streamlit/secrets.toml` com as credenciais necessárias. Abra o arquivo `secrets.toml` e insira as informações de login conforme o exemplo abaixo:

```toml
[login]
user = "seu_usuario"
password = "sua_senha"
```

Substitua `"seu_usuario"` e `"sua_senha"` pelos seus próprios dados de usuário e senha.

Certifique-se de que o arquivo `secrets.toml` está corretamente configurado para que a autenticação funcione corretamente durante a execução da aplicação.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues para relatar problemas ou sugerir melhorias através de pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

## Contato

Para mais informações ou feedback, entre em contato através do email: edjdevel@gmail.com

## Autor

edwdev - [GitHub](https://github.com/edwdev-oficial)