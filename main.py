from tkinter import *

window = Tk()
window.config(bg="white")
window.geometry('500x400')

window.update()

def start_test():
    global text_index
    text_index = 0
    main_menu_frame.pack_forget()

    test_frame.pack(fill=BOTH)
    ans_frame.pack(fill=BOTH, expand=1)

    question_message.config(text=que_text_list[text_index], width=window.winfo_width() - que_mes_x)  # відступ
    question_message.pack(side=TOP, pady=que_mes_y, padx=que_mes_x, fill=X)
    question_message.bind("<Configure>", lambda e: question_message.configure(width=e.width-10))

    # little_menu_frame
    little_menu_frame.pack(fill=X, side=BOTTOM)
    que_next.pack(side=RIGHT, padx=5)
    que_prev.pack(side=RIGHT, padx=5)
    menu_btn.pack(side=LEFT, padx=5)


def finish_test():
    test_frame.pack_forget()
    ans_frame.pack_forget()
    finish_btn.pack_forget()
    little_menu_frame.pack_forget()

    main_menu_frame.pack(fill=BOTH, expand=1)


def next_question():
    global text_index, text_count
    if text_index < text_count - 1:
        text_index = text_index + 1
    else:
        finish_btn.pack(expand=1)

    question_message.pack_forget()

    # до 2 (-)=(перенос строки), НЕ ОБОВ'ЯЗКОВО
    if que_text_list[text_index][-4:-1] == "(-)":
        if que_text_list[text_index + 1][-4:-1] == "(-)":
            que_text_list[text_index + 1] = que_text_list[text_index + 1][:-4] + "\n" + que_text_list[text_index + 2]
            que_text_list.remove(que_text_list[text_index + 2])
            text_count -= 1

        que_text_list[text_index] = que_text_list[text_index][:-4] + "\n" + que_text_list[text_index + 1]
        que_text_list.remove(que_text_list[text_index + 1])
        text_count -= 1
    # уже краще

    question_message.config(text=que_text_list[text_index], width=window.winfo_width() - (que_mes_x + 1))  # відступ
    question_message.pack(side=TOP, pady=que_mes_y, padx=que_mes_x, fill=X)


def prev_question():
    global text_index
    if text_index > 0:
        text_index = text_index - 1

    question_message.pack_forget()
    question_message.config(text=que_text_list[text_index])
    question_message.pack(side=TOP, pady=10, padx=10, fill=X)


# TEST all \/\/\/
# test frame
test_frame = Frame()
test_frame.config(bg="brown")
# test_frame.pack()
# test_frame.pack_forget()
#

# Question
question_message = Message(test_frame)
que_mes_x = 10
que_mes_y = 10

que_text_list = open("test/questions/questions.txt").readlines()
text_count = len(que_text_list)
text_index = 0
#


# ans
ans_text = open("test/answer/answers.txt").readlines()
ans_count = len(ans_text)

ans_frame = Frame()
ans_frame.config(bg="brown")

ans_listbox = Listbox(ans_frame)
ans_listbox.config()
ans_listbox.pack(expand=1)
for i in ans_text:
    ans_listbox.insert(0, i)


# ans_button = Button(ans_frame)
# for i in range(0, ans_count):
#     Button(ans_frame, text=ans_text[i], ).pack(expand=1, side=LEFT, pady=10, padx=10)
#

test_file = open("test/test.txt").readlines()
i=0
while test_file[i] != "(end)":
    while test_file[i] != "\n" :
        test_file[i]
        que_ans_list_pair = [[ans_listbox], [ans_listbox]]
        que_ans_list_pair[] = (que_text_list[i], ans_listbox)
        i += 1


# TEST /\/\/\

# MENU all \/\/\/
# Main menu \/
main_menu_frame = Frame()
main_menu_frame.config(bg="grey", relief=RAISED, borderwidth=1)
main_menu_frame.pack(fill=BOTH, expand=1)

start_btn = Button(main_menu_frame, text="start test", command=start_test)
start_btn.pack(expand=1)
# Main Menu /\

# Little Menu \/
little_menu_frame = Frame()
little_menu_frame.config(bg="black", borderwidth=4)

que_next = Button(little_menu_frame, text="next", command=next_question, bg="black", fg="white")
que_prev = Button(little_menu_frame, text="prev", command=prev_question, bg="black", fg="white")

menu_btn = Button(little_menu_frame, text="main menu", command=finish_test, bg="black", fg="white")

finish_btn = Button(little_menu_frame, text="Finish Test", command=finish_test, bg="black", fg="white")
# little menu /\
# MENU /\/\/\


window.mainloop()