import tkinter as tk
root = tk.Tk()


root.title("Resizable GUI with Labels")


# Create labels with text
label1 = tk.Label(root, text="A", bg="red")
label2 = tk.Label(root, text="B", bg="white")
label3 = tk.Label(root, text="C", bg="white")
label4 = tk.Label(root, text="D", bg="white")

# Pack labels with specified geometry
label1.pack(fill=tk.X, expand=True)
label2.pack()
label3.pack()
label4.pack()

root.mainloop()

