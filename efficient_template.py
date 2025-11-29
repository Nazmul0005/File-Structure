import os

structure = {
    "Project_Name": [
        "requirements.txt",
        "Dockerfile",
        ".dockerignore",
        "docker-compose.yml",
        ".env",
        "README.md",
        ".gitignore",
        {"mhire": [
            {"app": [
                {"config": ["config.py"]},
                {"core": ["__init__.py", "middleware.py", "security.py", "dependencies.py"]},
                {"database": ["database_connection.py", "database_manager.py"]},
                {"models": ["model.py"]},
                {"services": [
                    {"service1": ["service1.py", "service1_schema.py", "service1_router.py"]},
                    {"service2": ["service2.py", "service2_schema.py", "service2_router.py"]},
                    {"service3": ["service3.py", "service3_schema.py", "service3_router.py"]}
                ]},
                {"utils": ["__init__.py", "logger.py", "helpers.py", "response.py"]},
                "main.py"
            ]}
        ]},
        {"tests": ["test.py"]},
        {"nginx": ["nginx.conf"]},
        {"gunicorn": ["gunicorn.conf"]}
    ]
}


def create_structure(base_path, items):
    """Recursively create folders and files."""
    for item in items:
        if isinstance(item, str):
            # File path
            file_path = os.path.join(base_path, item)
            file_dir = os.path.dirname(file_path)
            if file_dir:
                os.makedirs(file_dir, exist_ok=True)
            # Only create if file doesn't exist or is empty
            if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
                open(file_path, "w").close()
                print(f"Created file: {file_path}")
            else:
                print(f"File already exists: {file_path}")

        elif isinstance(item, dict):
            for folder, subitems in item.items():
                folder_path = os.path.join(base_path, folder)
                os.makedirs(folder_path, exist_ok=True)
                print(f"Created folder: {folder_path}")
                create_structure(folder_path, subitems)


def main():
    for root, items in structure.items():
        os.makedirs(root, exist_ok=True)
        print(f"Created root folder: {root}")
        create_structure(root, items)


if __name__ == "__main__":
    main()
