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

  def receber_ataque(self, dano):
    self.__vida -= dano
    if self.__vida < 0:
      self.__vida = 0 
  
  def ataque(self, alvo):
    dano = self.__nivel * 2
    alvo.receber_ataque(dano)
    print(f"\n{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")
  
class Heroi(Personagem):
  def __init__(self, nome, vida, nivel, habilidade):
    super().__init__(nome, vida, nivel)
    self.__habilidade = habilidade

  def get_habilidade(self):
    return self.__habilidade
  
  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"

  def ataque_especial(self, alvo):
    dano = self.get_nivel() * 4
    alvo.receber_ataque(dano)
    print(f"{self.get_nome()} usou habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} dano!")
  
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
    self.heroi = Heroi(nome = "Ichigo Kurosaki", vida = 120, nivel = 12, habilidade = "Ataque Vasto Lorde")
    self.inimigo = Inimigo(nome = "Grimmjow", vida = 110, nivel = 8, tipo = "Hollow - Espada")

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

      if escolha == '1':
         self.heroi.ataque(self.inimigo)
      elif escolha == '2':
        self.heroi.ataque_especial(self.inimigo)
      else:
        print("Escolha inválida! Selecione a correta!")

      if self.heroi.get_vida() > 0:
        self.inimigo.ataque(self.heroi)

    if self.heroi.get_vida() > 0:
      print(f"\nParabéns o {self.heroi.get_nome()} ganhou a batalha!")
    else:
      print("\nO seu herói foi derrotado!")


# Criação da instância e execução do método início de batalha.
jogo = Jogo()
jogo.iniciar_batalha()