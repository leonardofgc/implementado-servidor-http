# Implementando Um Servidor HTTP
> Exemplo básico de construção de um servidor HTTP usando recursos nativos do Python.

![Badge em Desenvolvimento](https://img.shields.io/badge/Python-3.10-green)
![Badge em Desenvolvimento](https://img.shields.io/badge/Status-Em%20Desenvolvimento-green)

Objetivo deste repositório é pôr em pratica o conhecimento da implementação de um servidor HTTP e início da construção de uma API. 

**Nota**
> O Python possui um servidor HTTP nativo.

## Instalação

```bash
python -m http.server 8080
```

## Como usar via linha de comando?

No exemplo, estamos iniciando o servidor HTTP na pora 8080

_O argumento -m do python é utilizado para executar pela linha de comando um módulo que não está localizado na pasta atual.. No nosso caso o módulo http.server não está na pasta onde estamos executando o comando._

## Como usar via arquivo .py?
- Crie o arquivo server.py
- Importe o http.server

```bash
from http.server import HTTPServer, BaseHTTPRequestHandler
```
- Crie uma classe que seja herde de BaseHTTPRequestHandler
```bash
class SimpleHandler(BaseHTTPRequestHandler):
  ...
```
- Crie um método que irá tratar as requisições GET
```bash
def do_GET(self):
  ...
```
## Como executar via arquivo .py?

```bash
python server.py
```

## Versão/Funcionalidade
* 0.0.1
    * Work in progress

## Melhorias
- [ ] Exibir Dados
- [ ] Retornar Os Dados Em Um Formato Universal, Por Exemplo: JSON 

**Nota**
> http.server não é recomendado o uso em ambiente de produção.
> Documentação Ofical: [HTTP servers](https://docs.python.org/3/library/http.server.html#module-http.server "HTTP servers") 
## Contato

Leonardo Guimarães – [@leonardofgc](https://www.linkedin.com/in/leonardofgc/) – leonardofgc@gmail.com

[https://github.com/leonardofgc/implementado-servidor-http](https://github.com/leonardofgc/)

## Clonando O Projeto

1. git clone https://github.com/leonardofgc/implementado-servidor-http.git
2. cd implementado-servidor-http
3. python3 -m venv .venv `Neste projeto esse passo é Opcional, até o momento todos os recursos são nativos do Python, porém recomendado.`
4. python server.py
