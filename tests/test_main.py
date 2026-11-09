from src.main import add_task, complete_task

def test_add_task():
    tasks = []
    updated = add_task(tasks, "Тестовая задача")
    assert len(updated) == 1
    assert updated[0]["title"] == "Тестовая задача"

def test_complete_task():
    tasks = [{"title": "Тест", "completed": False}]
    res = complete_task(tasks, 0)
    assert res is True
    assert tasks[0]["completed"] is True