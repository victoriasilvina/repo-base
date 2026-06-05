# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

def format_task(task):
    status = "[✓]" if task.get("done", False) else "[ ]"

    task_id = task["id"]
    priority = task["priority"]
    title = task["title"]


    formatted_task = f"{status} [{priority}] #{task_id} - {title}"

    return formatted_task

def filter_tasks(tasks, show_done=True):
    filtered = tasks if show_done else [
        t for t in tasks if not t.get("done", False)
    ]

    priority_order = {"high": 0, "medium": 1, "low": 2}

    return None