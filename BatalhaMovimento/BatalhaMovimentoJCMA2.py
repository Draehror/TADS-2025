Partes = ['Os pés,', ' as pernas,', ' o bumbum', 'Os braços,', ' a cabeça', ' o nariz', ' e agora o corpo todo']
frase = ""

for i in range(7):
    print('Essa é a batalha do movimento\nEssa é a batalha do movimento\nMexendo '+Partes[i].rstrip(',').lower().strip()+' sem parar um momento\nMexendo '+Partes[i].rstrip(',').lower().strip()+' sem parar um momento')
    frase = frase + Partes[i] 
    if i == 2: 
        frase = frase + "\n"
    print(frase)
    print('Yeah!\nÉ isso ai!\nTodos dançando sem parar, uh!\n')

print('Muito bem, vocês são os melhores! Uh!')