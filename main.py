import customtkinter as ctk

key = {
    'А': '@', 'Б': '#', 'В': '$', 'Г': '%', 'Ґ': '^', 'Д': '&', 'Е': '*', 'Є': '(',
    'Ж': ')', 'З': '-', 'И': '_', 'І': '+', 'Ї': '=', 'Й': '{', 'К': '}', 'Л': '[',
    'М': ']', 'Н': ':', 'О': ';', 'П': '"', 'Р': "'", 'С': '<', 'Т': '>', 'У': ',',
    'Ф': '.', 'Х': '?', 'Ц': '/', 'Ч': '!', 'Ш': '`', 'Щ': '~', 'Ь': '|', 'Ю': '\\',
    'Я': '$', ' ': ' '
}
inv_key = {v: k for k, v in key.items()}

def encrypt(text):
    return ''.join(key.get(ch.upper(), ch) for ch in text)

def decrypt(text):
    return ''.join(inv_key.get(ch, ch) for ch in text)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Масонський шифратор")
app.geometry("500x300")

input_text = ctk.CTkTextbox(app, height=6)
input_text.pack(padx=20, pady=10, fill="x")

output_text = ctk.CTkTextbox(app, height=6)
output_text.pack(padx=20, pady=10, fill="x")

def on_encrypt():
    txt = input_text.get("1.0", "end").strip()
    output_text.delete("1.0", "end")
    output_text.insert("end", encrypt(txt))

def on_decrypt():
    txt = input_text.get("1.0", "end").strip()
    output_text.delete("1.0", "end")
    output_text.insert("end", decrypt(txt))

btn_frame = ctk.CTkFrame(app)
btn_frame.pack(pady=10)

ctk.CTkButton(btn_frame, text="Зашифрувати", command=on_encrypt).grid(row=0, column=0, padx=10)
ctk.CTkButton(btn_frame, text="Розшифрувати", command=on_decrypt).grid(row=0, column=1, padx=10)
ctk.CTkButton(btn_frame, text="Очистити", command=lambda: [input_text.delete("1.0", "end"),
                                                           output_text.delete("1.0", "end")]).grid(row=0, column=2, padx=10)

app.mainloop()
