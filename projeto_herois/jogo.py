# Estruturas de classes
# Personagem: Classe mãe, contém tudo que é comum entre os personais, herói ou inimigo.
# Herói: Herda tudo do personagem (controlado pelo usuário)
# Inimigo: Adversário do usuário

class Personagem:
  def __init__(self, nome, vida, nivel):
    self.__nome = nome
    self.__vida = vida
    self.__nivel = nivel
    
  def get_nome(self):
    return self.__nome
  
  def get_vida(self):
    return self.__vida
  
  def get_nivel(self):
    return self.__nivel
  
  def exibir_detalhes(self):
    return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"
  
class Heroi(Personagem):
  def __init__(self, nome, vida, nivel, habilidade):
    super().__init__(nome, vida, nivel)
    self.__habilidade = habilidade

  def get_habilidade(self):
    return self.__habilidade
  
  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"
  
class Inimigo(Personagem):
  def __init__(self, nome, vida, nivel, tipo):
    super().__init__(nome, vida, nivel)
    self.__tipo = tipo

  def get_tipo(self):
    return self.__tipo
  
  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n"

class Jogo:
  """Classe para a orquestração."""

  def __init__(self) -> None:
    self.heroi = Heroi(nome = "Ichigo Kurosaki", vida = 1200, nivel = 12, habilidade = "Ataque Vasto Lorde")
    self.inimigo = Inimigo(nome = "Grimmjow", vida = 1100, nivel = 10, tipo = "Hollow - Espada")

  def iniciar_batalha(self):
    """ Gerenciador de turnos. """
    print("\nInicio de batalha!")
    while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
      print("\nDetalhes do Herói:")
      print(self.heroi.exibir_detalhes())
      print("\nDetalhes do Inimigo:")
      print(self.inimigo.exibir_detalhes())
  
      input("Pressione Enter para iniciar...")
      escolha = input("Escolha o tipo de ataque: (1 - Ataque Normal, 2 - Ataque Especial): ")

# Criação da instância e execução do método início de batalha.
jogo = Jogo()
jogo.iniciar_batalha()