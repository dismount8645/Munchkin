# Munchkin

[![CI](https://github.com/dismount8645/Munchkin/actions/workflows/ci.yml/badge.svg)](https://github.com/dismount8645/Munchkin/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)

Board game companion tool for **Munchkin** — logic tracker, state manager, and UI helper for the card game.

## Features

- **Game Logic:** Turn, combat, and card resolution in \src/game_logic.py\
- **UI:** Tkinter/custom UI in \src/UI.py\ with flowchart visualization
- **Persistence:** Player saves in \players_save.json\
- **Extras:** Card index, combat system, deck management in \xtra_features/\

## Tech Stack

- **Language:** Python 3.11
- **UI:** Tkinter / custom
- **Data:** JSON saves, PNG flowcharts

## Project Structure

``text
Munchkin/
├── README.md
├── LICENSE
├── .github/
├── src/
│   ├── game_logic.py
│   ├── UI.py
│   ├── main.py
│   └── download_png.py
├── extra_features/
│   ├── card_index.py
│   ├── combat_system.py
│   └── deck.py
├── tests/                  # Future tests
└── docs/
    ├── game_flowchart.md
    └── game_flowchart.png
``

## Quick Start

``bash
git clone https://github.com/dismount8645/Munchkin.git
cd Munchkin
pip install -r requirements.txt  # if present
python src/main.py
``

## Usage

Run \python src/main.py\ to launch the companion UI. Game state is auto-saved to \players_save.json\.

## Development

- Place new features in \xtra_features/\ or \src/\
- Run \python -m py_compile src/*.py\ to verify

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE) © 2026 dismount8645 (dismount8645)

