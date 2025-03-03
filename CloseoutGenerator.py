import tkinter as tk
from tkinter import font
from customtkinter import CTk as ctk
import json
import openai

# OpenAI API key setup - UG2/FMI key
openai.api_key = 'sk-***'

# Function for generating closeouts


def generate_closeouts(work_order_description):
    # The priming prompt
    prompt = ("Work Order: Install new backup generator in Server Room\n"
              "A new backup generator was installed in the Server Room as planned. All connections to critical infrastructure were made and verified. The generator was tested under simulated power loss conditions and functioned as expected, ensuring continuous power supply to the servers. Post-installation, the area was cleaned and all installation-related debris was removed.\n"
              "Work Order: "
              "Work Order: HVAC system maintenance in Production Room 2\n"
              "HVAC system in Production Room 2 underwent comprehensive maintenance. Filters were replaced, and system components were cleaned and lubricated as necessary. System performance was validated post-maintenance, showing improvement in efficiency. Proper documentation of the maintenance process has been recorded as per company guidelines.\n"
              "Work Order: "
              "Work Order: Replace faulty water pump in Lab 6\n"
              "The faulty water pump in Lab 6 was successfully replaced. New pump was installed, tested under various conditions, and confirmed operational. Post-installation area was cleaned and returned to its original state.\n"
              "Work Order: "
              "Work Order: Rearrange tables in the Lab\n"
              "The lab configuration has been successfully altered as per instructions. Tables were strategically repositioned to optimize space utilization and create a more open central area. Following the rearrangement, all tables were checked and confirmed to be stable, ensuring safety in the workspace. The area was left in a tidy and orderly state.\n"
              "Work Order: "
              "Work Order: Escort vendor to the Lab\n"
              "The vendor was successfully escorted to the designated lab. Prior to starting work, the vendor was briefed on necessary safety protocols and confirmed to be equipped with appropriate safety gear. Ensuring vendor compliance with our safety rules will help maintain a secure work environment. The escort task was completed without issue.\n"
              "Work Order: ")

    closeout_variations = []
    for _ in range(1):
        response = openai.Completion.create(
            engine="text-davinci-002",
            # Add the work order to the priming prompt
            prompt=prompt + work_order_description,
            temperature=0.5,
            max_tokens=200
        )
        closeout_variations.append(response.choices[0].text.strip())
    return closeout_variations

# Function for getting input and displaying closeouts


def generate_and_display_closeouts():
    work_order = work_order_entry.get("1.0", 'end-1c')
    closeouts = generate_closeouts(work_order)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "\n\n".join(closeouts))


def clear_entries():
    work_order_entry.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)


def on_window_resize(event):
    # Update the widget sizes when the window is resized
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(3, weight=1)


# GUI setup
root = ctk()
root.configure(bg=root["bg"])  # set background color
root.title("Closeout Generator")

# Define the font properties
text_font = font.Font(size=12)

# Input text field
tk.Label(root, text="Input Work Order Description or Your Notes:",
         bg=root["bg"], fg='white').grid(row=0, column=0, sticky='w')
work_order_entry = tk.Text(root, height=5, font=text_font, wrap=tk.WORD,
                           bg=root["bg"], fg='white', insertbackground='white')
work_order_entry.grid(row=1, column=0, sticky='nsew', padx=10)

# Output text field
tk.Label(root, text="Generated Notes:", bg=root["bg"], fg='white').grid(
    row=2, column=0, sticky='w')
output_text = tk.Text(root, height=10, font=text_font, wrap=tk.WORD,
                      bg=root["bg"], fg='white', insertbackground='white')
output_text.grid(row=3, column=0, sticky='nsew', padx=10)

# Button frame
button_frame = tk.Frame(root, bg=root["bg"])
button_frame.grid(row=4, column=0, sticky='nsew', padx=10, pady=(10, 5))

# Button for generating closeouts
generate_button = tk.Button(button_frame, text="Generate",
                            command=generate_and_display_closeouts, bg='black', fg='white', width=10)
generate_button.pack(padx=5, pady=5)

# Button for clearing the entries
clear_button = tk.Button(button_frame, text="Clear",
                         command=clear_entries, bg='black', fg='white', width=10)
clear_button.pack(padx=5, pady=5)

# Configure resizing behavior
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(3, weight=1)
root.bind('<Configure>', on_window_resize)

root.mainloop()
