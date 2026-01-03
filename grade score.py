import tkinter as tk  # Import the GUI library

# This function runs when you click the button
def calculate_grade():
    try:
        score = int(entry.get())  # Get input and convert it to integer

        # 🔽 This is your grading logic:
        if score >= 90:
            result.set("Grade: A")
        elif score >= 80:
            result.set("Grade: B")
        else:
            result.set("Grade: C or below")
    
    except ValueError:
        # If the input is not a number, show this
        result.set("Please enter a valid number")

# GUI setup
window = tk.Tk()
window.title("Grade Calculator")

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Check Grade", command=calculate_grade)
button.pack()

result = tk.StringVar()
label = tk.Label(window, textvariable=result)
label.pack()

window.mainloop()
