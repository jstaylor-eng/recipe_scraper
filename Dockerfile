# Base image
FROM python:3.10

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Start Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]

