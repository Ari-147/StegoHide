from email.policy import default
from tkinter.messagebox import showerror
from PIL import Image
from tkinter import filedialog

selected_image_path = None

def select_image(label, ctk):
    global selected_image_path
    filepath = filedialog.askopenfilename(filetypes=(("Image Files", "*.png *.jpg *.jpeg"),))
    if filepath:
        selected_image_path = filepath
        image = Image.open(filepath)
        image.thumbnail((280, 280))
        ctk_image = ctk.CTkImage(image, size=(280, 280))
        label.configure(image=ctk_image, text="")
        label.image = ctk_image  # Prevent garbage collection

def hide_message_in_image(image_path, message, output_path):
    img = Image.open(image_path).convert('RGB')
    width, height = img.size
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # Delimiter

    if len(binary_message) > width * height * 3:
        raise ValueError("Message is too large to fit in the image")

    pixels = img.load()
    index = 0
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            if index < len(binary_message):
                r = (r & 0xFE) | int(binary_message[index])
                index += 1
            if index < len(binary_message):
                g = (g & 0xFE) | int(binary_message[index])
                index += 1
            if index < len(binary_message):
                b = (b & 0xFE) | int(binary_message[index])
                index += 1
            pixels[x, y] = (r, g, b)

    img.save(output_path)

def save_encoded_image(message, selected_image_path, messagebox, filedialog):
    if not selected_image_path:
        showerror = messagebox.showerror("Error", "Please select an image first.")
        return
    filepath = filedialog.asksaveasfilename(defaultextenion = ".png",
                                            filetypes = (("PNG files", "*.png"),))
    if filepath:
        try:
            hide_message_in_image(selected_image_path, message, filepath)
            messagebox.showinfo("Sucess", "Message hidden successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

