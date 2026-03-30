#!/bin/bash

echo "Starting ingestion..."
python ingest.py

echo "Starting FastAPI..."
uvicorn src.main:app --host 0.0.0.0 --port 8000 &

echo "Waiting for FastAPI to be ready..."
while ! curl -f http://localhost:8000/ > /dev/null 2>&1; do
    echo "FastAPI not ready yet, waiting 2 seconds..."
    sleep 2
done

echo "FastAPI is ready! Starting Gradio..."
python gradio_app.py