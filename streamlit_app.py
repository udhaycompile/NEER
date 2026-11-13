# Entry point for Streamlit Community Cloud.
# Makes the `neer` package importable, then runs the real dashboard.
import sys
import pathlib
import runpy

ROOT = pathlib.Path(__file__).parent
sys.path.insert(0, str(ROOT))
runpy.run_path(str(ROOT / "neer" / "app" / "dashboard.py"), run_name="__main__")
