import tkinter as tk
from tkinter import filedialog, messagebox
import os


class TextReplacer:
    def __init__(self, master):
        self.master = master
        master.title("Замена текста")

        self.input_file_path = tk.StringVar()
        self.replacement_file_path = tk.StringVar()
        self.output_folder_path = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        fields = [
            ("Исходный файл с текстом:", self.input_file_path, self.select_input_file),
            ("Файл со словами для замены:", self.replacement_file_path, self.select_replacement_file),
            ("Папка для сохранения файлов:", self.output_folder_path, self.select_output_folder)
        ]

        for i, (label_text, var, command) in enumerate(fields):
            tk.Label(self.master, text=label_text).grid(row=i, column=0, sticky=tk.W)
            tk.Entry(self.master, textvariable=var, width=50).grid(row=i, column=1)
            tk.Button(self.master, text="Выбрать", command=command).grid(row=i, column=2)

        tk.Label(self.master, text="Символы для замены:").grid(row=3, column=0, sticky=tk.W)
        self.replace_symbol_entry = tk.Entry(self.master)
        self.replace_symbol_entry.grid(row=3, column=1)

        tk.Button(self.master, text="Заменить", command=self.replace_text).grid(row=4, column=1)

    def select_input_file(self):
        self.input_file_path.set(filedialog.askopenfilename(
            title="Выберите файл с исходным текстом",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        ))

    def select_replacement_file(self):
        self.replacement_file_path.set(filedialog.askopenfilename(
            title="Выберите файл со словами для замены",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        ))

    def select_output_folder(self):
        self.output_folder_path.set(filedialog.askdirectory(
            title="Выберите папку для сохранения файлов"
        ))

    def replace_text(self):
        replace_symbol = self.replace_symbol_entry.get()

        if not replace_symbol or not all(
                [self.input_file_path.get(), self.replacement_file_path.get(), self.output_folder_path.get()]):
            messagebox.showerror("Ошибка", "Заполните все поля и выберите все необходимые файлы и папки.")
            return

        try:
            with open(self.input_file_path.get(), 'r', encoding='utf-8') as file:
                input_text = file.read()

            with open(self.replacement_file_path.get(), 'r', encoding='utf-8') as file:
                replacements = file.read().splitlines()

            for word in replacements:
                modified_text = input_text.replace(replace_symbol, word)
                output_filename = os.path.join(self.output_folder_path.get(), f"{word}.txt")
                with open(output_filename, 'w', encoding='utf-8') as output_file:
                    output_file.write(modified_text)

            messagebox.showinfo("Успех", "Файлы успешно созданы.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TextReplacer(root)
    root.mainloop()