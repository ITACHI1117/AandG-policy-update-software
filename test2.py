import tkinter as tk
import sys
import platform


class Popup:
    def __init__(self):
        self.tl = None
        self.root = tk.Tk()
        self.root.title("Grab Set/Release")

        tk.Label(self.root, text=f"Python v{platform.python_version()}").pack(padx=12, pady=12)
        tk.Button(self.root, text="Popup!", width=20, command=self.popup).pack(padx=12, pady=12)
        tk.Button(self.root, text="Exit", width=20, command=sys.exit).pack(padx=12, pady=12)

        self.root.mainloop()

    def popup(self):
        if self.tl is None:
            self.tl = tk.Toplevel()
            tk.Button(self.tl, text="Grab set", width=20, command=self.lock).pack(padx=12, pady=12)
            tk.Button(self.tl, text="Grab release", width=20, command=self.unlock).pack(padx=12, pady=12)

    def lock(self):
        self.tl.grab_set()
        print("Grab set!")

    def unlock(self):
        self.tl.grab_release()
        print("Grab released!")


Popup()