FROM python:3.12

# Install PostgreSQL and necessary libraries
RUN apt-get update && apt-get install -y postgresql postgresql-client libpq-dev

# Set the working directory in the container
WORKDIR /setup

# Copy all project files into the container
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Ensure the config file path is correct
CMD ["python3", "main.py"]
