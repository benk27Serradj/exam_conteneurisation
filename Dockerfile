# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the whole project into the container
COPY . .

# Default command: evaluate all methods
CMD ["python", "evaluate.py", "--method", "all"]