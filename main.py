from tkinter import *
import random

que_list = []
ans_list = {}
correct_ans_list = {}
user_ans = {}
finale_score = 0
btn_color = 'black'


def next_question(task_num):
    global que_label
    global btn_next
    global finish_btn
    global ans
    global status_bar

    just_list = []
    for s in ans.curselection():
        just_list.append(ans.get(s))

    user_ans[que_list[task_num]] = just_list

    btn_next.pack_forget()
    status_bar.pack_forget()
    ans.delete(0, END)
    ans.config(height=len(ans_list[que_list[task_num + 1]]))

    que_label.config(text=que_list[task_num + 1])
    btn_next = Button(mini_menu_fr, text='Next', command=lambda: next_question(task_num + 1), bg=btn_color, fg='white',
                      width=12, height=2)
    status_bar = Label(mini_menu_fr, text="     task " + str(task_num + 2) + " of " + str(len(que_list)),
                       height=2, bg="black", fg='white', anchor=W)

    if ans_var.get():
        random.shuffle(ans_list[que_list[task_num + 1]])

    for k in ans_list[que_list[task_num + 1]]:
        ans.insert(END, k)

    if len(correct_ans_list[que_list[task_num + 1]]) != 1:
        ans.config(selectmode='multiple')
    else:
        ans.config(selectmode='single')

    if task_num + 2 == len(que_list):
        btn_next.config(state=DISABLED)

    btn_next.pack(side=RIGHT)
    status_bar.pack(side=LEFT)


def finish_test():
    global finale_score

    just_list = []
    for s in ans.curselection():
        just_list.append(ans.get(s))

    user_ans[que_list[len(que_list) - 1]] = just_list

    for ques in que_list:
        cur_score = 0
        if user_ans[ques] != None:
            for ans1 in user_ans[ques]:
                if len(correct_ans_list[ques]) == 1:
                    if ans1 in correct_ans_list[ques]:
                        finale_score += 1
                else:
                    if ans1 in correct_ans_list[ques]:
                        cur_score += 1
                    else:
                        cur_score -= 1

        if cur_score <= 0:
            cur_score = 0
        else:
            cur_score = cur_score / len(correct_ans_list[ques])
        finale_score += cur_score

    result_label.config(text="You scored " + str(finale_score) + '/' + str(len(que_list)) + "!")

    task_fr.pack_forget()
    score_fr.pack(fill=BOTH, expand=1)

    return


def start_test():
    global user_ans
    global que_rand
    global ans_rand
    global que_list

    main_fr.pack_forget()
    window_fr.pack_forget()
    task_fr.pack(fill=BOTH, expand=1)

    if que_var.get():
        temp = que_list[1:]
        random.shuffle(temp)
        temp2 = que_list[0]
        que_list = []
        que_list.append(temp2)
        que_list += temp

    user_ans = dict.fromkeys(que_list)


def test_settings():
    global st_btn, sett_btn, info_btn, exit_btn, random_que_btn, random_ans_btn, menu_btn

    st_btn.pack_forget()
    sett_btn.pack_forget()
    info_btn.pack_forget()
    exit_btn.pack_forget()
    random_que_btn.pack()
    random_ans_btn.pack()
    menu_btn.pack()


def main_menu():
    global st_btn, sett_btn, info_btn, exit_btn, random_que_btn, random_ans_btn, menu_btn

    random_que_btn.pack_forget()
    random_ans_btn.pack_forget()
    menu_btn.pack_forget()
    st_btn.pack(expand=1, side=TOP)
    sett_btn.pack(side=TOP)
    info_btn.pack(side=TOP)
    exit_btn.pack(side=TOP)


# READ FILE
test_lines = open("test/test.txt").readlines()

i = 0
while i < len(test_lines):
    question = test_lines[i]
    question = question[0:len(question) - 1]
    que_list.append(question)
    ans_list[question] = []
    correct_ans_list[question] = []

    while test_lines[i] != "(end)\n":
        i += 1
        answer = test_lines[i]

        if answer[len(answer) - 4:] == "(+)\n":
            answer = answer[0:len(answer) - 4]
            correct_ans_list[question].append(answer)
        else:
            answer = answer[0:len(answer) - 1]
        if answer != "(end)":
            ans_list[question].append(answer)
    i += 1

# WINDOW
window = Tk()
window.title("тестувальна система")
window.geometry('450x580')
window.update()
my_icon = PhotoImage(file='test/icon.png')
window.iconphoto(False, my_icon)

# MAIN MANU
window_fr = Frame(window, bg="#FFF83F")
window_fr.pack(fill=BOTH, expand=1)

main_fr = Frame(window_fr, bg='#FFF83F')
main_fr.pack(expand=1)

# BUTTONS on start menu
st_btn = Button(main_fr, text='Start', bg=btn_color, fg='white', width=15, height=3, command=start_test)
st_btn.pack(expand=1, side=TOP)

sett_btn = Button(main_fr, text='Settings', bg=btn_color, fg='white', width=15, height=3, command=test_settings)
sett_btn.pack(side=TOP)

info_btn = Button(main_fr, text='Info', bg=btn_color, fg='white', width=15, height=3)
info_btn.pack(side=TOP)

exit_btn = Button(main_fr, text='Exit', bg=btn_color, fg='white', width=15, height=3, command=window.quit)
exit_btn.pack(side=TOP)

# settings
que_var = BooleanVar()
ans_var = BooleanVar()
random_que_btn = Checkbutton(main_fr, text="Random Questions", bg="#FFF83F", variable=que_var, onvalue=True,
                             offvalue=False, font=('Times', 20))
random_ans_btn = Checkbutton(main_fr, text="Random Answers  ", bg="#FFF83F", variable=ans_var, onvalue=True,
                             offvalue=False, font=('Times', 20))

menu_btn = Button(window_fr, text='Menu', bg=btn_color, fg='white', width=15, height=3, command=main_menu)

# TASK
task_fr = Frame(window, bg="#FFF83F")

quest_fr = Frame(task_fr)
quest_fr.pack(side=TOP, fill='x', padx=10)
quest_fr.config(bg="#FFF83F")

que_label = Message(quest_fr, text=que_list[0], justify=CENTER, width=window.winfo_width() - 14, bg="#FFF83F",
                    fg="#0C090A", font=('Times', 20))
que_label.pack(side=TOP, pady=10, fill='x')
que_label.bind("<Configure>", lambda e: que_label.configure(width=e.width - 10))

ans_fr = Frame(task_fr)
ans_fr.pack(side=TOP, fill=BOTH, expand=1)
ans_fr.config(bg="#FFF83F")

ans = Listbox(ans_fr, height=len(ans_list[que_list[0]]), width=window.winfo_width(), font=('Times', 17),
              activestyle='dotbox', selectmode='single', bg="#FFF27A", fg="#0C090A", highlightbackground="black")
ans.pack(side=TOP)

for j in ans_list[que_list[0]]:
    ans.insert(END, j)

if len(correct_ans_list[que_list[0]]) != 1:
    ans.config(selectmode='multiple')

mini_menu_fr = Frame(task_fr, bg="black")
mini_menu_fr.pack(side=BOTTOM, fill='x')

btn_next = Button(mini_menu_fr, text='Next', command=lambda: next_question(0), bg=btn_color, fg='white', width=12,
                  height=2)
finish_btn = Button(mini_menu_fr, text='Finish test', command=finish_test, bg=btn_color, fg='white', width=12, height=2)
btn_exit = Button(mini_menu_fr, text='Exit', command=window.quit, bg=btn_color, fg='white', width=12, height=2)

status_bar = Label(mini_menu_fr, text="     task 1 of " + str(len(que_list)), height=2, bg="black", fg='white',
                   anchor=W)

btn_exit.pack(side=LEFT)
finish_btn.pack(side=LEFT)
btn_next.pack(side=RIGHT)
status_bar.pack(side=LEFT)

# SCORE
score_fr = Frame(window, bg="#FFF83F")
result_label = Label(score_fr, font=('Times', 30),
                     text="You scored " + str(finale_score) + '/' + str(len(que_list)) + "!", bg="#FFF83F",
                     fg="#0C090A")

btn_menu = Button(score_fr, text='Exit', command=window.quit, bg=btn_color, fg='white', width=12, height=2)

result_label.pack(side=TOP, expand=1)
btn_menu.pack(side=TOP, expand=1)

window.mainloop()
