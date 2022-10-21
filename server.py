from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200) # Adiciona o código HTTP 200, é a resposta de sucesso que indica que a requisição foi bem sucedida.
        self.send_header("Content-type", "text/html; charset=utf-8") # Adiciona dados ao cabeçalho HTTP, como o conteúdo retornado e a codificação.
        self.end_headers() #Indica o fim do cabeçalho HTTP na reposta
        data = f"""
            <html>
                <head>
                    <title>Olá Mundo</title>
                </head>
                <body>
                    <p>Testando nosso servidor HTTP!</p>
                    <p>Diretório: {self.path}</p>
                </body>
        """.encode() # Um pequeno trecho html codificado por padrão em UTF-8
        self.wfile.write(data) # Contém o fluxo de saída para gravar a reposta ao cliente.

server = HTTPServer(('localhost', 8000), SimpleHandler) # Passa os parãmetros para iniciar o servidor, o primeiro é uma tupla com o endereço e a porta do servidor e o segundo um handler para tratar as requisições.
server.serve_forever() # Inicia e mantém o servidor ativo.