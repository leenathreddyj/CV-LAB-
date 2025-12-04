#!/bin/bash
# Railway startup script
# Railway automatically sets PORT environment variable
if [ -z "$PORT" ]; then
    PORT=5000
fi
echo "Starting Gunicorn on port $PORT"
exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 2 --timeout 300 --access-logfile - --error-logfile - --log-level info app:app
