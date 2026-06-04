# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

def format_task(task):
    status = "[ ]"

    task_id = task["id"]
    priority = task["priority"]
    title = task["title"]


    formatted_task = f"{status} [{priority}] #{task_id} - {title}"

    return formatted_task

def filter_tasks(tasks, show_done=True):
    if show_done:
        return tasks
    return [t for t in tasks if not t["done"]]
