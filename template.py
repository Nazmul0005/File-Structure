import os
from pathlib import Path

project_name="com"

list_of_files=[
    f"{project_name}/mhire/app/config/config.py",
    f"{project_name}/mhire/app/database/databse_connection.py",
    f"{project_name}/mhire/app/database/databse_manager.py",
    f"{project_name}/mhire/app/services/feature1/a_schema.py",
    f"{project_name}/mhire/app/services/feature1/a.py",
    f"{project_name}/mhire/app/services/feature1/a_router.py",
    f"{project_name}/mhire/app/services/feature2/b_schema.py",
    f"{project_name}/mhire/app/services/feature2/b.py",
    f"{project_name}/mhire/app/services/feature2/b_router.py",
    f"{project_name}/mhire/app/main.py",
    f"nginx/nginx.conf",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "docker-compose.yml",
    ".env",
    "README.md",
    
]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir , exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open (filepath , "w") as f:
            pass

    else:
        print(f"File already exists : {filepath}")