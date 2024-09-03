# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the Python scripts into the container
COPY fixed_width_generator.py fixed_width_parser.py ./

# Generate the fixed-width file
RUN python fixed_width_generator.py

# Parse the fixed-width file and generate CSV
RUN python fixed_width_parser.py

# Set the default command to run the parser
CMD ["python", "fixed_width_parser.py"]