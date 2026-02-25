import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()

class Player:
    def __init__(self, name, level, strength, player_class, gender, gold):
        self.name = name
        self.level = int(level)
        self.strength = int(strenght)
        self.player_class = player_class
        self.gender = gender
        self.gold = gold
        
    def change_level(self, amount):
        if self.level + amount > 0:
            self.level += amount

    def change_strength(self, amount):
        if self.strength + amount > 0:
            self.strength += amount
 
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
        self.player_class_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.gold_var = tk.StringVar()

        self.root.bind('<Return>', self.add_player)
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
        self.player_class_var.set(placeholder_text)
        self.player_class_combobox = ttk.Combobox(frame, textvariable=self.player_class_var, values=["Officer", "Mechanic", "Wizard", "Warrior", "Rogue"], state="readonly").grid(row=3, column=1)

        tk.Label(frame, text="Gender:").grid(row=4, column=0)
        self.gender_var.set(placeholder_text)
        self.gender_combobox = ttk.Combobox(frame, textvariable=self.gender_var, values=["Male", "Female"], state="readonly").grid(row=4, column=1)

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
    def add_player(self, event=None):
        name = self.name_var.get().strip()
        player_class = self.player_class_var.get().strip()
        gender = self.gender_var.get().strip()

        # Tjek om felterne er udfyldt (hvis du tilføjer level/strength inputs, kan de også tilføjes her)
        if not name or not player_class or name =="Vælg en" or gender =="Vælg en":
            messagebox.showwarning("Fejl", "Udfyld venligst alle felter før du tilføjer en spiller!")
            return

        player = Player(
            self.name_var.get(),
            self.level_var.get(),
            self.strenght_var.get(),
            self.player_class_var.get(),
            self.gender_var.get(),
            self.gold_var.get()
        )

        self.players.append(player)

        self.table.insert("", "end", values=(
            player.name,
            player.level,
            player.strength,
            player.player_class,
            player.gender,
            player.gold
        ))

        # Ryd felter
        self.name_var.set("")
        self.level_var.set("")
        self.strenght_var.set("")
        self.player_class_var.set(placeholder_text)
        self.gender_var.set(placeholder_text)
#On button pushed command mangler

app = ScoreboardApp(root)
root.mainloop()