#В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
#его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
#приближенный к оригиналу.
#https://www.digiseller.ru/preview/125077/p1_30116215520413.JPG

from tkinter import *
from tkinter import messagebox

#окно
root = Tk()

def btn1_click():
    name = loginInput1.get()
    email = loginInput2.get()
    message = loginInput3.get()

    info_str = f'имя: {str(name)}, email: {email}, message: {message}'
    messagebox.showinfo(title='название', message=info_str)

    #if error
    #messagebox.showerror(title='', message='ошибочка!')


    print('отправлено')

def btn2_click():
    print('очищено')


#задний фон
root['bg'] = 'white'

root.title('форма заявки')
root.geometry('540x690')
root.resizable(width=False, height=True)

#прозрачность
root.wm_attributes('-alpha', 0.9)

#имя
#frame_text = Frame(root)
#frame_text.place(relx=1)

title1 = Label(text='ваше имя', bg='gray', font=40)
title1.pack()

loginInput1 = Entry(bg='white')
loginInput1.pack()

#email
title2 = Label(text='ваш email', bg='gray', font=40)
title2.pack()

loginInput2 = Entry(bg='white')
loginInput2.pack()

#сообщение
title3 = Label(text='тема письма', bg='gray', font=40)
title3.pack()

loginInput3 = Entry (bg='white')
loginInput3.pack()

#кнопка отправки
frame_btn1 = Frame(root, bg='green' )
frame_btn1.place(relx=0.15, rely=0.5, relwidth=0.7, relheight=0.25)

btn = Button(frame_btn1, text='отправить email', font=120, command=btn1_click)
btn.pack()

#кнопка делит
frame_btn2 = Frame(root, bg='red')
frame_btn2.place(relx=0.15, rely=0.8, relwidth=0.7, relheight=0.25)

btn2 = Button(frame_btn2, text='очистить', font=120, command=btn2_click)
btn2.pack()





mainloop()