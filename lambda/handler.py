import json

def handler(event, context):
   print("Log event received")
   for record in event.get("records", []):
       print(record)
   return {"statusCode":200}

# --- Add this for local testing ---
if __name__ == "__main__":
    # Simulate a fake Lambda event
    mock_event = {
        "records": [
            "Test Record 1: KinD Cluster Heartbeat",
            "Test Record 2: ArgoCD Sync Status"
        ]
    }
    # Call the handler and print the result
    result = handler(mock_event, None)
    print(f"Result: {result}")