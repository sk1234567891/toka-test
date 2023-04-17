# Use a Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port that the application will listen on
EXPOSE 5000

# Set the command to start the application
CMD [ "python", "main.py" ]

