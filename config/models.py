import os
import sys
import pkgutil
import importlib
from app.models import __path__ as models_path

def models():
    # Tambahkan path aplikasi ke PYTHONPATH
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    
    # Impor otomatis semua model di folder models
    for _, module_name, _ in pkgutil.iter_modules(models_path):
        importlib.import_module(f"app.models.{module_name}")