import tkinter as tk

def key_pressed(event):
    label.config(text="Key Pressed: " + event.keysym)

# Create window
window = tk.Tk()
window.title("Keyboard Event Monitoring")
window.geometry("400x200")

title = tk.Label(
    window,
    text="Keyboard Event Monitoring",
    font=("Arial", 16)
)
title.pack(pady=30)

label = tk.Label(
    window,
    text="Press any key...",
    font=("Arial", 14)
)
label.pack()

# Monitor keyboard events in this window
window.bind("<Key>", key_pressed)

window.mainloop()
