from http.server import HTTPServer, BaseHTTPRequestHandler
from evento import Evento
from evento_online import EventoOnLine
import json
ev = Evento("Aula De Python", "Rio de Janeiro")
ev_online = EventoOnLine("Live de Python")
ev2_online = EventoOnLine("Live de GoLang")
ev3_online = EventoOnLine("Live de Rust")
eventos = [ev, ev_online, ev2_online, ev3_online]
class SimpleHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)  # Adiciona o código HTTP 200, é a resposta de sucesso que indica que a requisição foi bem sucedida.
            self.send_header("Content-type","text/html; charset=utf-8")  # Adiciona dados ao cabeçalho HTTP, como o conteúdo retornado e a codificação.
            self.end_headers()  # Indica o fim do cabeçalho HTTP na reposta
            data = f"""
                <html>
                    <head>
                        <title>Olá Mundo</title>
                    </head>
                    <body>
                        <p>Testando nosso servidor HTTP!</p>
                        <p>Diretório: {self.path}</p>
                    </body>
                </html>
                """.encode() # Um pequeno trecho html codificado por padrão em UTF-8
            self.wfile.write(data) # Contém o fluxo de saída para gravar a reposta ao cliente.
        elif self.path == "/eventos":
            self.send_response(200)  # Adiciona o código HTTP 200, é a resposta de sucesso que indica que a requisição foi bem sucedida.
            self.send_header("Content-type","text/html; charset=utf-8")  # Adiciona dados ao cabeçalho HTTP, como o conteúdo retornado e a codificação.
            self.end_headers()  # Indica o fim do cabeçalho HTTP na reposta
            stylesheet = """
                <style>
                    table{border-collapse: collapse;}
                    td,th {
                        border: 1px solid #DDDDDD;
                        text-align: left;
                        padding: 8px
                    }
                </style>
            """
            eventos_html = ""
            for ev in eventos:
                eventos_html += f"""
                        <tr>
                            <td>{ev.id}</td> 
                            <td>{ev.nome}</td>
                            <td>{ev.local}</td>
                        </tr>
                    """
            data = f"""
                    <html>
                        <head>{stylesheet}</head>
                        <table>
                            <tr>
                                <th>ID</th>
                                <th>Nome</th>
                                <th>Local</th>
                            </tr>
                            {eventos_html}
                        </table>
                    </html>""".encode()  # Um pequeno trecho html codificado por padrão em UTF-8
            self.wfile.write(data)  # Contém o fluxo de saída para gravar a reposta ao cliente.
        elif self.path == "/api/eventos":
            self.send_response(200)  # Adiciona o código HTTP 200, é a resposta de sucesso que indica que a requisição foi bem sucedida.
            self.send_header("Content-type","application/json; charset=utf-8")  # Adiciona dados ao cabeçalho HTTP, como o conteúdo retornado e a codificação.
            self.end_headers()  # Indica o fim do cabeçalho HTTP na reposta
            dict_eventos = []
            for ev in eventos:
                dict_eventos.append({
                    "id": ev.id,
                    "nome": ev.nome,
                    "local": ev.local
                })
            data = json.dumps(dict_eventos).encode()
            self.wfile.write(data)


try:
    server = HTTPServer(('localhost', 8000), SimpleHandler) # Passa os parãmetros para iniciar o servidor, o primeiro é uma tupla com o endereço e a porta do servidor e o segundo um handler para tratar as requisições.
    server.serve_forever() # Inicia e mantém o servidor ativo.
except KeyboardInterrupt:
    print("Servidor Finalizado Pelo Usuário")