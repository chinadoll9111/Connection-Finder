import sys
import os
import time
import threading

# Fix import paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import tkinter as tk
from tkinter import ttk

from DAVIIS.bfs import bfs_find_path
from ELIJAH.csv_loader import load_csv


# Load graph
graph = load_csv("ELIJAH/data.csv")


# ===================== WINDOW =====================
root = tk.Tk()
root.title("Connection Finder")
root.geometry("500x450")
root.configure(bg="#0f172a")


# ===================== STYLE =====================
style = ttk.Style()
style.theme_use("default")

style.configure("TButton", font=("Segoe UI", 11, "bold"), padding=10)
style.configure("TEntry", padding=8)


# ===================== MAIN FRAME =====================
frame = tk.Frame(root, bg="#111827")
frame.place(relx=0.5, rely=0.5, anchor="center", width=480, height=420)


# ===================== TITLE =====================
title = tk.Label(
    frame,
    text="🔎 Connection Finder",
    font=("Segoe UI", 18, "bold"),
    bg="#111827",
    fg="white"
)
title.pack(pady=(20, 5))

subtitle = tk.Label(
    frame,
    text="Find connections between people using BFS",
    font=("Segoe UI", 9),
    bg="#111827",
    fg="#9ca3af"
)
subtitle.pack(pady=(0, 20))


# ===================== INPUTS =====================
label1 = tk.Label(frame, text="First Person", bg="#111827", fg="#e5e7eb", font=("Segoe UI", 10))
label1.pack(anchor="w", padx=40)

entry1 = tk.Entry(frame, font=("Segoe UI", 11), bg="#1f2937", fg="white", insertbackground="white", relief="flat")
entry1.pack(pady=8, ipadx=10, ipady=6)

label2 = tk.Label(frame, text="Second Person", bg="#111827", fg="#e5e7eb", font=("Segoe UI", 10))
label2.pack(anchor="w", padx=40)

entry2 = tk.Entry(frame, font=("Segoe UI", 11), bg="#1f2937", fg="white", insertbackground="white", relief="flat")
entry2.pack(pady=8, ipadx=10, ipady=6)


# ===================== SEARCH FUNCTION =====================
# 1️⃣ update_ui FIRST
def update_ui(result, time_taken):
    output.delete("1.0", tk.END)

    if result:
        output.insert(
            tk.END,
            f"{' → '.join(result)}\n\n⏱ Time: {time_taken:.6f} seconds"
        )
    else:
        output.insert(
            tk.END,
            f"No connection found\n\n⏱ Time: {time_taken:.6f} seconds"
        )

    output.see(tk.END)


# 2️⃣ run_search SECOND
def run_search(start, target):
    start_time = time.time()
    result = bfs_find_path(graph, start, target)
    end_time = time.time()
    time_taken = end_time - start_time

    root.after(0, update_ui, result, time_taken)


# 3️⃣ search LAST
def search():
    start = entry1.get().strip()
    target = entry2.get().strip()

    output.delete("1.0", tk.END)

    if not start or not target:
        output.insert(tk.END, "⚠️ Please fill both fields")
        return

    if start not in graph:
        output.insert(tk.END, "❌ First person not found")
        return

    output.insert(tk.END, "🔍 Searching... please wait")

    import threading
    threading.Thread(target=run_search, args=(start, target), daemon=True).start()
# ===================== BUTTON =====================
search_btn = tk.Button(
    frame,
    text="SEARCH",
    command=search,
    bg="#ec4899",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    activebackground="#db2777",
    relief="flat",
    padx=10,
    pady=8
)
search_btn.pack(pady=15)


# ===================== RESULT BOX =====================
result_frame = tk.Frame(frame, bg="#111827")
result_frame.pack(pady=10)

scrollbar = tk.Scrollbar(result_frame)
scrollbar.pack(side="right", fill="y")

output = tk.Text(
    result_frame,
    height=6,
    wrap="word",
    bg="#111827",
    fg="#22c55e",
    font=("Segoe UI", 11, "bold"),
    yscrollcommand=scrollbar.set,
    relief="flat"
)

output.pack(side="left", fill="both", expand=True)
scrollbar.config(command=output.yview)


# ===================== FOOTER =====================
footer = tk.Label(
    frame,
    text="Powered by BFS Algorithm",
    bg="#111827",
    fg="#6b7280",
    font=("Segoe UI", 8)
)
footer.pack(side="bottom", pady=10)


# ===================== RUN =====================
root.mainloop()