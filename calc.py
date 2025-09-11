import math
import os
import json
from datetime import datetime
import sympy as sp


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HISTORY_FILE = os.path.join(BASE_DIR, "history.json")

x, y, z = sp.symbols("x y z")
variables = {"x": x, "y": y, "z": z}


safe = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "pi": math.pi
}


try:
    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    history = []


while True:
    raw = input("Enter arithmetic expression here: (or type Q to quit; ? for commands) ").strip()


    if raw.lower() in ("q", "quit"):
        print("Goodbye.")
        break


    if raw.lower() in ("help", "?"):
        print("""
Available commands:
  [expression]   -> evaluate arithmetic (e.g. 5+5, 3^2, sqrt(16))
  H or history   -> show calculation history
  RH             -> remove last history entry
  CH             -> clear all history
  Q or quit      -> exit the calculator
        """)
        continue


    if raw.lower() in ("h", "history"):
        if not history:
            print("No history yet. Do some calculations!")
        else:
            for num, entry in enumerate(history, start=1):
                print(f"{num}. {entry['time']} - {entry['expr']} = {entry['result']}")
        continue


    if raw.lower() == "rh":
        if history:
            removed = history.pop()
            print(f"Removed last entry: {removed['expr']} = {removed['result']}")
        else:
            print("No history to remove.")
        continue


    if raw.lower() == "ch":
        history.clear()
        print("History cleared.")
        continue

    if "=" in raw:
        try:

            solve_for = input("Which variable do you want to solve for? (x, y, z): ").strip().lower()
            if solve_for not in variables:
                print("Unsupported variable. Choose from x, y, z.")
                continue

            left_str, right_str = raw.split("=", 1)

            left_norm = left_str.replace("^", "**").replace("÷", "/").replace("√", "sqrt")
            right_norm = right_str.replace("^", "**").replace("÷", "/").replace("√", "sqrt")


            sympy_locals = {
                **variables,
                "sin": sp.sin,
                "cos": sp.cos,
                "sqrt": sp.sqrt,
                "pi": sp.pi
            }


            left_expr = sp.sympify(left_norm, locals=sympy_locals)
            right_expr = sp.sympify(right_norm, locals=sympy_locals)


            equation = sp.Eq(left_expr, right_expr)
            solutions = sp.solve(equation, variables[solve_for])
            print(f"Solution(s) for {solve_for}:", solutions)

        except Exception as error:
            print("Error solving equation:", error)
        continue



    if raw.strip().endswith(("+", "-", "*", "/", "^")):
        print("Malformed expression. Can't end with an operator. Try again.")
        continue


    expression = (
        raw
        .replace("^", "**")
        .replace("x", "*")
        .replace("÷", "/")
        .replace("√", "sqrt")
    )


    try:
        result = eval(expression, {"__builtins__": None}, safe)
        print(f"Result: {result}")
    except Exception as error:
        print("Error:", error)
        continue


    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append({"time": now, "expr": raw, "result": result})


    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)
