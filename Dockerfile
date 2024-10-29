# Base image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Make sure the runserver.sh script is executable (if you have one)
RUN chmod +x /app/runserver.sh

# Set the command to run your application (uncomment and modify if needed)
# CMD ["bash", "/app/runserver.sh"]
