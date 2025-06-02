
import tkinter as tk

def button1(parent, text, command=None):
	normal_bg = "#444444"
	hover_bg = "#555555"
	pressed_bg = "#666666"
	
	btn = tk.Button(
		parent,
		text=text,
		bg=normal_bg,
		fg="white",
		relief="flat",
		borderwidth=0,
		highlightthickness=1,
		highlightbackground="#555555",
		highlightcolor="#8888ff",
		activeforeground="white",
		activebackground=pressed_bg
	)

	# Add hover & click effects
	btn.bind("<Enter>", lambda e: btn.config(bg=hover_bg))
	btn.bind("<Leave>", lambda e: btn.config(bg=normal_bg))
	btn.bind("<Button-1>", lambda e: btn.config(bg=pressed_bg))
	btn.bind("<ButtonRelease-1>", lambda e: btn.config(bg=normal_bg))
	
	# Set command after bindings
	if command:
		btn.config(command=command)

	return btn

def on_resize(event):
    total_width = root.winfo_width()
    sidebar_width = total_width // 10
    canvas_width = total_width - sidebar_width

    sidebar.config(width=sidebar_width)
    canvas.config(width=canvas_width)

def exit_on_esc(event):
    root.destroy()

# Create main window
root = tk.Tk()
root.title("Map Generator")
root.geometry("800x600")
root.configure(bg="#222222")  # Dark background

# Grid configuration
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=1)

# Sidebar frame
sidebar = tk.Frame(root, bg="#333333")
sidebar.grid(row=0, column=0, sticky="ns")

# Sidebar content
tk.Label(sidebar, text="Sidebar", bg="#333333", fg="white").pack(pady=10)
button1(sidebar, "Button 1").pack(pady=5, fill='x', padx=5)
button1(sidebar, "Button 2").pack(pady=5, fill='x', padx=5)

# Canvas area
canvas = tk.Canvas(root, bg="#111111", highlightthickness=0)
canvas.grid(row=0, column=1, sticky="nsew")

# Example canvas drawing
canvas.create_oval(100, 100, 200, 200, fill="#0066ff")

# Bindings
root.bind("<Configure>", on_resize)
root.bind("<Escape>", exit_on_esc)

def run():
    root.mainloop()
