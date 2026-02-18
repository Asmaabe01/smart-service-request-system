# backend/app/routes_list.py

from backend.app.main import app

print("=" * 50)
print("FASTAPI APPLICATION ROUTES")
print("=" * 50)

# Print all routes
for route in app.routes:
    methods = ", ".join(route.methods) if hasattr(route, 'methods') else "ANY"
    print(f"{methods:20} {route.path}")

print("=" * 50)
print(f"Total routes: {len(app.routes)}")
print("=" * 50)
