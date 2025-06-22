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
#прозрачность
root.wm_attributes('-alpha', 0.9)

frame = Frame(root, bg='green')
frame.place(relwidth=0.7, rely=0.15, relheight=0.7)


#имя
title1 = Label(frame, text='ваше имя', bg='gray', font=40)
title1.pack()

loginInput1 = Entry(frame , bg='white')
loginInput1.pack()

#email
title2 = Label(frame, text='ваш email', bg='gray', font=40)
title2.pack()

loginInput2 = Entry(frame, bg='white')
loginInput2.pack()

#email
title3 = Label(frame, text='тема письма', bg='gray', font=40)
title3.pack()

loginInput3 = Entry(frame, bg='white')
loginInput3.pack()

#кнопки
btn = Button(frame, text='отправить email' , command=btn1_click)
btn.pack()

btn2 = Button(frame, text='очистить', command=btn2_click)
btn2.pack()




mainloop()