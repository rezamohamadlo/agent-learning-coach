def rename_task(tasks, task_id, new_title):
    """Return renamed task records without modifying the input records."""
    title = new_title.strip()
    if not title:
        raise ValueError("Title is required")
    if not any(task["id"] == task_id for task in tasks):
        raise ValueError("Unknown task ID")
    return [
        {**task, "title": title} if task["id"] == task_id else dict(task)
        for task in tasks
    ]
