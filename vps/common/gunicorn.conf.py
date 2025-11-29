# ⚠️ Replace:
# PROJECT_NAME → e.g., myproject



import multiprocessing

# Server Socket
bind = "0.0.0.0:8000"

# Worker Processes
workers = 2  # Adjust according to CPU limits
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 120
keepalive = 5

# Logging
loglevel = "info"
accesslog = "/app/logs/access.log"
errorlog = "/app/logs/error.log"

# Process Naming
proc_name = "PROJECT_NAME"  # Replace with your project name
