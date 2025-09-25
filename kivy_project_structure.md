# Продакшн-структура Kivy-проекта

    todo_planner/
    │
    ├── assets/              # icons, pictures, fonts
    │
    ├── kv/                  # Kv files for screens
    │   ├── main_menu.kv
    │   ├── task_list.kv
    │   ├── add_task.kv
    │   ├── calendar.kv
    │   └── settings.kv
    │
    ├── locale/              # translations for multilingualism
    │   ├── en.json
    │   ├── ru.json
    │
    ├── models/              # business logic, work with database
    │   ├── __init__.py
    │   └── tasks.py
    │
    ├── screens/             # Screens (each in its own file)
    │   ├── __init__.py
    │   ├── main_menu.py
    │   ├── task_list.py
    │   ├── add_task.py
    │   ├── calendar.py
    │   └── settings.py
    │
    ├── utils/               # Auxiliary functions
    │ ├── i18n.py            # Multicipment
    │ ├ ─ Config.py          # download configurations
    │   └── logger.py
    │
    ├── .gitignore           # Exception Rules for Git
    ├── __init__.py          # file to make the project a package
    ├── config.json          # Configuration of the application (language, theme, database, window, logistics)
    ├── kivy_project_structure.md # File describing the structure of the project
    ├── main.py              # Entry point
    ├── requirements.txt     # Installation Requirements
    └──  TO_DO.kv            # main KV (Screenmanager + Navigation)


    
