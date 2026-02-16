# backend/app/routes_list.py

from backend.app.main import app

# Print a message to check if app is loaded
print("FastAPI app loaded successfully!")

# Print all routes
for route in app.routes:
    print(f"{route.method} {route.path}")
