# forthcompilerpy

An on-going project for CS130: Computer Organization class at American University of Armenia, Fall 2022

Author: Gevorg Nersesian

Supervisor: Norayr Chilingaryan 

The initial goal is to develop a Forth compiler with Python with basic dictionary. 

***Usage***

Open a terminal windoe in a directory of yout forth file

Use this ```python3 main.py [forthInputFileName].fs``` to activate the compiler 

In your currecnt working directory you will find a folder with the raw files ans an executable of the inputted forth script


***Dictionary***

Note, that Forth is stack-oriented.

Integers are just being pushed to the head of the stack

```+```, ```-```, ```*```: does the given operation on elements and pushes the result to the the head of the stack

```dup```: duplicates an element at the head of the stack

```swap```: swaps elements at the head of the stack

```drop```: drops one element from the head of the stack

```.h```: prints out an element at the head of the stack
