import pygame


# define a function to load a sound
def play_audio(file_name):
    pygame.init()  # initiate the module

    music = pygame.mixer.Sound(file_name)
    music.play()  # play the sound

    # get the length of the sound in seconds and multiplicate to get milliseconds
    pygame.time.wait(int(music.get_length() * 1000))
    pygame.quit()


play_audio("file_name")
