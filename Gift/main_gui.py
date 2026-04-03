import tkinter as tk
from tkinter import ttk
from csv_loader import load_csv
from bfs import bfs

# Load graph
graph = load_csv("data.csv")

# Create window
root = tk.Tk()
root.title("Connection Finder")
root.geometry("500x420")
root.configure(bg="#0f172a")  # deep dark blue

# STYLE
style = ttk.Style()
style.theme_use("default")

style.configure("TButton",
                font=("Segoe UI", 11, "bold"),
                padding=10)

style.configure("TEntry",
                padding=8)

# MAIN FRAME (card style)
frame = tk.Frame(root, bg="#111827", bd=0)
frame.place(relx=0.5, rely=0.5, anchor="center", width=420, height=360)

# TITLE
title = tk.Label(frame,
                 text="🔎 Connection Finder",
                 font=("Segoe UI", 18, "bold"),
                 bg="#111827",
                 fg="white")
title.pack(pady=(20, 5))

subtitle = tk.Label(frame,
                    text="Find connections between people using BFS",
                    font=("Segoe UI", 9),
                    bg="#111827",
                    fg="#9ca3af")
subtitle.pack(pady=(0, 20))

# INPUT 1
label1 = tk.Label(frame, text="First Person",
                  bg="#111827", fg="#e5e7eb",
                  font=("Segoe UI", 10))
label1.pack(anchor="w", padx=40)

entry1 = tk.Entry(frame,
                  font=("Segoe UI", 11),
                  bg="#1f2937", fg="white",
                  insertbackground="white",
                  relief="flat")
entry1.pack(pady=8, ipadx=10, ipady=6)

# INPUT 2
label2 = tk.Label(frame, text="Second Person",
                  bg="#111827", fg="#e5e7eb",
                  font=("Segoe UI", 10))
label2.pack(anchor="w", padx=40)

entry2 = tk.Entry(frame,
                  font=("Segoe UI", 11),
                  bg="#1f2937", fg="white",
                  insertbackground="white",
                  relief="flat")
entry2.pack(pady=8, ipadx=10, ipady=6)

# RESULT BOX
output = tk.Label(frame,
                  text="",
                  wraplength=320,
                  bg="#111827",
                  fg="#22c55e",
                  font=("Segoe UI", 11, "bold"))
output.pack(pady=20)

# SEARCH FUNCTION
def search():
    start = entry1.get().strip()
    target = entry2.get().strip()

    if not start or not target:
        output.config(text="⚠️ Please fill both fields", fg="#facc15")
        return

    if start not in graph:
        output.config(text="❌ First person not found", fg="#ef4444")
        return

    result = bfs(graph, start, target)

    if result:
        output.config(text=" → ".join(result), fg="#22c55e")
    else:
        output.config(text="No connection found", fg="#ef4444")

# BUTTON
search_btn = tk.Button(frame,
                       text="SEARCH",
                       command=search,
                       bg="#ec4899",
                       fg="white",
                       font=("Segoe UI", 12, "bold"),
                       activebackground="#db2777",
                       relief="flat",
                       padx=10,
                       pady=8)
search_btn.pack(pady=10)

# FOOTER
footer = tk.Label(frame,
                  text="Powered by BFS Algorithm",
                  bg="#111827",
                  fg="#6b7280",
                  font=("Segoe UI", 8))
footer.pack(side="bottom", pady=10)

root.mainloop()