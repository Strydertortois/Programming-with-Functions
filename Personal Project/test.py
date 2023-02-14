import tkinter as tk
import tkinter.font as font

root = tk.Tk()
root.title("Calorie Tracker")
root.geometry("400x400")
root.config(bg="#F7F7F7")

myFont = font.Font(family='Helvetica', size=12)

label_input = tk.Label(root, text="Enter the number of calories:", bg="#F7F7F7", font=myFont)
label_input.pack(pady=10)

entry_input = tk.Entry(root, width=20, font=myFont)
entry_input.pack(pady=10)

calories = []

def add_calorie():
    calorie = entry_input.get()
    if calorie.isdigit():
        calories.append(int(calorie))
        label_calories.config(text="Calories: " + str(sum(calories)))
        entry_input.delete(0, 'end')
    else:
        label_error.config(text="Please enter a valid number.", fg="red")

button_add = tk.Button(root, text="Add Calories", bg="#B3E5FC", font=myFont, command=add_calorie)
button_add.pack(pady=10)

label_calories = tk.Label(root, text="Calories: 0", bg="#F7F7F7", font=myFont)
label_calories.pack(pady=10)

label_error = tk.Label(root, text="", bg="#F7F7F7", font=myFont)
label_error.pack(pady=10)

root.mainloop()
