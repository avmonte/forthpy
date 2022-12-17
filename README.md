# forthcompilerpy

A final project for CS130: Computer Organization class at American University of Armenia, Fall 2022

Author: Gevorg Nersesian

Supervisor: Norayr Chilingaryan 

The initial goal is to develop a Forth compiler with Python with basic dictionary. 

***Usage***

Open a terminal windoe in a directory of your Forth file

Type ```python3 main.py [forthInputFileName].fs``` and press Enter to activate the compiler 

In your current working directory you will find a folder with the raw files and an executable of the inputted Forth script


***Dictionary***

Note, that Forth is stack-oriented.

Integers are just being pushed to the head of the stack

```+```, ```-```, ```*```: does the given operation on elements and pushes the result to the the head of the stack

```dup```: duplicates an element at the head of the stack

```swap```: swaps elements at the head of the stack

```drop```: drops one element from the head of the stack

```.h```: prints out an element from the head of the stack
