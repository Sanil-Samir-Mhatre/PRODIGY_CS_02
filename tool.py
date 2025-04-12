from tkinter import filedialog, Tk, Button, Label, messagebox
from PIL import Image
import os

KEY = 123  # Encryption key


def encrypt_image(input_path, output_path):
    try:
        image = Image.open(input_path).convert("RGB")
        pixels = image.load()
        width, height = image.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                # Safe XOR Encryption
                r_enc = r ^ KEY
                g_enc = g ^ KEY
                b_enc = b ^ KEY

                pixels[x, y] = (r_enc, g_enc, b_enc)

        image.save(output_path)
        messagebox.showinfo("Success", f"Image encrypted and saved to:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def decrypt_image(input_path, output_path):
    # Decryption is identical to encryption when using XOR
    encrypt_image(input_path, output_path)


def choose_file(encrypt=True):
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return

    base, ext = os.path.splitext(file_path)
    operation = "_encrypted" if encrypt else "_decrypted"
    output_path = f"{base}{operation}{ext}"

    if encrypt:
        encrypt_image(file_path, output_path)
    else:
        decrypt_image(file_path, output_path)


# GUI setup
root = Tk()
root.title("Pixel Manipulation for Image Encryption")

# Use full screen dimensions dynamically
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(True, True)

Label(root, text="Pixel Manipulation for Image Encryption", font=("Arial", 24, "bold")).pack(pady=40)

Button(root, text="Encrypt Image", command=lambda: choose_file(encrypt=True),
       width=30, height=3, font=("Arial", 16), bg="lightblue").pack(pady=30)

Button(root, text="Decrypt Image", command=lambda: choose_file(encrypt=False),
       width=30, height=3, font=("Arial", 16), bg="lightgreen").pack(pady=30)

Button(root, text="Exit", command=root.destroy,
       width=30, height=3, font=("Arial", 16), bg="lightcoral").pack(pady=30)

root.mainloop()
