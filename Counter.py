import tkinter as tk
import time
from threading import Thread

# Initialize starting number
number = 168000

# Function to update the number every 30 minutes (1800 seconds)
def update_number():
    global number
    while True:
        number += 10
        number_label.config(text=str(number))
        time.sleep(15)  # Wait for 15 seconds (15 seconds)

# Function to start the counter
def start_counter():
    Thread(target=update_number).start()

# Create the main window
root = tk.Tk()
root.title("Number Counter")

# Display the number
number_label = tk.Label(root, text=str(number), font=("Helvetica", 48))
number_label.pack(pady=20)

# Start button
start_button = tk.Button(root, text="Start Counter", command=start_counter, font=("Helvetica", 24))
start_button.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()
