# Step 1: Use Python 3.8 image
FROM python:3.8-slim

# Step 2: Install necessary packages
RUN apt-get update \
    && apt-get install -y ffmpeg libsndfile1 \
    && pip install --upgrade pip

# Step 3: Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Step 4: Copy application code
COPY ./app /app

# Step 5: Expose port and start FastAPI app
EXPOSE 8000
CMD ["uvicorn", "app.orchestrator:app", "--host", "0.0.0.0", "--port", "8000"]
