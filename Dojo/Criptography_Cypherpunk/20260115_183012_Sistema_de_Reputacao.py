# Este código simula um sistema de reputação onde usuários podem verificar a reputação de outros através de atestados assinados. 
# Cada atestado é representado por um dicionário contendo o nome do atestador e a nota dada. 
# O código calcula a média das notas para determinar a reputação de um usuário. 
# Para rodar, não são necessárias bibliotecas externas.

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.atestados = []

    def adicionar_atestado(self, atestador, nota):
        self.atestados.append({'atestador': atestador, 'nota': nota})

    def verificar_reputacao(self):
        if not self.atestados:
            return "Sem atestados."
        media = sum(atestado['nota'] for atestado in self.atestados) / len(self.atestados)
        return f"A reputação de {self.nome} é {media:.2f}"

# Exemplo de uso
usuario = Usuario("Alice")
usuario.adicionar_atestado("Bob", 4.5)
usuario.adicionar_atestado("Carol", 5.0)
usuario.adicionar_atestado("Dave", 3.8)

print(usuario.verificar_reputacao())