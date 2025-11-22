# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy everything from your repo into the container
COPY . /app /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Streamlit will run on
EXPOSE 7860

# Run the Streamlit app
CMD ["streamlit", "run", "app/app.py"]


