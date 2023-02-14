import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

window = ctk.CTk()

frame = ctk.CTkFrame(master=window)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="CALORIE TRACKER")
label.pack(pady=12, padx=1)

entry1 = ctk.CTkEntry(master=frame, placeholder_text="Enter Calories (ex: 300)", width=200)
entry1.pack(pady=2, padx=10)

entry2 = ctk.CTkEntry(master=frame, placeholder_text="Enter Description (ex: pizza)", width=200)
entry2.pack(pady=2, padx=10)

def getEntry1():
    calories = entry1.get()
    return calories
def getEntry2():
    description = entry2.get()
    return description
def insertData(calories, description):
    textbox.insert(ctk.INSERT, f"{description} ({calories} calories) \n")

textbox = ctk.CTkTextbox(master=frame, width=300, height=100)
textbox.pack(pady=20, padx=10)

calories = getEntry1()
description = getEntry2()

caloriesList = []
def addCalories():
    total = sum(caloriesList)
    return total

def displayInfo():
    #call input functions
    calories_input = getEntry1()
    description_input = getEntry2()
    #add input to list of calories

    if calories_input.isdigit():
        caloriesList.append(int(calories_input))
    #insert into main textbox
        insertData(calories_input, description_input)
        entry1.delete(ctk.ANCHOR, ctk.END)
        entry2.delete(ctk.ANCHOR, ctk.END)
        label_error.configure(text="")
        #call addCalories and configure text box to display total
        total = addCalories()
        textbox2.configure(text=f"Total Calories: {total}")

    else:
        label_error.configure(text="Please enter correct data")


button = ctk.CTkButton(master=frame, text="Enter", command=displayInfo)
button.pack(padx=0, pady=10)

textbox2 = ctk.CTkLabel(master=frame, width=150, height=25, text="")
textbox2.pack(pady=5, padx=10)

label_error = ctk.CTkLabel(master=frame, text="")
label_error.pack(pady=0, padx=0)


window.resizable(width=False, height=False)
window.mainloop()