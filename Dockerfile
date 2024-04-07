# FROM python:3.9-slim

# WORKDIR /app

# COPY . .

# RUN pip install --no-cache-dir google-api-python-client google-auth-httplib2 google-auth-oauthlib

# CMD ["python", "backup.py"]

# FROM python:3.9-slim
# WORKDIR /app
# COPY . .
# COPY credentials.json /app/
# RUN pip install --no-cache-dir google-api-python-client google-auth-httplib2 google-auth-oauthlib
# CMD ["python", "backup.py"]

FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the script, requirements, token file, credentials file, and last backup time file
COPY backup.py .
COPY requirements.txt .
COPY token.pickle .
COPY credentials.json .
COPY last_backup_time.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the backup script
CMD ["python", "backup.py"]
