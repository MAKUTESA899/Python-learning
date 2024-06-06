import tkinter as tk
from datetime import datetime

def update_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

# Create the main window
root = tk.Tk()
root.title("Date and Time Display")

# Create a label to display the time
time_label = tk.Label(root, font=("Helvetica", 24))
time_label.pack(pady=20)

# Start updating the time
update_time()

# Run the application
root.mainloop()