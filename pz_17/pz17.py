#В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
#его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
#приближенный к оригиналу.
#https://www.digiseller.ru/preview/125077/p1_30116215520413.JPG

import tkinter as tk
from tkinter import ttk, filedialog


class ApplicationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Форма заявки")
        self.root.geometry("500x400")

        self.create_widgets()

    def create_widgets(self):
        # Основной фрейм
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Информация о допустимых типах файлов
        info_label = ttk.Label(
            main_frame,
            text="Допустимые типы вложений: zip, rar, txt, doc, jpg, png, gif, odt, xml\n"
                 "Макс. размер каждого файла: 1024kb.\n"
                 "Макс. общий размер файла: 2048kb.",
            justify=tk.LEFT
        )
        info_label.pack(anchor=tk.W, pady=(0, 10))

        # Создаем фрейм для формы
        form_frame = ttk.Frame(main_frame)
        form_frame.pack(fill=tk.X, pady=5)

        # Поля формы
        self.create_form_row(form_frame, "Ваше имя:", "*", 0)
        self.create_form_row(form_frame, "Ваш Email:", "*", 1)
        self.create_form_row(form_frame, "Тема письма:", "", 2)

        # Поля для прикрепления файлов
        self.file_entries = []
        for i in range(3):
            self.create_file_row(form_frame, f"Прикрепить файл:", i + 3)

        # Поле для сообщения
        msg_label = ttk.Label(main_frame, text="Ваше сообщение: *", justify=tk.LEFT)
        msg_label.pack(anchor=tk.W, pady=(10, 0))

        self.message_text = tk.Text(main_frame, height=5, wrap=tk.WORD)
        self.message_text.pack(fill=tk.X, pady=5)

        # Кнопки
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)

        send_btn = ttk.Button(button_frame, text="Отправить Email")
        send_btn.pack(side=tk.LEFT, padx=5)

        clear_btn = ttk.Button(button_frame, text="Очистить")
        clear_btn.pack(side=tk.LEFT)

    def create_form_row(self, parent, label_text, required_text, row):
        label = ttk.Label(parent, text=label_text)
        label.grid(row=row, column=0, sticky=tk.W, padx=(0, 5), pady=2)

        entry = ttk.Entry(parent)
        entry.grid(row=row, column=1, sticky=tk.EW, pady=2)

        if required_text:
            req_label = ttk.Label(parent, text=required_text, foreground="red")
            req_label.grid(row=row, column=2, sticky=tk.W, padx=(5, 0))

        parent.columnconfigure(1, weight=1)

    def create_file_row(self, parent, label_text, row):
        label = ttk.Label(parent, text=label_text)
        label.grid(row=row, column=0, sticky=tk.W, padx=(0, 5), pady=2)

        entry = ttk.Entry(parent)
        entry.grid(row=row, column=1, sticky=tk.EW, pady=2)
        self.file_entries.append(entry)

        browse_btn = ttk.Button(
            parent,
            text="Обзор...",
            width=8,
            command=lambda: self.browse_file(entry))
        browse_btn.grid(row=row, column=2, padx=(5, 0))

    def browse_file(self, entry):
        filetypes = [
            ('Архивы', '*.zip *.rar'),
            ('Текстовые файлы', '*.txt *.doc *.odt *.xml'),
            ('Изображения', '*.jpg *.png *.gif'),
            ('Все файлы', '*.*')
        ]

        filename = filedialog.askopenfilename(filetypes=filetypes)
        if filename:
            entry.delete(0, tk.END)
            entry.insert(0, filename)


if __name__ == "__main__":
    root = tk.Tk()
    app = ApplicationForm(root)
    root.mainloop()
