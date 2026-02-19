# backend/app/routes_list.py

from backend.app.main import app

# Print all routes
for route in app.routes:
    print(f"{route.method} {route.path}")
