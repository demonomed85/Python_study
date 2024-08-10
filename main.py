from tkinter import Tk, Button, Label, Entry, Listbox, LEFT, BOTTOM, Frame, END, font, DISABLED, NORMAL, ACTIVE


def disable_all_button(event):
    selected_task_indices = readyBox.curselection()
    if selected_task_indices:
        delete_button.config(state=DISABLED)
        take_inWork_button.config(state=DISABLED)
        ready_button.config(state=DISABLED)

def disable_take_inWork_button(event):
    selected_task_indices = in_workBox.curselection()
    if selected_task_indices:
        delete_button.config(state=NORMAL)
        take_inWork_button.config(state=DISABLED)
        ready_button.config(state=NORMAL)

def disable_ready_button(event):
    selected_task_indices = task_listBox.curselection()
    if selected_task_indices:
        delete_button.config(state=NORMAL)
        take_inWork_button.config(state=NORMAL)
        ready_button.config(state=DISABLED)

def add_task():
    task = task_entry.get()
    if task:
        task_listBox.insert(END, task)
        task_entry.delete(0, END)

def delete_task():
    list_newTask = task_listBox.curselection()
    list_inWork = in_workBox.curselection()
    if list_newTask:
        for index in list_newTask[::-1]:
            task_listBox.delete(index)
    elif list_inWork:
        for index in list_inWork[::-1]:
            in_workBox.delete(index)

def get_inWork():
    selected_task_indices = task_listBox.curselection()
    if selected_task_indices:
        for index in selected_task_indices[::-1]:
            task = task_listBox.get(index)
            in_workBox.insert(END, task)
            task_listBox.delete(index)

def to_readyList():
    selected_task_indices = in_workBox.curselection()
    if selected_task_indices:
        for index in selected_task_indices[::-1]:
            task = in_workBox.get(index)
            readyBox.insert(END, task)
            in_workBox.delete(index)


root = Tk()
root.geometry("1200x700")
root.title("OP08 - Task list")

root.configure(background="azure2")

frame_enter_new_task = Frame(root, bg="azure2")
frame_enter_new_task.pack()
frame_board_title = Frame(root, bg="azure2")
frame_board_title.pack()
frame_board = Frame(root, bg="azure2")
frame_board.pack()
frame_button = Frame(root, bg="azure2")
frame_button.pack()
frame_sign = Frame(root, bg="azure2")
frame_sign.pack(side=BOTTOM)


text1 = Label(frame_enter_new_task, text="Введите новую задачу:", bg="azure2", font="bolt")
text1.pack(pady=10)

task_entry = Entry(frame_enter_new_task, width=30, bg="antique white")
task_entry.pack(side=LEFT)

add_task_button = Button(frame_enter_new_task, text="Добавить задачу", command=add_task)
add_task_button.pack(padx = 10)

font14 = font.Font(family="Helvetica", size=14, weight="bold")
text2 = Label(frame_board_title, text="Список задач:", bg="azure2", font=font14)

text2.pack(pady=40)
text2 = Label(frame_board_title, text="Новые задачи", bg="azure2", font="bolt")
text2.pack(side=LEFT, padx=120)
text2 = Label(frame_board_title, text="В работе", bg="azure2", font="bolt")
text2.pack(side=LEFT, padx=120)
text2 = Label(frame_board_title, text="Выполненные", bg="azure2", font="bolt")
text2.pack(side=LEFT, padx=120)

task_listBox = Listbox(frame_board, height=20, width=50, bg="antique white")
task_listBox.pack(side=LEFT)
task_listBox.bind("<<ListboxSelect>>", disable_ready_button)
in_workBox = Listbox(frame_board, height=20, width=50, bg="antique white")
in_workBox.pack(side=LEFT)
in_workBox.bind("<<ListboxSelect>>", disable_take_inWork_button)
readyBox = Listbox(frame_board, height=20, width=50, bg="antique white")
readyBox.pack(pady=15)
readyBox.bind("<<ListboxSelect>>", disable_all_button)


delete_button = Button(frame_button, text="Удалить задачу", command=delete_task, state="disabled")
delete_button.pack(side=LEFT, padx=10)

take_inWork_button = Button(frame_button, text="Взять в работу", command=get_inWork, state="disabled")
take_inWork_button.pack(side=LEFT, padx=10)

ready_button = Button(frame_button, text="Выполнена", command=to_readyList, state="disabled")
ready_button.pack(side=LEFT, padx=10)


text2 = Label(frame_sign, text="Сделано Сергеевым Дмитрием", bg="azure2")
text2.pack(pady=10)


root.mainloop()