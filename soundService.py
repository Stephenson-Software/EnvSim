import pygame


#  @author Daniel McCoy Stephenson
#  @since August 5th, 2022
class SoundService:
    def __init__(self):
        self.reproduceSoundEffect = pygame.mixer.Sound("pop.wav")
        self.deathSoundEffect = pygame.mixer.Sound("death.mp3")

        self.reproduceSoundEffect.set_volume(0.2)
        self.deathSoundEffect.set_volume(0.2)

    def playReproduceSoundEffect(self):
        pygame.mixer.Sound.play(self.reproduceSoundEffect)
    
    def playDeathSoundEffect(self):
        pygame.mixer.Sound.play(self.deathSoundEffect)