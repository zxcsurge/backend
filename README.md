# Проект FastAPI

Таск-трекер курса backend-разработки. Задачи хранятся в SQLite, у сущности Task есть полный CRUD.

## Запуск

```bash
source .venv/bin/activate
pip install -r requirements.txt
cd task_app
uvicorn main:app --reload
```

Проверка в браузере: http://127.0.0.1:8000/docs

Эндпоинты:

- `POST /tasks` — создать задачу
- `GET /tasks` — список задач
- `GET /tasks/{task_id}` — одна задача
- `PATCH /tasks/{task_id}` — изменить задачу
- `DELETE /tasks/{task_id}` — удалить задачу
