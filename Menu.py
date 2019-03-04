import pygame
class Menu:
    def __init__(self, punkts):
        self.punkts = punkts

    def render(self, poverhnost, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]-30))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]-30))

    def menu(self):
        done = True
        font_menu = pygame.font.Font(None, 50)   # ШРИФТ!!!
        pygame.key.set_repeat(0,0)  #Вырубим повторение клавиш
        pygame.mouse.set_visible(True)
        punkt = 0

        while done:
            #info_string.fill((0, 100, 200))
            screen.fill((0, 100, 200))
            mp = pygame.mouse.get_pos()

            for i in self.punkts:
                if mp[0]>i[0] and mp[0]<i[0]+155 and mp[1]>i[1] and mp[1]<i[1]+50:
                    punkt = i[5]
                    self.render(screen, font_menu, punkt)

                    for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            sys.exit()
                        if e.type == pygame.KEYDOWN:
                            if e.key == pygame.K_ESCAPE:
                                sys.exit()

                            if e.key == pygame.K_UP:
                                if punkt > 0: punkt -= 1
                            if e.key == pygame.K_DOWN:
                                if punkt < len(self.punkts)-1:
                                     punkt += 1
                        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                            if punkt == 0:
                                done = False
                            elif punkt == 1:
                                sys.exit()

                                window.blit(info_string, (0, 0))
                                window.blit(screen, (0, 0))
                                pygame.display.flip()
