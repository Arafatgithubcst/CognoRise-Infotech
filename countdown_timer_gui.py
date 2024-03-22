import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")
        self.master.geometry("300x200")
        
        self.label = tk.Label(self.master, text="Enter time (in seconds):")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=5)
        
        self.start_button = tk.Button(self.master, text="Start Timer", command=self.start_timer)
        self.start_button.pack(pady=10)
        
    def start_timer(self):
        try:
            time_seconds = int(self.entry.get())
            if time_seconds <= 0:
                raise ValueError("Invalid input")
            self.countdown(time_seconds)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer for time (in seconds)")

    def countdown(self, seconds):
        while seconds >= 0:
            self.label.config(text=f"Time left: {seconds} seconds")
            self.master.update()
            time.sleep(1)
            seconds -= 1
        messagebox.showinfo("Time's up!", "Countdown timer finished!")

def main():
    root = tk.Tk()
    app = CountdownTimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
