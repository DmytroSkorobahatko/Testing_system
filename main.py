from tkinter import *

window = Tk()
window.config(bg="white")
window.geometry('400x300')


def close_main_menu():
    main_menu_frame.pack_forget()
    test_frame.pack(fill=BOTH, expand=1)

    question_label.config(text="que_text", bg="darkgray")
    question_label.pack(side=TOP)


def open_main_menu():
    main_menu_frame.pack(fill=BOTH, expand=1)
    test_frame.pack_forget()


test_frame = Frame()
test_frame.config(bg="brown")
test_frame.pack()
test_frame.pack_forget()

question_label = Label(test_frame)





main_menu_frame = Frame()
main_menu_frame.config(bg="grey", relief=RAISED, borderwidth=1)
main_menu_frame.pack(fill=BOTH, expand=1)

start_btn = Button(main_menu_frame, text="start test", command=close_main_menu)
start_btn.pack(expand=1)

little_menu_frame = Frame()
little_menu_frame.config(bg="black", borderwidth=2)
little_menu_frame.pack(fill=X, side=BOTTOM)

finish_btn = Button(little_menu_frame, text="finish test", command=open_main_menu, bg="black", fg="white")
finish_btn.pack(side=RIGHT)

window.mainloop()from tkinter import *

window = Tk()
window.config(bg="white")
window.geometry('400x300')


def close_main_menu():
    main_menu_frame.pack_forget()
    test_frame.pack(fill=BOTH, expand=1)

    question_label.config(text="que_text", bg="darkgray")
    question_label.pack(side=TOP)


def open_main_menu():
    main_menu_frame.pack(fill=BOTH, expand=1)
    test_frame.pack_forget()


test_frame = Frame()
test_frame.config(bg="brown")
test_frame.pack()
test_frame.pack_forget()

question_label = Label(test_frame)





main_menu_frame = Frame()
main_menu_frame.config(bg="grey", relief=RAISED, borderwidth=1)
main_menu_frame.pack(fill=BOTH, expand=1)

start_btn = Button(main_menu_frame, text="start test", command=close_main_menu)
start_btn.pack(expand=1)

little_menu_frame = Frame()
little_menu_frame.config(bg="black", borderwidth=2)
little_menu_frame.pack(fill=X, side=BOTTOM)

finish_btn = Button(little_menu_frame, text="finish test", command=open_main_menu, bg="black", fg="white")
finish_btn.pack(side=RIGHT)

window.mainloop()from tkinter import *

window = Tk()
window.config(bg="white")
window.geometry('400x300')


def close_main_menu():
    main_menu_frame.pack_forget()
    test_frame.pack(fill=BOTH, expand=1)

    question_label.config(text="que_text", bg="darkgray")
    question_label.pack(side=TOP)


def open_main_menu():
    main_menu_frame.pack(fill=BOTH, expand=1)
    test_frame.pack_forget()


test_frame = Frame()
test_frame.config(bg="brown")
test_frame.pack()
test_frame.pack_forget()

question_label = Label(test_frame)





main_menu_frame = Frame()
main_menu_frame.config(bg="grey", relief=RAISED, borderwidth=1)
main_menu_frame.pack(fill=BOTH, expand=1)

start_btn = Button(main_menu_frame, text="start test", command=close_main_menu)
start_btn.pack(expand=1)

little_menu_frame = Frame()
little_menu_frame.config(bg="black", borderwidth=2)
little_menu_frame.pack(fill=X, side=BOTTOM)

finish_btn = Button(little_menu_frame, text="finish test", command=open_main_menu, bg="black", fg="white")
finish_btn.pack(side=RIGHT)

window.mainloop()