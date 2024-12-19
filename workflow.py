# workflow.py - Orchestrating Tasks with Parallel Processing

from celery import chain, group
from tasks import fetch_documents_task, extract_data_task, compare_data_task

def process_documents(blob_path):
    # Step 1: Fetch documents
    fetch_task = fetch_documents_task.s(blob_path)

    # Step 2: Extract data from each document in parallel
    extract_tasks = fetch_task | group(extract_data_task.s(doc) for doc in fetch_task.get())

    # Step 3: Compare the extracted data
    compare_task = compare_data_task.s()

    # Combine the workflow into a single chain
    workflow = chain(fetch_task, extract_tasks, compare_task)
    result = workflow.apply_async()
    return result
