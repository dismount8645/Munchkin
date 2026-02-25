import tkinter as tk
from tkinter import ttk

root = tk.Tk()

class Player:
    def __init__(self, name, level, strenght, p_class, gender):
        self.name = name
        self.level = level
        self.strength = strenght
        self.p_class = p_class
        self.gender = gender

#==================
#===SCOREBOARD=====
#==================

class ScoreboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Player Menu")

        self.players = []

        self.name_var = tk.StringVar()
        self.level_var = tk.StringVar()
        self.strenght_var = tk.StringVar()
        self.p_class_var = tk.StringVar()
        self.gender_var = tk.StringVar()

        self.create_input_section()
        self.create_table()

    #================================
    # Input sektioner for nye spillere
    #================================
    def create_input_section(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Navn:").grid(row=0, column=0)
        tk.Entry(frame, textvariable=self.name_var).grid(row=0, column=1)

        tk.Label(frame, text="Class:").grid(row=3, column=0)
        tk.Entry(frame, textvariable=self.p_class_var).grid(row=3, column=1)

        tk.Label(frame, text="Gender:").grid(row=4, column=0)
        tk.Entry(frame, textvariable=self.gender_var).grid(row=4, column=1)

        tk.Button(frame, text="Tilføj spiller", command=self.add_player).grid(row=5, column=0, columnspan=2, pady=5)

    #==================
    # Tabel (Treeview)
    #==================
    def create_table(self):
        columns = ("Navn", "Level", "Strength", "Class", "Gender")

        self.table = ttk.Treeview(self.root, columns=columns, show="headings", height=8)

        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=100)

        self.table.pack(pady=10)

    #===============
    # Tilføj spillere
    #===============
    def add_player(self):
        player = Player(
            self.name_var.get(),
            self.level_var.get(),
            self.strenght_var.get(),
            self.p_class_var.get(),
            self.gender_var.get()
        )

        self.players.append(player)

        self.table.insert("", "end", values=(
            player.name,
            player.level,
            player.strength,
            player.p_class,
            player.gender
        ))

        # Ryd felter
        self.name_var.set("")
        self.level_var.set("")
        self.strenght_var.set("")
        self.p_class_var.set("")
        self.gender_var.set("")
#On button pushed command mangler

app = ScoreboardApp(root)
root.mainloop()