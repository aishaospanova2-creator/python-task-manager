from src.main import add_task, complete_task, validate_index

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

def test_validate_index():
    assert validate_index("0", 1) is True
    assert validate_index("abc", 1) is False