import json

class Evento:
    
    id = 1 # Atriubuto de Classe

    def __init__(self, nome, local = ""):
        self.nome = nome
        self.local = local
        self.id = Evento.id # Seta o valor do atributo de classe ao atributo de instância
        Evento.id += 1 # Para cada novo objeto, será incrementado 1 ao atributo de classe
    
    def imprime_informacoes(self):
        print(f"ID do Evento: {self.id}")
        print(f"Evento: {self.nome}")
        print(f"Local: {self.local}")
        print("=" * 100)
    
    def to_json(self):
        return json.dumps({
            "id": self.id,
            "nome": self.nome,
            "local": self.local
        })

    @staticmethod
    def calcula_limite_pessoas_area(area):

        if 5 <= area < 10:
            return 5
        elif 10 <= area < 20:
            return 15
        elif area >= 20:
            return 30
        else:
            return 0


    
    #@classmethod
    #def cria_evento_online(cls, nome):
        #evento = cls(nome, local = f"https://tamarcado.com.br/eventos?id={cls.id}")
        #return evento


 
#ev2 = Evento("Aula de GoLang", "Rio de Janeiro")


#ev2.imprime_informacoes()
#print("\n")

#ev_online = EventoOnLine.cria_evento_online("Live de Python")
#ev_online.imprime_informacoes()

#ev2_online = EventoOnLine.cria_evento_online("Live de GoLang")
#ev2_online.imprime_informacoes()



#print(Evento.calcula_limite_pessoas_area(18))

