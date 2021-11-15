from spirit_game.settings import *

class Board:

    def __init__(self, width: int, height: int):
        self.surface = pg.display.set_mode((width, height), 0, 32)
        pg.display.set_caption('The Curse Of Aegis')
        self.width = width
        self.height = height
        self.intro_bg = pg.image.load("images/intro1.jpg")
        my_font = "font/ArchitectsDaughter.ttf"
        self.menu_font = pg.font.Font(my_font, 45)
        self.bonus_font = pg.font.Font(my_font, 30)
        self.options_font = pg.font.Font(my_font, 65)
        self.title_font = pg.font.Font(my_font, 85)
        self.difficulty_font = pg.font.Font(my_font, 70)
        self.about_font = pg.font.Font(my_font, 20)
        self.game_over_font = pg.font.Font(my_font, 120)
        self.mute_font = pg.font.Font(my_font,30)

    def draw_menu(self, *args):
        self.intro_bg = pg.transform.scale(self.intro_bg, (self.width, self.height))
        self.surface.blit(self.intro_bg, (0, 0), (0, 0, self.width, self.height))
        self.draw_text(self.surface, "The Curse Of Aegis", self.width / 2, self.height * 0.25, self.title_font)
        self.draw_text(self.surface, "Play", self.width / 2, self.height * 0.4, self.menu_font)
        self.draw_text(self.surface, "About", self.width / 2, self.height * 0.5, self.menu_font)
        self.draw_text(self.surface, "Rules", self.width / 2, self.height * 0.6, self.menu_font)
        self.draw_text(self.surface, "Ranking", self.width / 2, self.height * 0.7, self.menu_font)
        self.draw_text(self.surface, "Settings", self.width / 2, self.height * 0.8, self.menu_font)
        self.draw_text(self.surface, "Quit", self.width / 2, self.height * 0.9, self.menu_font)
        for drawable in args:
            drawable.draw_on(self.surface)
        pg.display.update()

    def draw_rules(self, *args):
        self.intro_bg = pg.transform.scale(self.intro_bg, (self.width, self.height))
        self.surface.blit(self.intro_bg, (0, 0), (0, 0, self.width, self.height))
        self.draw_text(self.surface, "Rules:", self.width / 2, self.height * 0.1, self.difficulty_font)
        self.draw_text(self.surface, "1. Search for 3 keys in the whole map to open the door." , self.width/2, self.height * 0.25, self.about_font)
        self.draw_text(self.surface, "2. Collect coins to score more." , self.width/2-159, self.height * 0.30, self.about_font)
        self.draw_text(self.surface, "3. Fight with the spirits using the Space Bar." , self.width/2-80, self.height * 0.35, self.about_font)
        self.draw_text(self.surface, "4. Collect first-aid boxes to restore your energy." , self.width/2-50, self.height * 0.40, self.about_font)
        self.draw_text(self.surface, "5. Collect speedups to double your speed for 15 seconds." , self.width/2, self.height * 0.45, self.about_font)
        self.draw_text(self.surface, "6. Searching the fuel bottle is the end task." , self.width/2-80, self.height * 0.50, self.about_font)
        self.draw_text(self.surface, "7. Press 'p' to pause the game." , self.width/2-159, self.height * 0.55, self.about_font)
        self.draw_text(self.surface, "8. Press 'm' to mute and unmute the game." , self.width/2-90, self.height * 0.60, self.about_font)
        self.draw_text(self.surface, "9. Use '1', '2', '3' or '4' to change the guns." , self.width/2-100, self.height * 0.65, self.about_font)
        self.draw_text(self.surface, "Return", self.width / 2, self.height * 0.8, self.menu_font)
        for drawable in args:
            drawable.draw_on(self.surface)
        pg.display.update()

    def draw_options(self, *args):
        self.intro_bg = pg.transform.scale(self.intro_bg, (self.width, self.height))
        self.surface.blit(self.intro_bg, (0, 0), (0, 0, self.width, self.height))
        self.draw_text(self.surface, "Controls", self.width / 2, self.height * 0.35, self.options_font)
        self.draw_text(self.surface, "Audio", self.width / 2, self.height * 0.5, self.options_font)
        self.draw_text(self.surface, "Return", self.width / 2, self.height * 0.65, self.options_font)
        for drawable in args:
            drawable.draw_on(self.surface)
        pg.display.update()
    
    def draw_scoreboard(self, *args):
        self.intro_bg = pg.transform.scale(self.intro_bg, (self.width, self.height))
        self.surface.blit(self.intro_bg, (0, 0), (0, 0, self.width, self.height))
        self.draw_text(self.surface, "Leaderboard:", self.width / 2, self.height * 0.2, self.difficulty_font)
        pos = 0.35
        with open(SCOREBOARD) as f:
            for line in f:
                x = line.split()
                self.draw_text(self.surface, x[0], self.width / 3, self.height * pos, self.bonus_font)
                self.draw_text(self.surface, x[1], self.width * 2 / 3, self.height * pos, self.bonus_font)
                pos +=0.08
        self.draw_text(self.surface, "Return", self.width / 2, self.height * 0.8, self.menu_font)
        for drawable in args:
            drawable.draw_on(self.surface)
        pg.display.update()


    def draw_game_controls(self, *args):
        self.intro_bg = pg.transform.scale(self.intro_bg, (self.width, self.height))
        self.surface.blit(self.intro_bg, (0, 0), (0, 0, self.width, self.height))
        self.draw_text(self.surface, "Arrow Keys", self.width / 2, self.height * 0.6, self.menu_font)
        self.draw_text(self.surface, "W-A-S-D Keys", self.width / 2, self.height * 0.7, self.menu_font)
        self.draw_text(self.surface, "Quit", self.width / 2, self.height * 0.8, self.menu_font)
        for drawable in args:
            drawable.draw_on(self.surface)
        pg.display.update()
        pass

    def draw_audio_controls(self, *args):
        self.intro_bg = pg.transform.scale(self.intro_bg, (self.width, self.height))
        self.surface.blit(self.intro_bg, (0, 0), (0, 0, self.width, self.height))
        self.draw_text(self.surface, "Mute", self.width / 2, self.height * 0.6, self.menu_font)
        self.draw_text(self.surface, "Unmute", self.width / 2, self.height * 0.7, self.menu_font)
        self.draw_text(self.surface, "Quit", self.width / 2, self.height * 0.8, self.menu_font)
        for drawable in args:
            drawable.draw_on(self.surface)
        pg.display.update()
        pass

    def draw_about(self, *args):
        self.intro_bg = pg.transform.scale(self.intro_bg, (self.width, self.height))
        self.surface.blit(self.intro_bg, (0, 0), (0, 0, self.width, self.height))
        self.draw_text(self.surface, "About:", self.width / 2, self.height * 0.1, self.difficulty_font)
        self.draw_text(self.surface, "The ship named Aegis got cursed, and our sailor stuck is in an island populated with" , self.width/2, self.height * 0.25, self.about_font)
        self.draw_text(self.surface, "spirits. To return to his home, the sailor needs ship fuel. In search of ship fuel," , self.width/2, self.height * 0.30, self.about_font)
        self.draw_text(self.surface, "he enters a haunted laboratory filled with spirits and searches for the fuel. He" , self.width/2, self.height * 0.35, self.about_font)
        self.draw_text(self.surface, "needs to collect 3 keys scattered all over the place to reach the main room having." , self.width/2, self.height * 0.40, self.about_font)
        self.draw_text(self.surface, "the fuel. To achieve this, he needs to kill the spirits in his way because they will" , self.width/2, self.height * 0.45, self.about_font)
        self.draw_text(self.surface, "get attracted by the sailor and will lower his health. The player needs to help the" , self.width/2, self.height * 0.50, self.about_font)
        self.draw_text(self.surface, "sailor find the keys to the main door and collect the fuel to reach back his home." , self.width/2, self.height * 0.55, self.about_font)


        self.draw_text(self.surface, "Return", self.width / 2, self.height * 0.8, self.menu_font)
        for drawable in args:
            drawable.draw_on(self.surface)
        pg.display.update()
        pass
    def draw_game_over(self, scoreboard: list, message: str, *args):
        background = (0, 0, 0)
        self.surface.fill(background)
        self.draw_text(self.surface, message, self.width / 2, self.height * 0.2, self.game_over_font)
        self.draw_text(self.surface, "Players with the best scores :", self.width / 2, self.height * 0.4, self.menu_font)
        self.draw_text(self.surface, "Press 'q' to go to Main Screen", self.width / 2, self.height * 0.9, self.menu_font)
        pos = 0.5
        for player in scoreboard:
            self.draw_text(self.surface, player[0], self.width / 3, self.height * pos, self.bonus_font)
            self.draw_text(self.surface, player[1], self.width * 2 / 3, self.height * pos, self.bonus_font)
            pos += 0.08
        for drawable in args:
            drawable.draw_on(self.surface)
        pg.display.update()

    def draw_choosing_difficulty(self, *args):
        self.intro_bg = pg.transform.scale(self.intro_bg, (self.width, self.height))
        self.surface.blit(self.intro_bg, (0, 0), (0, 0, self.width, self.height))
        self.draw_text(self.surface, "Easy", self.width / 2, self.height * 0.2, self.difficulty_font)
        self.draw_text(self.surface, "Hard", self.width / 2, self.height * 0.4, self.difficulty_font)
        self.draw_text(self.surface, "Return", self.width / 2, self.height * 0.6, self.difficulty_font)
        for drawable in args:
            drawable.draw_on(self.surface)

        pg.display.update()

    def draw_input(self, word: str, x: int, y: int):
        self.surface.fill((0, 0, 0))
        self.draw_text(self.surface, "Please enter your name:", self.width / 2, self.height / 3, self.menu_font)
        text = self.menu_font.render("{}".format(word), True, MENU_FONT_COLOR)
        rect = text.get_rect()
        rect.center = x, y
        pg.display.update()
        return self.surface.blit(text, rect)

    def draw_pause(self):
        self.draw_text(self.surface, "Paused", self.width / 2, self.height / 3, self.title_font)
        self.draw_text(self.surface, "Press 'm' to Mute or Unmute", self.width / 2, self.height / 2, self.mute_font)

    def draw_spirits_left(self, left: int):
        self.draw_text(self.surface, "spirits: {}".format(left), self.width - 150, 25, self.bonus_font)

    def draw_bonus(self, bonus: str):
        self.draw_text(self.surface, bonus, self.width - 300, 25, self.bonus_font)

    def draw_ammo_quantity(self, ammo: str):
        self.draw_text(self.surface, ammo, 400, 25, self.bonus_font)

    def draw_coins_collected(self, coins):
        self.draw_text(self.surface, "Score : {}".format(coins) , 700, 25, self.bonus_font)

    def draw_money(self):
        self.draw_text(self.surface, "9 800 zl", self.width - 100, 60, self.bonus_font)

    @staticmethod
    def draw_adds(surface, x, y, image, amount=1):
        for i in range(amount):
            img_rect = image.get_rect()
            img_rect.x = x + 30 * i
            img_rect.y = y
            surface.blit(image, img_rect)

    @staticmethod
    def draw_text(surface, text, x, y, font):
        if text is not None:
            text = font.render(text, True, MENU_FONT_COLOR)
            rect = text.get_rect()
            rect.center = x, y
            surface.blit(text, rect)
