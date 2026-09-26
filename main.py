import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
from backend import select_image, save_encoded_image, extract_message, get_selected_image_path

app = ctk.CTk()
app.title("StegoHide")
app.geometry("800x400")
app.resizable(False, False)

#try:
 #   app.iconbitmap('encryption.ico')
#except Exception as e:
 #   print(e)

title_label = ctk.CTkLabel(app, text="Stego", font=("Consolas", 80, "bold"))
title_label.place(x=90, y=130)
titleR_label = ctk.CTkLabel(app, text="Hide", font=("Consolas", 30, "bold"), text_color="red")
titleR_label.place(x=250, y=222)

tabview = None
current_mode = "dark"

def back_to_main():
    global tabview
    if tabview is not None:
        tabview.destroy()
        tabview = None
    title_label.place(x=90, y=130)
    titleR_label.place(x=250, y=222)
    en_button.place(x=500, y=140)
    dc_button.place(x=500, y=200)

def create_encode_tab(tab):
    img_frame = ctk.CTkFrame(tab, width=200, height=200, corner_radius=15)
    img_frame.place(x=30, y=20)
    image_label = ctk.CTkLabel(img_frame, text="Selected Image", compound="center",
                               font=("Consolas", 16), fg_color="transparent", corner_radius=15)
    image_label.pack(fill="both", expand=True, padx=5, pady=5)

    input_frame = ctk.CTkFrame(tab, width=400, height=300, fg_color="transparent")
    input_frame.place(x=350, y=20)

    file_button = ctk.CTkButton(input_frame, text="Select Image", command=lambda: select_image(image_label, ctk),
                                border_color='red', border_width=2, fg_color="transparent",
                                text_color=("black", "white"), hover_color="#444444")
    file_button.pack(pady=5)

    secret_text = ctk.CTkTextbox(input_frame, width=300, height=100, font=("Consolas", 14),
                                 border_width=2, border_color='red')
    secret_text.pack(pady=5)

    save_button = ctk.CTkButton(input_frame, text="Save Encoded Image",
                                command=lambda: save_encoded_image(secret_text.get("1.0", "end-1c"),
                                                                   get_selected_image_path(), messagebox, filedialog),
                                fg_color="transparent", border_color='red', border_width=2,
                                text_color=("black", "white"), hover_color="#444444")
    save_button.pack(pady=15)

    back_button = ctk.CTkButton(tab, text="Back", command=back_to_main,
                                fg_color="transparent", border_color='red', border_width=2,
                                text_color=("black", "white"), hover_color="#444444",
                                height=30, width=90, font=("Consolas", 14, "bold"), corner_radius=8)
    back_button.place(x=20, y=310)

def create_decode_tab(tab):
    img_frame = ctk.CTkFrame(tab, width=200, height=200, corner_radius=15)
    img_frame.place(x=30, y=20)
    image_label = ctk.CTkLabel(img_frame, text="Selected Image", compound="center",
                               font=("Consolas", 16), fg_color="transparent", corner_radius=15)
    image_label.pack(fill="both", expand=True, padx=5, pady=5)

    output_frame = ctk.CTkFrame(tab, width=400, height=300, fg_color="transparent")
    output_frame.place(x=350, y=20)

    file_button = ctk.CTkButton(output_frame, text="Select Image", command=lambda: select_image(image_label, ctk),
                                border_color='red', border_width=2, fg_color="transparent",
                                text_color=("black", "white"), hover_color="#444444")
    file_button.pack(pady=5)

    extracted_text = ctk.CTkTextbox(output_frame, width=300, height=100, font=("Consolas", 14),
                                    border_width=2, border_color='red', state="disabled")
    extracted_text.pack(pady=5)

    extract_button = ctk.CTkButton(output_frame, text="Extract Message",
                                   command=lambda: extract_message(extracted_text, get_selected_image_path(), messagebox),
                                   fg_color="transparent", border_color='red', border_width=2,
                                   text_color=("black", "white"), hover_color="#444444")
    extract_button.pack(pady=15)

    back_button = ctk.CTkButton(tab, text="Back", command=back_to_main,
                                fg_color="transparent", border_color='red', border_width=2,
                                text_color=("black", "white"), hover_color="#444444",
                                height=30, width=90, font=("Consolas", 14, "bold"), corner_radius=8)
    back_button.place(x=20, y=310)

def show_tab(tab_name):
    global tabview
    if tabview is not None:
        tabview.destroy()

    tabview = ctk.CTkTabview(app, width=800, height=400, border_color='red', border_width=2)
    encode_tab = tabview.add("Encode")
    decode_tab = tabview.add("Decode")

    create_encode_tab(encode_tab)
    create_decode_tab(decode_tab)

    tabview.set(tab_name)
    tabview.place(x=0, y=0)

    title_label.place_forget()
    titleR_label.place_forget()
    en_button.place_forget()
    dc_button.place_forget()

    update_theme_colors()

def update_theme_colors():
    color = "white" if current_mode == "dark" else "black"
    for child in app.winfo_children():
        if isinstance(child, (ctk.CTkButton, ctk.CTkEntry, ctk.CTkTextbox)):
            child.configure(text_color=color)

def toggle_mode():
    global current_mode
    current_mode = "dark" if current_mode == "light" else "light"
    ctk.set_appearance_mode(current_mode)
    update_theme_colors()

en_button = ctk.CTkButton(app, text="Encode", command=lambda: show_tab("Encode"),
                          border_color='red', border_width=2, fg_color="transparent",
                          text_color="white", hover_color="#444444", height=40, width=200,
                          font=("Consolas", 18, "bold"), corner_radius=8)
en_button.place(x=500, y=140)

dc_button = ctk.CTkButton(app, text="Decode", command=lambda: show_tab("Decode"),
                          border_color='red', border_width=2, fg_color="transparent",
                          text_color="white", hover_color="#444444", height=40, width=200,
                          font=("Consolas", 18, "bold"), corner_radius=8)
dc_button.place(x=500, y=200)

switch = ctk.CTkSwitch(app, text="Switch Mode", command=toggle_mode,
                       button_color="red", progress_color="#444444",
                       font=("Consolas", 14))
switch.place(x=10, y=10)

app.mainloop()
