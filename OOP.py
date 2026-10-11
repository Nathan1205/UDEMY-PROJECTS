class PlayerCharacter():
    def __init__(self, name, age):
        self.name = name#atributos
        self.age = age
    

    def run(self):
        print("run")
        return 'done'

player1 = PlayerCharacter("Juansito",5)
player2 = PlayerCharacter('Juanita',8)
print(player1)
print(player2)

print(player1.run())

        