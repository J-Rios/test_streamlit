# -*- mode: python ; coding: utf-8 -*-

import os

# Set Project Name
APP_NAME = "streamlit_demo"

# Set file paths
project_base_path = os.path.abspath(
    os.path.join(os.path.dirname(__name__), '..', '..')
)
sources_path = os.path.join(project_base_path, 'src')
resources_path = os.path.join(project_base_path, 'res')

a = Analysis(['run_app.py'],
    pathex=[sources_path],
    binaries=[],
    datas=[
        (sources_path, 'src'),
        (resources_path, 'res')
    ],
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
