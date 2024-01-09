import tkinter as tk
import query_manipulator

window = tk.Tk()
window.title("SQL Query")

query_label = tk.Label(window, text="Type your SQL DQL Query")
query_label.pack()

query_entry = tk.Text(window, height=4, width=100)
query_entry.pack()


def submit_query():
    query = query_entry.get("1.0", "end-1c")

    response = query_manipulator.validate_query(query)

    validation_box.delete("1.0", tk.END)
    validation_box.insert(tk.END, response)

    if response == "Valid Query!":
        algebra = query_manipulator.relational_algebra(query)
        algebra_box.delete("1.0", tk.END)
        algebra_box.insert(tk.END, algebra)
        query_manipulator.build_and_show_tree(query)


def clear_input():
    query_entry.delete("1.0", tk.END)


submit_button = tk.Button(window, text="Submit", command=submit_query)
submit_button.pack()

empty_button = tk.Button(window, text="Clear", command=clear_input)
empty_button.pack()

validation_label = tk.Label(window, text="Validation Message")
validation_label.pack()

validation_box = tk.Text(window, height=4, width=100)
validation_box.pack()

algebra_label = tk.Label(window, text="Relational Algebra")
algebra_label.pack()

algebra_box = tk.Text(window, height=4, width=100)
algebra_box.pack()

window.mainloop()
