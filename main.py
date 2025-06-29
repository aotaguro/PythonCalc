import tkinter as tk
from sympy import sympify, SympifyError


def on_click(symbol: str) -> None:
    """Append the clicked symbol to the calculator entry field."""
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)


def calculate() -> None:
    """Safely evaluate the expression using sympy and show the result."""
    expression = entry.get()
    try:
        result = sympify(expression).evalf()
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except (SympifyError, ZeroDivisionError):
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def clear() -> None:
    """Clear the calculator entry field."""
    entry.delete(0, tk.END)


# Step 1: Create the main application window
root = tk.Tk()
root.title("Calculator")

# Step 2: Create the display field
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=5,
                 relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Step 3: Define calculator button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 3)
]

# Step 4: Create buttons for digits and operations
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                       command=lambda t=text: on_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Step 5: Create equals (=) and clear (C) buttons
equals_button = tk.Button(root, text='=', width=5, height=2,
                          font=('Arial', 18), command=calculate)
equals_button.grid(row=4, column=2, padx=5, pady=5)

clear_button = tk.Button(root, text='C', width=22, height=2,
                         font=('Arial', 18), command=clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

# Step 6: Start the GUI event loop
root.mainloop()
