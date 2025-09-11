. READ.ME && UPDATE LOG

sympy *IS* required for this to work.

If you are using Linux:

1) Open the Terminal and type "mkdir ~/StMaryCalc".
2) Then use the "cp" command to copy the calculator over to the new folder you made with the command "cp ~/Downloads/calc.py ~/StMaryCalc". 
3) Finally, "cd" into the StMaryCalc folder and type "pip install sympy" to install dependencies.
4) Go ahead and type "python3 calc.py"

If you are using Windows:
1) Make a folder for the calculator and drag "calc.py" into it.
2) Right-click anywhere inside the folder and click "Open in Terminal"
3) Now type "pip install sympy" to install dependencies.
4) Run the calculator with "python3 calc.py"

Changes from StMaryCalcV1: 
* Rewrote as an interactive terminal (users can type expressions directly without manually inputting operations and numbers one at a time.) 
* Supports new functions/constants, like "√", and cos, and pi. 
* Added calculation history! H to show History, RH to remove the last entry, and CH to clear the history. 
* History saves in a local history.json file that gets saved into with every calculation. 
* Added algebra solving capabilities with Sympy. Enter equations like "2*x + 3 = 9" and choose which variable to solve for!

Planned features for V3:
Basic calculus/trig support
GUI experiments with Tkinter
