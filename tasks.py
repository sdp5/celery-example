# tasks.py - Task Definitions

from celery_config import celery_app
import logging

logger = logging.getLogger(__name__)

@celery_app.task
def fetch_documents_task(blob_path):
    try:
        documents = fetch_documents(blob_path)  # Replace with your actual fetch logic
        return documents  # Assume this returns a list of document paths or contents
    except Exception as e:
        logger.error(f"Error fetching documents: {e}")
        raise

@celery_app.task
def extract_data_task(document):
    try:
        extracted_data = extract_data(document)  # Replace with your actual extraction logic
        return extracted_data
    except Exception as e:
        logger.error(f"Error extracting data: {e}")
        raise

@celery_app.task
def compare_data_task(extracted_data_list):
    try:
        comparison_results = compare_data(extracted_data_list)  # Replace with your actual comparison logic
        return comparison_results
    except Exception as e:
        logger.error(f"Error comparing data: {e}")
        raise
