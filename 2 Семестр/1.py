import random
import tkinter as tk

def spin_wheel():
    prize = random.choice(players)
    result_label.config(text="{} выпал(а)!".format(prize))

root = tk.Tk()
root.title("Колесо Фортуны")

players = []
num_players = int(input("Введите количество игроков: "))
for i in range(num_players):
    player_name = input("Введите имя игрока {}: ".format(i+1))
    players.append(player_name)


spin_button = tk.Button(root, text="Крутить колесо", command=spin_wheel)
spin_button.pack(pady=20)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
