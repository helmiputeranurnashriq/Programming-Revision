import random,sys

class Game:

    def __init__(self):
        self.score = 0
        self.exp = 0
        self.level = 1
        self.status = False
        self.win = 0
        self.lose = 0
        self.ties = 0
        self.bot_move = ''


    def bot_setup(self):
        random_number = random.randint(1,3)
        if random_number == 1:
            self.bot_move = 'b'
            return "Batu"

        elif random_number == 2:
            self.bot_move  = 'k'
            return "Kertas"
        
        elif random_number == 3:
            self.bot_move  = 'g'
            return "Gunting" 


    def exp_point(self):
        if self.exp >= 100:
            self.level += 1
            self.exp = 0
            print("Tahniah, tahap anda telah meningkat kepada tahap ", self.level)
            


    def game_process(self):
        while True:
            print("Kamu adalah tahap ",self.level)
            print("Jumlah Experience Point ",self.exp)
            print("Keputusan: {} Menang, {} Kalah, {} Seri".format(self.win, self.lose, self.ties))

            while True:
                print('Masukkan Langkah Anda: (b) Batu, (k) Kertas, (g) Gunting or (q)Keluar')
                playerMove = input("Tulis disini ...")
                if playerMove.lower() == 'q':
                    sys.exit()

                if playerMove == 'b' or playerMove == 'k' or playerMove == 'g':
                    break

                print('Masukkan salah satu pilihan berikut: b, k , g or q.')

            if playerMove == 'b':
                print("Batu lawan ... ")
            
            elif playerMove == 'k':
                print("Kertas lawan ... ")

            elif playerMove == 'g':
                print("Gunting lawan ... ")


            print(self.bot_setup())

            if playerMove == self.bot_move:
                print("Keputusan SERI!")
                self.ties = self.ties + 1
                self.exp += 5

            elif playerMove == 'b' and self.bot_move == 'g':
                print("Tahniah kamu MENANG ")
                self.win +=  1
                self.exp += 10

            elif playerMove == 'k' and self.bot_move == 'b':
                print("Tahniah kamu MENANG ")
                self.win +=  1
                self.exp += 10

            elif playerMove == 'g' and self.bot_move == 'k':
                print("Tahniah kamu MENANG! ")
                self.win +=  1
                self.exp += 10

            elif playerMove == 'b' and self.bot_move == 'k':
                print("Kamu TEWAS! ")
                self.lose += 1
                self.exp += 0

            elif playerMove == 'k' and self.bot_move == 'g':
                print("Kamu TEWAS! ")
                self.lose += 0

            elif playerMove == 'g' and self.bot_move == 'b':
                print("Kamu TEWAS! ")
                self.lose += 0
            
            self.exp_point()



if __name__ == '__main__':
    a = Game()
    a.game_process()
