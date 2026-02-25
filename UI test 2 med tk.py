import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()

class Player:
    def __init__(self, name, level, strength, player_class, gender, gold):
        self.name = name
        self.level = 1
        self.strength = 0
        self.player_class = player_class
        self.gender = gender
        self.gold = 0
        
    def change_level(self, amount):
        if self.level + amount > 0:
            self.level += amount

    def change_strength(self, amount):
        if self.strength + amount > 0:
            self.strength += amount

    def change_gold(self, amount):
        if self.gold + amount > 0:
            self.gold += amount
            
placeholder_text = "Vælg en"
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
        self.strength_var = tk.StringVar()
        self.player_class_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.gold_var = tk.StringVar()

        self.root.bind('<Return>', self.add_player)
        self.create_input_section()
        self.create_table()
        self.create_update_buttons()

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
        columns = ("Navn", "Level", "Strength", "Class", "Gender", "Gold")

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
        gold = self.gold_var.get().strip()

        # Tjek om felterne er udfyldt (hvis du tilføjer level/strength inputs, kan de også tilføjes her)
        if not name or not player_class or name =="Vælg en" or gender =="Vælg en":
            messagebox.showwarning("Fejl", "Udfyld venligst alle felter før du tilføjer en spiller!")
            return

        player = Player(
            self.name_var.get(),
            self.level_var.get(),
            self.strength_var.get()or 1,
            self.player_class_var.get() or 0,
            self.gender_var.get(),
            self.gold_var.get() or 0
        )

        self.players.append(player)
        self.refresh_table()

        # Ryd felter
        self.name_var.set("")
        self.level_var.set("")
        self.strength_var.set("")
        self.player_class_var.set(placeholder_text)
        self.gender_var.set(placeholder_text)
        self.gold_var.set("")



#================
#Knapper + -
#===============
    def create_update_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Button(frame, text="Level +", command=lambda: self.update_stat("level", +1)).grid(row=0, column=0)
        tk.Button(frame, text="Level -", command=lambda: self.update_stat("level", -1)).grid(row=0, column=1)

        tk.Button(frame, text="Strength +", command=lambda: self.update_stat("strength", +1)).grid(row=1, column=0)
        tk.Button(frame, text="Strength -", command=lambda: self.update_stat("strength", -1)).grid(row=1, column=1)

        tk.Button(frame, text="Gold +", command=lambda: self.update_stat("gold", +100)).grid(row=2, column=0)
        tk.Button(frame, text="Gold -", command=lambda: self.update_stat("gold", -100)).grid(row=2, column=1)
        
    def update_stat(self, stat, amount):
        selected = self.table.selection()
        if not selected:
            return

        index = self.table.index(selected[0])
        player = self.players[index]

        if stat == "level":
            player.change_level(amount)
        elif stat == "strength":
            player.change_strength(amount)
        elif stat == "gold":
            player.change_gold(amount)

        self.refresh_table()

    def refresh_table(self):
        for row in self.table.get_children():
            self.table.delete(row)

        for p in self.players:
            self.table.insert("", "end", values=(
                p.name, p.level, p.strength, p.player_class, p.gender, p.gold
            ))

app = ScoreboardApp(root)
root.mainloop()

