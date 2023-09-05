import tkinter as tk  # For creating a simple GUI
import threading

def long_running_function():
    # Simulate a time-consuming operation
    import time
    time.sleep(5)
    print("hiii")

def run_function_in_background():
    # Create a thread to run the long_running_function
    thread = threading.Thread(target=long_running_function)
    thread.start()

def main():
    root = tk.Tk()
    root.title("Responsive GUI")

    label = tk.Label(root, text="Click the button to run a function")
    label.pack()

    button = tk.Button(root, text="Run Function", command=run_function_in_background)
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
