
# Base Image Python + Linux
FROM python:3.11-slim

# Working directory inside container
WORKDIR /app

# Copying dependencies file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Document the PORT
EXPOSE 5000

# Setting default Environment Variable
ENV PORT=5000

# Command to start app(Gunicorn)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]