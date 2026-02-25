import tkinter as tk
from tkinter import ttk, messagebox
import game_logic as logic
from functools import partial

# UI State variables
root_window = None
placeholder_text = ""
available_classes = []
available_genders = []

# Tkinter Variables
name_var = None
player_class_var = None
gender_var = None
table = None

def setup_ui(root, placeholder, classes, genders):
    global root_window, placeholder_text, available_classes, available_genders
    global name_var, player_class_var, gender_var
    
    root_window = root
    placeholder_text = placeholder
    available_classes = classes
    available_genders = genders

    # Initialize Tkinter variables attached to the root
    name_var = tk.StringVar()
    player_class_var = tk.StringVar()
    gender_var = tk.StringVar()

    root_window.bind('<Return>', add_player)
    
    create_input_section()
    create_table()
    create_update_buttons()
    
    refresh_table()

def create_input_section():
    frame = tk.Frame(root_window)
    frame.pack(pady=10)

    tk.Label(frame, text="Navn:").grid(row=0, column=0)
    tk.Entry(frame, textvariable=name_var).grid(row=0, column=1)

    tk.Label(frame, text="Class:").grid(row=3, column=0)
    player_class_var.set(placeholder_text)
    ttk.Combobox(frame, textvariable=player_class_var, values=available_classes, state="readonly").grid(row=3, column=1)

    tk.Label(frame, text="Gender:").grid(row=4, column=0)
    gender_var.set(placeholder_text)
    ttk.Combobox(frame, textvariable=gender_var, values=available_genders, state="readonly").grid(row=4, column=1)

    tk.Button(frame, text="Tilføj spiller", command=add_player).grid(row=5, column=0, columnspan=2, pady=5)

def create_table():
    global table
    columns = ("Navn", "Level", "Strength", "Class", "Gender", "Gold")

    tree_frame = tk.Frame(root_window)
    tree_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    table = ttk.Treeview(tree_frame, columns=columns, show="headings", height=8)

    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=100)

    scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=table.yview)
    table.configure(yscroll=scrollbar.set)
    
    table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

def add_player(event=None):
    name = name_var.get().strip()
    player_class = player_class_var.get().strip()
    gender = gender_var.get().strip()

    if player_class == placeholder_text or gender == placeholder_text or not logic.add_player(name, player_class, gender):
        messagebox.showwarning("Fejl", "Udfyld venligst alle felter før du tilføjer en spiller!")
        return

    refresh_table()

    name_var.set("")
    player_class_var.set(placeholder_text)
    gender_var.set(placeholder_text)

def create_update_buttons():
    frame = tk.Frame(root_window)
    frame.pack(pady=10)

    tk.Button(frame, text="Level +", command=partial(update_stat, "level", +1)).grid(row=0, column=0)
    tk.Button(frame, text="Level -", command=partial(update_stat, "level", -1)).grid(row=0, column=1)

    tk.Button(frame, text="Strength +", command=partial(update_stat, "strength", +1)).grid(row=1, column=0)
    tk.Button(frame, text="Strength -", command=partial(update_stat, "strength", -1)).grid(row=1, column=1)

    tk.Button(frame, text="Gold +", command=partial(update_stat, "gold", +100)).grid(row=2, column=0)
    tk.Button(frame, text="Gold -", command=partial(update_stat, "gold", -100)).grid(row=2, column=1)
    
def update_stat(stat, amount):
    selected = table.selection()
    if not selected:
        return

    index = table.index(selected[0])
    logic.update_player_stat(index, stat, amount)
    refresh_table()

    children = table.get_children()
    if index < len(children):
        table.selection_set(children[index])

def refresh_table():
    for row in table.get_children():
        table.delete(row)

    for p in logic.get_players():
        table.insert("", "end", values=(
            p.name, p.level, p.strength, p.player_class, p.gender, p.gold
        ))
