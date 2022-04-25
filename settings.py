import colors
import file

import random
import time
import tkinter as tk
import pygame
import pygame_widgets
from Game import oneplayer
from Game import twoplayer

# Game Window size
window_x = 720
window_y = 480
game_window = pygame.display.set_mode((window_x, window_y))

# Player 1 Standart Settings
snake_position = [100, 50]
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0

# Player 2 Standart Settings
snake_position2 = [100, 100]
snake_body2 = [[100, 100],
               [90, 100],
               [80, 100],
               [70, 100]
               ]
direction2 = 'RIGHT'
change_to2 = direction2
score2 = 0
# Game Standart Settings
snake_speed = 15
game_size = 10
root = tk.Tk()
fps = pygame.time.Clock()
nicknames = file.loadscore()
player = tk.StringVar()
root.destroy()
Button = 1
counter = 0
active = 0
Multiplayer = False
color = colors.color
color2 = colors.color2
pycolor = pygame.Color(colors.green)
pycolor2 = pygame.Color(colors.cyan)


# Changing Settings
def settings(setting, value):
    global snake_speed
    global game_size
    global Button
    global color
    global color2
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    global counter
    global Multiplayer
    global pycolor
    global pycolor2
    global powerups
    global active
    # Changing Snake Speed
    if setting == 0:
        snake_speed = value
    # Changing Snake Size
    elif setting == 1:
        game_size = value
    # Changing Steering Buttons
    elif setting == 2:
        Button = value
    # Color channging for Button and snake for each player
    elif setting == 3:
        color = random.choice(colors.colors)
        color2 = random.choice(colors.colors)
        if color == pycolor:
            color = random.choice(colors.colors)
        elif color2 == pycolor:
            color2 = random.choice(colors.colors)
        elif pycolor == pycolor2:
            color = random.choice(colors.colors)
        pycolor = pygame.Color(color)
        pycolor2 = pygame.Color(color2)
        if value == 0:
            b.destroy()
            b = tk.Button(root, text='', command=lambda: settings(3, 0), background=colors.from_rgb(color), height=2,
                          width=4)
            b.grid(row=9, column=7)
        elif value == 1:
            if Multiplayer:
                c.destroy()
                c = tk.Button(root, text='', command=lambda: settings(3, 1), background=colors.from_rgb(color2),
                              height=2,
                              width=4)
                c.grid(row=9, column=9, columnspan=1)
    elif setting == 4:
        counter += 1
        if counter % 2:
            # Deactivate Buttons and enable Player 2 Settings
            Multiplayer = True
            a.configure(background=colors.from_rgb(colors.gray))
            h.configure(background=colors.from_rgb(colors.gray))
            i.configure(background=colors.from_rgb(colors.gray))
            c = tk.Button(root, text='', command=lambda: settings(3, 1), background=colors.from_rgb(colors.cyan),
                          height=2, width=4)
            c.grid(row=9, column=9, columnspan=1)
            d = tk.Label(root, text="Player 1:")
            d.grid(row=4, column=2)
            e = tk.Label(root, text="Player 2:")
            e.grid(row=4, column=4)
            f = tk.Label(root, text="Player 1:")
            f.grid(row=8, column=7)
            g = tk.Label(root, text="Player 2:")
            g.grid(row=8, column=9)
        else:
            # Activate Buttons and remove Player 2 Settings
            a.configure(background="white")
            h.configure(background=colors.from_rgb(colors.standard))
            i.configure(background=colors.from_rgb(colors.standard))
            c.destroy()
            d.destroy()
            e.destroy()
            f.destroy()
            g.destroy()
            Multiplayer = False


# Building the Settings Window
def settings_window():
    global a
    global b
    global h
    global i
    global root
    global player
    pygame.quit()
    time.sleep(1)
    pygame.init()
    root = tk.Tk()
    player = tk.StringVar()
    root.title('Snake Settings')
    root.tk.call('wm', 'iconphoto', root._w,
                 tk.PhotoImage(file='ressources/Snake.ico'))
    root.resizable(False, False)
    root.geometry('{}x{}'.format(window_x, window_y))
    tk.Label(root, text="Luke's version of Snake",
             font=("Helvetica", 20)).grid(row=0, column=0)
    tk.Label(root, text="Snake Speed:").grid(row=1, column=0)
    tk.Button(root, text="Easy", command=lambda: settings(
        0, 10)).grid(row=1, column=2)
    tk.Button(root, text="Normal", command=lambda: settings(
        0, 20)).grid(row=1, column=3)
    tk.Button(root, text="Hard", command=lambda: settings(
        0, 30)).grid(row=1, column=4)
    tk.Label(root, text="Snake Size:").grid(row=2, column=0)
    tk.Button(root, text="Small", command=lambda: settings(
        1, 7.5)).grid(row=2, column=2)
    tk.Button(root, text="Normal", command=lambda: settings(
        1, 10)).grid(row=2, column=3)
    tk.Button(root, text="Big", command=lambda: settings(
        1, 15)).grid(row=2, column=4)
    tk.Label(root, text="Nickname:").grid(row=3, column=0)
    a = tk.Entry(root, textvariable=player)
    a.grid(row=3, column=1, columnspan=4)
    tk.Label(root, text="Buttons:").grid(row=5, column=0)
    h = tk.Button(root, text="WASD", command=lambda: settings(2, 0))
    h.grid(row=5, column=2)
    i = tk.Button(root, text="Arrows", command=lambda: settings(2, 1))
    i.grid(row=5, column=4)
    tk.Label(root, text="Two Player Mode:").grid(row=7, column=0)
    tk.Checkbutton(root, text="", command=lambda: settings(4, 0)
                   ).grid(row=7, column=2)
    tk.Button(root, text="Start Game", command=start_game).grid(
        row=9, column=2, columnspan=2)
    tk.Button(root, text='Quit', command=quit).grid(row=9, column=4)
    b = tk.Button(root, text=' ', command=lambda: settings(3, 0), background=colors.from_rgb(colors.green), height=2,
                  width=4)
    b.grid(row=9, column=7)
    root.mainloop()


# Starting the Game and setting Colors for the Snakes
def start_game():
    global nicknames
    global game_window
    global root
    nicknames = file.loadscore()
    root.destroy()
    game_window = pygame.display.set_mode((window_x, window_y))
    game_window.fill(pygame.Color(colors.black))
    pygame.init()
    gameIcon = pygame.image.load('ressources/Snake.ico')
    pygame.display.set_icon(gameIcon)
    pygame_widgets.update(pygame.event.get())
    pygame.closeable = False
    pygame.display.update()
    fps.tick(snake_speed)
    pygame_widgets.update(fps)
    reset(snake_speed, game_size, pycolor, pycolor2)


# Reseting the changed values to the settings
def reset(snake_speed, game_size, pycolor, pycolor2):
    # Player 1 Settings Reset
    snake_position = [100, 50]
    snake_body = [[100, 50],
                  [90, 50],
                  [80, 50],
                  [70, 50]
                  ]
    direction = 'RIGHT'
    change_to = direction
    score = 0
    # Player 2 Settings Reset
    snake_position2 = [100, 100]
    snake_body2 = [[100, 100],
                   [90, 100],
                   [80, 100],
                   [70, 100]
                   ]
    direction2 = 'RIGHT'
    change_to2 = direction2
    score2 = 0
    # Fruit/Apple/Berry
    fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                      random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True
    # Power-Ups
    if Multiplayer:
        twoplayer(change_to, direction, fruit_position, fruit_spawn, snake_speed, score, snake_position, snake_body,
                  game_size,
                  pycolor, Multiplayer, change_to2, direction2, score2, snake_position2, snake_body2, pycolor2)
    if not Multiplayer:
        oneplayer(change_to, direction, fruit_position, fruit_spawn, snake_speed, score, snake_position, snake_body,
                  game_size,
                  pycolor, Multiplayer, change_to2, direction2, score2, snake_position2, snake_body2, pycolor2)


# Back to menu and resetting the settings
def reset_menu():
    global snake_position
    global snake_position2
    global snake_body
    global snake_body2
    global change_to
    global change_to2
    global score
    global score2
    global counter
    global a, b, c, d, e, f, g, h, i
    global root
    global Multiplayer
    global fruit_position
    global fruit_spawn
    # Player 1 Settings Reset
    snake_position = [100, 50]
    snake_body = [[100, 50],
                  [90, 50],
                  [80, 50],
                  [70, 50]
                  ]
    direction = 'RIGHT'
    change_to = direction
    score = 0
    # Player 2 Settings Reset
    snake_position2 = [100, 100]
    snake_body2 = [[100, 100],
                   [90, 100],
                   [80, 100],
                   [70, 100]
                   ]
    direction2 = 'RIGHT'
    change_to2 = direction2
    score2 = 0
    counter = 0
    Multiplayer = False
    settings_window()
