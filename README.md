# Projeto E-commerce 
<p>deployed on aws at: <a href="https://projetos.matheusvicente.dev.br/loja/" target="_blank" rel="noopener noreferrer">https://projetos.matheusvicente.dev.br/loja/</a></p>


### Sobre o projeto
Realizada a criação de um e-commerce simples utilizando o framework Django. Projeto do curso [Curso de Python 3 - Do Básico Ao Avançado (Completo)](https://www.udemy.com/course/python-3-do-zero-ao-avancado/) sem intenção de ser utilizado para produção. 

- Projeto conta com:
* Cadastro de usuário
* Login e Logout para usuários
* Área para usuário com histórico dos pedidos
* Adicionar e remover do carrinho
* Carrinho que navega entre sessões
* Busca
* CPF único no cadastro

Se você for dar uma olhada no <a href="https://projetos.matheusvicente.dev.br/loja/" target="_blank" rel="noopener noreferrer">site</a> recomendo que se for cadastrar um usuário use o gerador de dados da <a href="https://www.4devs.com.br/gerador_de_pessoas" target="_blank" rel="noopener noreferrer">4devs</a>

### A ser desenvolvido
No curso em questão o projeto não conta com um sistema de cálculo de frete, que pretendo implementar no projeto em breve, inclusive você pode me ajudar. Também pretendo melhorar a parte do Front-End que está totalmente básica e foram retirados arquivos do próprio curso mencionado.

- [ ] Cálculo de frete
- [ ] Melhorar Front-End

### Como rodar o projeto na sua máquina
Abaixo um mini guia de como rodar na sua máquina local, pode variar dependendo do sistema operacional que você estiver utilizando.
Necessário:

- Instalar git:
- Instalar Python:

Escolha uma pasta da sua máquina para baixar os arquivos do repositório e dê o comando em seu terminal:
```
git clone https://github.com/Matheusvicentesn/django-e-commerce.git .
```


- Em seguida na mesma pasta onde você clonou o repositório(certifique-se de estar na pasta raiz do projeto) vamos criar e ativar o nosso ambiente virtual através dos comandos:

```
python3 -m venv venv
```
```
source venv/bin/activate
```

- Com o ambiente criado e ativado, podemos instalar os requerimentos para rodar o projeto:

```
pip install -r requirements.txt
```

- Realizar migrações e criar um usuário:

```
python manage.py migrate
```
- E para criar o usuário administrador:

```
python manage.py createsuperuser
```
- Preencher com as informações:
 Nome de usuário, E-mail, senha, e repetir senha. Se aparecer a mensagem que senha é fraca você pode prosseguir apertando Y. 
 
![alt text](https://i.ibb.co/LZbQ0Cf/Screenshot-20220321193315-756x204.png)



- Agora você já pode rodar na sua máquina, com o comando:
```
python manage.py runserver
```

- Para acessar a área administrativa basta entrar no endereço padrão:
```
http://127.0.0.1:8000/admin/
```
Aqui você pode criar usuários, adcionar produtos e "gerenciar" a loja !

Qualquer dúvida ou sugestão estou disponível no e-mail:
<a href="mailto:contato@matheusvicente.dev.br?subject=Questions" title=""> contato@matheusvicente.dev.br</a>



