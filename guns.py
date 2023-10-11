import random


class GunGame:
    def __init__(self):#take it out and edit to now neet(IS POSSIBLE!!!!)
        self.user_bullets = 0
        self.comp_bullets = 0
        self.options = ["Load", "Shoot", "Block"]
        self.user_move = ""
        self.comp_move = ""
        self.user_alive = True
        self.comp_alive = True

    def instructions(self):

        print("Guns works in a very complex way.")
        print("We each choose one of the 3 options:")
        print("Load")
        print("Shoot")
        print("and Shield")
        print("In order to shoot, you need to load a bullet first. You can use shield as many times as you want.")
        print("The goal of the game is to shoot and kill the opposing player.")

    def user_pick(self):

        print("Alright, choose your option!")
        print("[Please write Load, Shoot, or Block!]")
        self.user_move = input("Input: ").title()

        if self.user_move == "Load":
            self.user_bullets += 1
            print("You load your gun!")
        elif self.user_move == "Shoot":
            if self.user_bullets >= 1:
                print("You shot a bullet!")
            elif self.user_bullets == 0:
                print("You do not have a bullet!")
        else:
            print("You block with your magical shield!")

    def comp_pick(self):
        self.comp_move = random.choice(self.options)
        if self.comp_move == "Load":
            self.comp_bullets += 1
        elif self.comp_move == "Shoot":
            if self.comp_bullets >= 1:
                print("The computer shot a bullet!")
            elif self.user_bullets == 0:
                print("The computer does not have a bullet, but tries to shoot it again!")
        else:
            print("The computer blocks with its magical shield!")

    def play_game(self):
        if self.user_move == "Load" and self.comp_move == "Load":
            print("Both of you load!")
            print("Congrats, you both live!")
        elif self.user_move == "Load" and self.comp_move == "Block":
            print("You load your gun as the computer blocks with its magic shield.")
        elif self.user_move == "Load" and self.comp_move == "Shoot":
            if self.comp_bullets == 0:
                print("The computer tries to shoot at you, but completely forgot that he didn't have a bullet in the first place!")
            elif self.comp_bullets >= 1:
                print("You see the computer aiming at your head and fires at you!")
                print("GAME OVER!")
                self.user_alive = False
        elif self.user_move == "Shoot" and self.comp_move == "Load":
            if self.user_bullets == 0:
                print("You aim your gun at the computer and attempt to fire your gun. However, it fizzes out as you realize that you never loaded the gun in the first place.")
            elif self.user_bullets >= 1:
                print("You aim your gun at the computer and shoot your bullet, killing it instantly!")
                print("YOU WIN!")
                self.comp_alive = False
        elif self.user_move == "Shoot" and self.comp_move == "Block":
            if self.user_bullets == 0:
                print("You aim your gun as the computer scrambles to make a magical shield. You pull the trigger...and you realize you never loaded the gun in the first place.")
            elif self.user_bullets >= 1:
                print("You aim your gun at the computer as it scrambles to make a magical shield. You fire the gun and hit its shield.")
                self.user_bullets -= 1
        elif self.user_move == "Shoot" and self.comp_move == "Shoot":
            if self.user_bullets and self.comp_bullets == 0:
                print("Both of you aim your guns at one another, in a standoff. You both shoot your guns...and nothing happens")
            elif self.user_bullets >= 1 and self.comp_bullets >= 1:
                print("Both of you aim your weapons at one another and know your faiths were sealed. You fired your guns and hoped for the best.")
                print("GAME OVER!")
                self.user_alive = False
            elif self.user_bullets == 0 and self.comp_bullets >= 1:
                print("You both aim your guns at one another, knowing well that you forgot to load your gun again while the computer did.")
                print("GAME OVER!")
                self.user_alive = False
            elif self.user_bullets >= 1 and self.comp_bullets == 0:
                print("You both aim your weapons at one another, in a standoff. You both shoot your weapons, but your gun was the only one loaded.")
                print("YOU WIN!")
                self.comp_alive = False
        elif self.user_move == "Block" and self.comp_move == "Load":
            print("You take the safer option and block while the computer quickly loads a bullet in")
        elif self.user_move == "Block" and self.comp_move == "Shoot":
            if self.comp_bullets == 0:
                print("The computer tries to shoot at you, but realizes it never loaded his gun in the first place.")
            elif self.comp_bullets >= 1:
                print("The computer is able to shoot at you, but you were able to block it with your shield!")
        elif self.user_move == "Block" and self.comp_move == "Block":
            print("Both of you choose to block and take the safest route")





    def start(self):
        self.instructions()
        while True:
            self.user_pick()
            self.comp_pick()
            self.play_game()
            if self.user_alive == False:#check if this works
                print("Do you want to play this game again?")
                play = input().title()
                if play == "Yes":
                    self.user_alive = True
                    self.comp_alive = True
                    self.user_bullets = 0
                    self.comp_bullets = 0
                else:
                    break
            if not self.comp_alive:
                print("Do you want to play the game again?")
                play = input().upper()
                if play == "Yes":
                    self.user_alive = True
                    self.comp_alive = True
                    self.user_bullets = 0
                    self.comp_bullets = 0
                else:
                    break




main()


