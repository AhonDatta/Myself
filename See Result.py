import tkinter as tk
from tkinter import ttk
from myself import *

# Function to get the value of myself.p and display it
def display_value():
    value = myself.p
    label.config(text=f"Value of myself.p: {value}", foreground="blue")

# Create the main window
root = tk.Tk()
root.title("Myself Display")
root.configure(bg="lightblue")

# Create and pack the label with custom colors
label = ttk.Label(root, text="Value of myself.p:", font=("Helvetica", 14), foreground="white", background="lightblue")
label.pack(padx=20, pady=20)

# Create and pack the button with custom colors
button = ttk.Button(root, text="Show Value", command=display_value, style="TButton")
button.pack(padx=20, pady=20)

# Style configuration for the button
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), foreground="white", background="blue", padding=10)

# Run the Tkinter event loop
root.mainloop()
import tkinter as tk
from tkinter import ttk
from myself import *

# Function to get the value of myself.p and display it
def display_value():
    value = myself.p
    label.config(text=f"Value of myself: {value}", foreground="blue")

# Create the main window
root = tk.Tk()
root.title("Myself Display")
root.configure(bg="lightblue")

# Create and pack the label with custom colors
label = ttk.Label(root, text="Press the button:", font=("Helvetica", 14), foreground="white", background="lightblue")
label.pack(padx=20, pady=20)

# Create and pack the button with custom colors
button = ttk.Button(root, text="CLICK HERE", command=display_value, style="TButton")
button.pack(padx=20, pady=20)

# Style configuration for the button
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), foreground="white", background="blue", padding=10)

# Run the Tkinter event loop
root.mainloop()
import tkinter as tk
from tkinter import ttk
from myself import *

# Function to get the value of myself.p and display it
def display_value():
    value = myself.p
    label.config(text=f"Value of myself: {value}", foreground="blue")

# Create the main window
root = tk.Tk()
root.title("Myself Display")
root.configure(bg="lightblue")

# Create and pack the label with custom colors
label = ttk.Label(root, text="Value of myself.p:", font=("Helvetica", 14), foreground="white", background="lightblue")
label.pack(padx=20, pady=20)

# Create and pack the button with custom colors
button = ttk.Button(root, text="Show Value", command=display_value, style="TButton")
button.pack(padx=20, pady=20)

# Style configuration for the button
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), foreground="white", background="blue", padding=10)

# Run the Tkinter event loop
root.mainloop()
