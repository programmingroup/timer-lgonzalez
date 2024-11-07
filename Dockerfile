# Step 1: Set a Python base image
FROM python:3.8-slim-buster

# Step 2: Set the working directory inside the container
WORKDIR /python-docker

# Step 3: Install Flask
RUN pip install --no-cache-dir flask

# Step 4: Copy the application code into the container
COPY . .

# Step 5: Expose the port
EXPOSE 5000

#Step 6: Run the Flask application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
