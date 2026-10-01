import argparse
import json
import os
import sys
from datetime import datetime

def process_data(input_name, batch_size):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [INFO] Starting Non-Web Batch Processing Job...")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [INFO] Processing dataset target: {input_name}")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [INFO] Configured batch size: {batch_size} records")

    records = []
    for i in range(1, batch_size + 1):
        records.append({
            "record_id": i,
            "status": "PROCESSED",
            "score": round((i * 13.37) % 100, 2)
        })

    output_dir = "/data"
    os.makedirs(output_dir, exist_ok=True)
    output_filepath = os.path.join(output_dir, "processing_report.json")

    summary_payload = {
        "task": "SWE40006 - Task 4.4 High Distinction",
        "job_name": input_name,
        "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_records": batch_size,
        "summary": {
            "completed": len(records),
            "errors": 0
        },
        "records": records
    }

    with open(output_filepath, "w") as f:
        json.dump(summary_payload, f, indent=4)

    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [SUCCESS] Report successfully written to {output_filepath}")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [INFO] Job completed successfully. Container exiting with code 0.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI Data Processor")
    parser.add_argument("--name", type=str, default="Analytics-Batch-01", help="Dataset/Job name")
    parser.add_argument("--size", type=int, default=5, help="Number of records to process")
    args = parser.parse_args()

    process_data(args.name, args.size)