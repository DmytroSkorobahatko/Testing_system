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

    question_message.config(text=que_list[text_index], width=window.winfo_width() - que_mes_x)  # відступ
    question_message.pack(side=TOP, pady=que_mes_y, padx=que_mes_x, fill=X)
    question_message.bind("<Configure>", lambda e: question_message.configure(width=e.width - 10))

    ans_box.pack()

    # little_menu_frame
    little_menu_frame.pack(fill=X, side=BOTTOM)
    next_btn.pack(side=RIGHT, padx=5)
    #que_prev.pack(side=RIGHT, padx=5)
    menu_btn.pack(side=LEFT, padx=5)
    finish_btn.pack(expand=1)


def finish_test():
    test_frame.pack_forget()
    ans_frame.pack_forget()
    finish_btn.pack_forget()
    next_btn.pack_forget()

    finish_frame.pack(fill=BOTH, expand=1)

    finish_label.pack(fill=X)

    

def main_menu():
    test_frame.pack_forget()
    ans_frame.pack_forget()
    little_menu_frame.pack_forget()
    finish_frame.pack_forget()

    main_menu_frame.pack(fill=BOTH, expand=1)

def next_question():
    global text_index, text_count, que_list, test_que_ans_dict
    if text_index < text_count - 1:
        text_index = text_index + 1

    question_message.pack_forget()
    ans_box.delete(0, END)
    ans_box.config(height=len(test_que_ans_dict[que_list[text_index]]))

    for ans in test_que_ans_dict[que_list[text_index]]:
        ans_box.insert(END, ans)

    question_message.config(text=que_list[text_index], width=window.winfo_width() - (que_mes_x + 1))  # відступ
    question_message.pack(side=TOP, pady=que_mes_y, padx=que_mes_x, fill=X)


def prev_question():
    global text_index
    if text_index > 0:
        text_index = text_index - 1

    ans_box.delete(0, END)
    ans_box.config(height=len(test_que_ans_dict[que_list[text_index]]))

    for ans in test_que_ans_dict[que_list[text_index]]:
        ans_box.insert(END, ans)

    question_message.pack_forget()
    question_message.config(text=que_list[text_index])
    question_message.pack(side=TOP, pady=10, padx=10, fill=X)


# TEST all \/\/\/
# test frame
test_frame = Frame()
test_frame.config(bg="#69c")
# test_frame.pack()
# test_frame.pack_forget()
#

# Question
question_message = Message(test_frame, font=(16))
que_mes_x = 10
que_mes_y = 10

text_index = 0
#

# Ans
ans_frame = Frame()
ans_frame.config(bg="#69c")
#

test_lines = open("test/test.txt").readlines()

ans_list = []
que_list = []
test_que_ans_dict = dict()
# = open("test/test.txt").readlines()
i = 0
while test_lines[i] != "(end)":
    j = i + 1
    while test_lines[j] != "\n":
        test_que_ans_dict[str(test_lines[i].rstrip())] = []
        ans_list += [test_lines[j]]
        # print(ans_list)
        j += 1

    test_que_ans_dict[str(test_lines[i].rstrip())] = ans_list
    ans_list = []
    i = j + 1

for key in test_que_ans_dict:
    que_list += [key]

ans_box = Listbox(ans_frame, height=len(test_que_ans_dict[que_list[text_index]]), bg="#69c", font=(16))

for ans in test_que_ans_dict[que_list[text_index]]:
    ans_box.insert(END, ans)

ans_box.pack(fill=X)


print(test_que_ans_dict)
text_count = len(que_list)

##############################
#     print(key)
#
# print(test_que_ans)
# print(que_list)
# i = 0
# j = 0
# while test_lines[i] != "(end)":
#     j = i
#     while test_lines[j] != "\n":
#         print(test_lines[j].rstrip())
#         j += 1
#         if test_lines[i] == "\n":
#             print("Hello")
#
#     i = j + 1
# for lines in test_lines:
#     line = lines.rstrip()
#     print(line)
#############################3

# TEST /\/\/\

# MENU all \/\/\/
# Main menu \/
main_menu_frame = Frame()
main_menu_frame.config(bg="grey", relief=RAISED, borderwidth=1)
main_menu_frame.pack(fill=BOTH, expand=1)

start_btn = Button(main_menu_frame, text="start test", command=start_test)
start_btn.pack(expand=1)
# Main Menu /\

#
finish_frame = Frame()
finish_frame.config(bg="grey")

finish_label = Label(finish_frame)
finish_label.config(text="Congrat!")


# Little Menu \/
little_menu_frame = Frame()
little_menu_frame.config(bg="black", borderwidth=4)

next_btn = Button(little_menu_frame, text="next", command=next_question, bg="black", fg="white", font=(16))
#que_prev = Button(little_menu_frame, text="prev", command=prev_question, bg="black", fg="white")

menu_btn = Button(little_menu_frame, text="main menu", command=main_menu, bg="black", fg="white", font=(16))

finish_btn = Button(little_menu_frame, text="Finish Test", command=finish_test, bg="black", fg="white", font=(16))
# little menu /\
# MENU /\/\/\


window.mainloop()