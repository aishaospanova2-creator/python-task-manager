def add_task(tasks: list, task_name: str) -> list:
    """Добавляет новую задачу в список."""
    if task_name:
        tasks.append({"title": task_name, "completed": False})
    return tasks

def list_tasks(tasks: list) -> list:
    """Возвращает список всех задач."""
    return tasks

def complete_task(tasks: list, index: int) -> bool:
    """Отмечает задачу как выполненную по индексу."""
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        return True
    return False

def validate_index(index_str: str, max_len: int) -> bool:
    """Проверяет корректность введенного индекса."""
    if index_str.isdigit():
        idx = int(index_str)
        return 0 <= idx < max_len
    return False

def main():
    tasks = []
    print("=== Менеджер задач ===")
    tasks = add_task(tasks, "Изучить Git Rebase")
    print("Список задач:", list_tasks(tasks))

if __name__ == "__main__":
    main()
# Search functionality start
