# -*- mode: python ; coding: utf-8 -*-

import os
import site

from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import copy_metadata

# Set Project Name
APP_NAME = "streamlit_demo"

# Set file paths
project_base_path = os.path.abspath(
    os.path.join(os.path.dirname(__name__), '..', '..')
)
sources_path = os.path.join(project_base_path, 'src')
resources_path = os.path.join(project_base_path, 'res')

# Get Python Packages path
python_pkg_path = ""
python_packages = site.getsitepackages()
for path in python_packages:
    if "site-packages" in path:
        python_pkg_path = path
        break

# Setup App Data to add
datas = []
datas.append((f"{python_pkg_path}/streamlit/runtime", "./streamlit/runtime"))
datas += collect_data_files("streamlit")
datas += copy_metadata("streamlit")
datas.append((sources_path, 'src'))
datas.append((resources_path, 'res'))

a = Analysis(['run_app.py'],
    pathex=[sources_path],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name=APP_NAME,
    exclude_binaries=False, # Set to False for Single EXE file
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=APP_NAME,
)
