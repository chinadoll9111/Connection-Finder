# 📘 BFS-Based Social Network Search Engine

## 👥 Group Members

* Elijah
* Davis
* Gift

---

## 📌 Project Overview

This project is a **Graphical Search Engine Application** built using **Python** that demonstrates the use of the **Breadth-First Search (BFS)** algorithm on data stored in a **CSV file**.

The system simulates a **social network**, where:

* Each person represents a **node**
* Each connection represents an **edge**

Using BFS, the program finds the **shortest connection path** between two individuals.

---

## 🎯 Objectives

* To understand how **CSV files** can be used as data storage
* To implement **Breadth-First Search (BFS)** in a real-world scenario
* To convert tabular data into a **graph structure**
* To build a **modern GUI application** using Tkinter
* To simulate a real-life **connection finder system**

---

## 🧠 How the System Works

### 1. CSV Data (Data Source)

We created a CSV file (`data.csv`) containing two columns:

* `Person`
* `Connected_To`

Each row represents a relationship between two individuals.

Example:

```
Tunde → Emeka
Emeka → David
```

This data is interpreted as a **graph**.

---

### 2. Graph Conversion

The CSV file is read and converted into a **dictionary (adjacency list)**:

Example:

```
{
  "Tunde": ["Chioma", "Emeka"],
  "Emeka": ["David"]
}
```

---

### 3. BFS Algorithm

The BFS algorithm:

* Starts from a given node
* Explores all neighbors level by level
* Uses a **queue** to track traversal
* Returns the **shortest path** when the target is found

---

### 4. GUI Interface

We implemented a **modern graphical interface** using Tkinter where users can:

* Enter two names
* Click a **Search button**
* View the connection path visually

---

## 🛠️ Technologies Used

* Python
* Tkinter (GUI)
* CSV (Data storage)
* BFS Algorithm

---

## 📁 Project Structure

```
bfs-search-engine/
│
├── data.csv
├── csv_loader.py
├── bfs.py
├── main_gui.py
└── README.md
```

---

## 👨‍💻 Work Distribution

### 🔹 Elijah – Data & Graph Handling

* Created the CSV dataset (`data.csv`)
* Designed the structure of the data
* Implemented `csv_loader.py`
* Converted CSV data into a graph

---

### 🔹 Davis – Algorithm Implementation

* Implemented the BFS algorithm (`bfs.py`)
* Ensured correct traversal using queue and visited set
* Modified BFS to return the **full path**, not just True/False

---

### 🔹 Gift – GUI & Integration

* Designed the graphical interface (`main_gui.py`)
* Connected CSV loader and BFS algorithm
* Handled user input and displayed results
* Improved user experience with styling and feedback

---

## ▶️ How to Run the Project

1. Ensure Python is installed
2. Place all files in the same folder
3. Run the application:

```
python main_gui.py
```

4. Enter two names and click **SEARCH**

---

## 💡 Features

* Modern GUI design
* Path-based BFS output
* Error handling (empty input, invalid names)
* Real-life simulation (social network)

---

## 🔄 Version Control (GitHub Collaboration)

To ensure proper collaboration, we used **GitHub** for version control.

### 📌 Workflow Used

Each group member:

1. Created a **separate folder**:

   * `Elijah/`
   * `Davis/`
   * `Gift/`

2. Worked only inside their folder initially:

   * Elijah → CSV + loader
   * Davis → BFS logic
   * Gift → GUI

---

### 🔁 Merging Process

After completing individual tasks:

1. One member created the main repository
2. Others **cloned the repository**
3. Each member **pushed their folder** to GitHub
4. Changes were **merged into the main branch**

---

### 🔀 Final Result

After merging:

* Every member now has the **complete project**
* Each folder now contains **all files from the project**
* The system is fully integrated and runnable

---

### 🧠 Important Concept

Initially:

* Each person had **only their own files**

After GitHub merge:

* Everyone has **all files (full project)**

This demonstrates proper use of:

* Collaboration
* Version control
* Code integration

---

## 🎤 Conclusion

This project demonstrates how theoretical concepts like **BFS** can be applied to real-world scenarios. By combining data structures, algorithms, and user interface design, we successfully built a functional and interactive search engine.

---

## 🚀 Future Improvements

* Add animations
* Convert to a web-based application
* Visualize graph connections
* Implement auto-suggestions

---

## ✅ Summary

This project showcases:

* Strong understanding of BFS
* Practical use of CSV data
* Team collaboration using GitHub
* Development of a modern GUI application

---
