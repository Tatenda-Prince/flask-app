# Use official Python image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy app files
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

