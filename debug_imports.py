import sys
import os

print(f"Current directory: {os.getcwd()}")
print(f"Python path: {sys.path}")

print("\n--- Checking files ---")
models_path = r"backend/app/models.py"
schemas_path = r"backend/app/schemas.py"

print(f"models.py exists: {os.path.exists(models_path)}")
print(f"schemas.py exists: {os.path.exists(schemas_path)}")

if os.path.exists(models_path):
    print("\n--- models.py first 10 lines ---")
    with open(models_path, 'r') as f:
        for i, line in enumerate(f):
            if i < 10:
                print(line.strip())

print("\n--- Trying imports ---")
try:
    from backend.app import models
    print("✓ backend.app.models imported")
    print(f"  Available: {[x for x in dir(models) if not x.startswith('_')]}")
except Exception as e:
    print(f"✗ Error importing models: {e}")

try:
    from backend.app import schemas
    print("✓ backend.app.schemas imported")
    print(f"  Available: {[x for x in dir(schemas) if not x.startswith('_')]}")
except Exception as e:
    print(f"✗ Error importing schemas: {e}")
