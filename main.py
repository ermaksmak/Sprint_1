import task_1
import task_2
import task_3
import task_4
import task_5
import task_6
import task_7

def run_task(task_number):
    if task_number == 1:
        task_1.run1()
    elif task_number == 2:
        task_2.run2()
    elif task_number == 3:
        task_3.run3()
    elif task_number == 4:
        task_4.run4()
    elif task_number == 5:
        task_5.run5()
    elif task_number == 6:
        task_6.run6()
    elif task_number == 7:
        task_7.run7()
    else:
        print("Неверный номер задачи")

def close_program():
    print("Завершение программы")


if __name__ == "__main__":
    while True:
        task_number = int(input("Введите номер задачи для выполнения (1-7) или 0 для выхода: "))

        if task_number == 0:
            close_program()
            break
        run_task(task_number)