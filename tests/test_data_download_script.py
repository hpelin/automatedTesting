import os, runpy

def test_download_script():
    runpy.run_path("scripts/download_data.py")
    assert os.path.exists("data/raw/titanic.csv")