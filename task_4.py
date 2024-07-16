def run4():
    new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
    completed_tasks = ['task_002', 'task_012', 'task_006']
    print('Список задач:', new_tasks)
    print('Выполненные задачи:', completed_tasks)
    # Завершение задачи task_005
    completed_tasks.append(new_tasks.pop(new_tasks.index('task_005')))
    # Удаление task_007 из списка
    new_tasks.remove('task_007')
    # Вывод последней задачи из списка
    print('Следующая задача: ', new_tasks[-1])