# Sound and Music
# Demonstrates playing sound and music files

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

# load a sound file
missle_sound = games.load_sound("missile.wav")

# load the music file
games.music.load("theme.mid")

choice = None
while choice != "0":

    print(
        """
        Sound and Music
        
    0 - Quit
    1- Play Missle Sound
    2 - Loop Missle Sound
    3 - Stop Missle sound
    4 - Play theme music
    5 - Loop theme music
    6 - Stop theme music
    """
    )

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye.")

    # play missle sound
    elif choice == "1":
        missle_sound.play()
        print("Playing missile sound.")

    # loop missle sound
    elif choice == "2":
        loop = int(input("Loop how many extra time? (-1 = forever): "))
        missle_sound.play(loop)
        print("Looping missile sound.")

    # stop missile sound
    elif choice == "3":
        missle_sound.stop()
        print("Stopping missile sound.")

    # play theme music
    elif choice == "4":
        games.music.play()
        print("Playing theme music.")

    # loop theme music
    elif choice == "5":
        loop = int(input("Loop how many extra times? (-1 = forever): "))
        games.music.play(loop)
        print("Looping theme music.")

    # stop theme music
    elif choice == "6":
        games.music.stop()
        print("Stopping theme music.")

    # some unknown choice
    else:
        print("\nSorry, but", choice, "isn't a valid choice.")

input("\n\nPress the enter key to exit.")

