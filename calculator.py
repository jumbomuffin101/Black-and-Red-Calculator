import tkinter as tk

def button_click(value):
    """Handle button clicks to append the clicked value to the entry field."""
    current = entry.get()  # Get the current text from the entry field
    entry.delete(0, tk.END)  # Clear the entry field
    entry.insert(tk.END, current + str(value))  # Append the clicked value

def button_clear():
    """Clear the entry field."""
    entry.delete(0, tk.END)  # Clear the entry field

def button_equal():
    """Evaluate the expression in the entry field and display the result."""
    try:
        result = eval(entry.get())  # Evaluate the mathematical expression
        entry.delete(0, tk.END)  # Clear the entry field
        entry.insert(tk.END, result)  # Insert the result into the entry field
    except Exception as e:
        entry.delete(0, tk.END)  # Clear the entry field if there's an error
        entry.insert(tk.END, "Error")  # Display an error message

# Create the main application window
root = tk.Tk()
root.title("Red and Black Calculator")  # Set the window title

# Set window background color
root.configure(bg="red")  # Change the background color of the main window

# Create an entry widget for displaying the expression/result
entry = tk.Entry(root, width=16, font=('Helvetica', 24), borderwidth=2, relief="solid", bg="black", fg="red")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # Place the entry in the grid

# Create a list of buttons for the calculator
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', 'C', '=', '+'
]

# Define colors for buttons
button_bg_color = "black"  # Background color for number buttons
button_fg_color = "red"       # Text color for number buttons
operator_bg_color = "black"    # Background color for operator buttons
operator_fg_color = "red"      # Text color for operator buttons

# Add buttons to the grid layout
row_value = 1  # Start from the second row
col_value = 0  # Start from the first column

for button in buttons:
    if button == "=":
        # Create the equals button with specific command and colors
        tk.Button(root, text=button, width=5, height=2, font=('Helvetica', 18), 
                  command=button_equal, bg=operator_bg_color, fg=operator_fg_color).grid(row=row_value, column=col_value, padx=5, pady=5)
    elif button == "C":
        # Create the clear button with specific command and colors
        tk.Button(root, text=button, width=5, height=2, font=('Helvetica', 18), 
                  command=button_clear, bg="black", fg="red").grid(row=row_value, column=col_value, padx=5, pady=5)
    elif button in ['/', '*', '-', '+']:
        # Create operator buttons with specific command and colors
        tk.Button(root, text=button, width=5, height=2, font=('Helvetica', 18), 
                  command=lambda b=button: button_click(b), bg=operator_bg_color, fg=operator_fg_color).grid(row=row_value, column=col_value, padx=5, pady=5)
    else:
        # Create number buttons with specific command and colors
        tk.Button(root, text=button, width=5, height=2, font=('Helvetica', 18), 
                  command=lambda b=button: button_click(b), bg=button_bg_color, fg=button_fg_color).grid(row=row_value, column=col_value, padx=5, pady=5)
    
    col_value += 1  # Move to the next column
    if col_value > 3:  # If we've filled 4 columns, move to the next row
        col_value = 0
        row_value += 1

# Start the Tkinter event loop to run the application
root.mainloop()