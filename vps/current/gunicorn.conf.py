import multiprocessing

# Server Socket
bind = "0.0.0.0:8000"

# Worker Processes
workers = 2  # Adjusted for your 1 CPU limit
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 120
keepalive = 5

# Logging
loglevel = "info"
accesslog = "/app/logs/access.log"
errorlog = "/app/logs/error.log"

# Process Naming
proc_name = "enroute1"