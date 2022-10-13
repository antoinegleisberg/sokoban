from cx_Freeze import setup,Executable

setup(name="Sokoban", version="0.1",
description = "Un jeu de sokoban", executables = [Executable("sokoban.py")])
