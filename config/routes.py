import importlib
import pkgutil
from app.routes import __path__ as routes_path

def routes(app):
    # Register semua router secara dinamis
    for module_info in pkgutil.iter_modules(routes_path):
        if not module_info.name.startswith("_"):  # Abaikan file seperti __init__.py
            module = importlib.import_module(f"app.routes.{module_info.name}")
            if hasattr(module, "router"):  # Pastikan module memiliki atribut `router`
                app.include_router(module.router, prefix=f"/{module_info.name}", tags=[module_info.name.capitalize()])