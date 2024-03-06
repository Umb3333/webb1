import tkinter as tk
import random
import threading
import os
import subprocess



# Global variable to control the thread
stop_thread = False

def create_fake_error():
    global stop_thread
    while not stop_thread:
        # Create a Tkinter window for each error message
        root = tk.Tk()
        root.title("Error")

        # Generate a random error message
        error_messages = [
            "Fatal Error: System Halted!",
            "Error 404: File Not Found",
            "Critical Error: Hard Drive Failure",
            "Access Violation: You Have Been Hacked",
            "Blue Screen of Death: Windows Encountered an Error"
        ]
        error_message = random.choice(error_messages)

        # Display the fake error message
        label = tk.Label(root, text=error_message, fg="red", font=("Comic Sans", 20))
        label.pack(padx=50, pady=20)

        # Function to close the window
        def close_window():
            root.destroy()

        # Set window size and position
        window_width = random.randrange(200,600)
        window_height = random.randrange(100,400)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = random.randint(0, screen_width - window_width)
        y = random.randint(0, screen_height - window_height)
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Run the Tkinter event loop
        root.mainloop()


       




if __name__ == "__main__":
    
    error_threads = []
    for _ in range(random.randrange(10000,10001)):  # Create 5 error message windows simultaneously
        error_thread = threading.Thread(target=create_fake_error)
        
        error_thread.start()
        error_threads.append(error_thread)

   
    input("Press Enter to stop the fake errors...\n")



    stop_thread = True

    
    for error_thread in error_threads:
        error_thread.join()

