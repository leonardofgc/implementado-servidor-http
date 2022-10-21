from evento import Evento
class EventoOnLine(Evento):
    
    def __init__(self, nome, _ = ""):
        local = f"https://tamarcado.com.br/eventos?id={EventoOnLine.id}"
        #Evento.__init__(self, nome, local)
        super().__init__(nome,local)

    def imprime_informacoes(self):
        print(f"ID do Evento: {self.id}")
        print(f"Evento: {self.nome}")
        print(f"Link: {self.local}")
        print("=" * 100)