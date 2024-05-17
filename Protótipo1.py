import random


class Carta:
    def __init__(self, nome, atributos):
        self.nome = nome
        self.atributos = atributos

    def __repr__(self):
        return f"{self.nome}: {self.atributos}"

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.cartas = []

    def adicionar_carta(self, carta):
        self.cartas.append(carta)

    def jogar_carta(self):
        return self.cartas.pop(0) if self.cartas else None

    def receber_cartas(self, cartas):
        self.cartas += cartas

    def tem_cartas(self):
        return len(self.cartas) > 0

    def mostrar_cartas(self):
       
        print("\nSuas cartas:")
        for i, carta in enumerate(self.cartas):
            print(f"{i + 1}. {carta}")
    
    def escolher_carta(self):
        
        while True:
            try:
                escolha = int(input("\nEscolha a carta que deseja usar (digite o número correspondente): ")) - 1
                if 0 <= escolha < len(self.cartas):
                    return self.cartas.pop(escolha)
                else:
                    print("Número inválido. Por favor, escolha um número entre 1 e", len(self.cartas))
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")


class IA(Jogador):
    def escolher_atributo(self, carta):
       
        return max(carta.atributos, key=lambda k: carta.atributos[k])

class SuperTrunfo:
    def __init__(self, jogadores, baralho):
        self.jogadores = jogadores
        self.baralho = baralho
        self.distribuir_cartas()
        self.indice_jogador_atual = 0 

    def distribuir_cartas(self):
        random.shuffle(self.baralho)
        num_cartas = len(self.baralho)
        
        for i in range(num_cartas):
            jogador_atual = self.jogadores[i % len(self.jogadores)]
            jogador_atual.adicionar_carta(self.baralho[i])

    def iniciar_jogo(self):
        rodada = 1
        while any(jogador.tem_cartas() for jogador in self.jogadores):
            print(f"\nRodada {rodada}:")
            
            
            cartas_jogadas = []
            
            
            for jogador in self.jogadores:
                if jogador == self.jogadores[0]:
                    # Jogador humano
                    jogador.mostrar_cartas()
                    carta_jogador_humano = jogador.escolher_carta()
                    print(f"{jogador.nome} jogou: {carta_jogador_humano}")
                    cartas_jogadas.append((jogador, carta_jogador_humano))
                else:
                    
                    carta_ia = jogador.jogar_carta()
                    print(f"{jogador.nome} jogou: {carta_ia}")
                    cartas_jogadas.append((jogador, carta_ia))

           
            jogador_atual = self.jogadores[self.indice_jogador_atual]
            carta_jogador_atual = cartas_jogadas[self.indice_jogador_atual][1]
            if jogador_atual == self.jogadores[0]:
                
                atributo = self.escolher_atributo_jogador(carta_jogador_atual)
            else:
                
                atributo = jogador_atual.escolher_atributo(carta_jogador_atual)

            print(f"{jogador_atual.nome} escolheu o atributo: {atributo}")
            
          
            vencedor = None
            cartas_para_ganhar = []
            
            
            for jogador, carta in cartas_jogadas:
                valor_atributo = carta.atributos[atributo]
                if vencedor is None or valor_atributo > cartas_para_ganhar[0][1].atributos[atributo]:
                    vencedor = jogador
                    cartas_para_ganhar = [(jogador, carta)]
                elif valor_atributo == cartas_para_ganhar[0][1].atributos[atributo]:
                    cartas_para_ganhar.append((jogador, carta))
            
            if len(cartas_para_ganhar) > 1:
                print("A rodada foi um empate!")

                for jogador, carta in cartas_para_ganhar:
                    jogador.adicionar_carta(carta)
            else:
                print(f"{vencedor.nome} venceu a rodada!")
                vencedor.receber_cartas([carta for _, carta in cartas_jogadas])

            self.indice_jogador_atual = (self.indice_jogador_atual + 1) % len(self.jogadores)

            rodada += 1
        
        vencedor_final = None
        max_cartas = 0
        for jogador in self.jogadores:
            if len(jogador.cartas) > max_cartas:
                vencedor_final = jogador
                max_cartas = len(jogador.cartas)
        
        if vencedor_final:
            print(f"\nJogo terminado! {vencedor_final.nome} venceu o jogo com {len(vencedor_final.cartas)} cartas!")
        else:
            print("\nJogo terminou com empate!")

    def escolher_atributo_jogador(self, carta):
        print(f"Atributos da carta jogada: {carta.atributos}")
        
        while True:
            atributo = input("Escolha um atributo para comparar: ").strip().lower()
            if atributo in carta.atributos:
                return atributo
            else:
                print("Atributo inválido. Por favor, escolha um atributo válido entre os seguintes: " + ", ".join(carta.atributos))

if __name__ == '__main__':
    baralho = [
        Carta("Carro A", {"velocidade": 220, "potencia": 150, "peso": 1200, "consumo": 12}),
        Carta("Carro B", {"velocidade": 200, "potencia": 180, "peso": 1300, "consumo": 15}),
        Carta("Carro C", {"velocidade": 230, "potencia": 200, "peso": 1100, "consumo": 10}),
        Carta("Carro D", {"velocidade": 210, "potencia": 160, "peso": 1250, "consumo": 14}),
        Carta("Carro E", {"velocidade": 240, "potencia": 220, "peso": 1150, "consumo": 11}),
        Carta("Carro F", {"velocidade": 190, "potencia": 170, "peso": 1350, "consumo": 13}),
        Carta("Carro G", {"velocidade": 250, "potencia": 230, "peso": 1050, "consumo": 9}),
        Carta("Carro H", {"velocidade": 205, "potencia": 175, "peso": 1400, "consumo": 16}),
        Carta("Carro I", {"velocidade": 225, "potencia": 200, "peso": 1150, "consumo": 11}),
        Carta("Carro J", {"velocidade": 200, "potencia": 165, "peso": 1200, "consumo": 14}),
        Carta("Carro K", {"velocidade": 210, "potencia": 185, "peso": 1300, "consumo": 13}),
        Carta("Carro L", {"velocidade": 215, "potencia": 180, "peso": 1250, "consumo": 12}),
        Carta("Carro M", {"velocidade": 235, "potencia": 190, "peso": 1100, "consumo": 10}),
        Carta("Carro N", {"velocidade": 225, "potencia": 220, "peso": 1150, "consumo": 12}),
        Carta("Carro O", {"velocidade": 195, "potencia": 175, "peso": 1200, "consumo": 14}),
        Carta("Carro P", {"velocidade": 210, "potencia": 200, "peso": 1350, "consumo": 13}),
        Carta("Carro Q", {"velocidade": 240, "potencia": 230, "peso": 1050, "consumo": 9}),
        Carta("Carro R", {"velocidade": 205, "potencia": 165, "peso": 1200, "consumo": 14}),
        Carta("Carro S", {"velocidade": 230, "potencia": 185, "peso": 1150, "consumo": 10}),
        Carta("Carro T", {"velocidade": 220, "potencia": 190, "peso": 1200, "consumo": 11}),
        Carta("Carro U", {"velocidade": 200, "potencia": 160, "peso": 1250, "consumo": 14}),
        Carta("Carro V", {"velocidade": 210, "potencia": 180, "peso": 1100, "consumo": 12}),
        Carta("Carro W", {"velocidade": 240, "potencia": 200, "peso": 1300, "consumo": 10}),
        Carta("Carro X", {"velocidade": 215, "potencia": 170, "peso": 1200, "consumo": 15}),
        Carta("Carro Y", {"velocidade": 230, "potencia": 220, "peso": 1150, "consumo": 11}),
        Carta("Carro Z", {"velocidade": 210, "potencia": 180, "peso": 1200, "consumo": 12}),
        Carta("Carro AA", {"velocidade": 240, "potencia": 230, "peso": 1050, "consumo": 10}),
        Carta("Carro BB", {"velocidade": 200, "potencia": 175, "peso": 1200, "consumo": 13}),
        Carta("Carro CC", {"velocidade": 230, "potencia": 210, "peso": 1150, "consumo": 10}),
        Carta("Carro DD", {"velocidade": 205, "potencia": 185, "peso": 1300, "consumo": 12}),
        Carta("Carro EE", {"velocidade": 215, "potencia": 170, "peso": 1250, "consumo": 14}),
        Carta("Carro FF", {"velocidade": 225, "potencia": 190, "peso": 1100, "consumo": 11}),
        Carta("Carro GG", {"velocidade": 235, "potencia": 220, "peso": 1200, "consumo": 12})
        
    ]

    
    jogador = Jogador("Jogador Humano")
    ia1 = IA("IA 1")
    ia2 = IA("IA 2")
    ia3 = IA("IA 3")
    
    jogadores = [jogador, ia1, ia2, ia3]

    
    jogo = SuperTrunfo(jogadores, baralho)
    
    
    jogo.iniciar_jogo()


