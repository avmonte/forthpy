# forthcompilerpy

A final project for CS130: Computer Organization, *American University of Armenia*, Fall 2022

Author: Gevorg Nersesian, gevorg_nersesyan@edu.aua.am    

Supervisor: Norayr Chilingaryan, nchilingaryan@aua.am



## Usage

In a terminal window of a directory with your Forth file, type
```bash
python3 main.py [inputFileName].fs
``` 

In your the directory you will find an executable of the inputted Forth script and a folder with the raw files (object and assembly files)a


## Dictionary

Integers are just being pushed to the head of the stack

```+```, ```-```, ```*```: does the given operation on elements and pushes the result to the the head of the stack

```dup```: duplicates an element at the head of the stack

```swap```: swaps elements at the head of the stack

```drop```: drops one element from the head of the stack

```.h```: prints out an element from the head of the stack
