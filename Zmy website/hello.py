import tkinter as tk

def play_action():
    
    print("hello u l monkey")


root = tk.Tk()
root.title("Play Button Example")


play_button = tk.Button(root, text="Play", command=play_action)
play_button.pack()


root.mainloop()
