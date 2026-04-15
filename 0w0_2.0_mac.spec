# -*- mode: python ; coding: utf-8 -*-
import sys

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('0w0.ico', '.')],
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
    [],
    exclude_binaries=True,
    name='0w0_2.0',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='0w0.icns',  # macOS는 .icns 사용
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='0w0_2.0',
)
app = BUNDLE(
    coll,
    name='0w0 Deadline Tracker.app',
    icon='0w0.icns',
    bundle_identifier='com.0w0.deadlinetracker',
    info_plist={
        'NSHighResolutionCapable': True,
        'CFBundleShortVersionString': '2.0',
        'CFBundleVersion': '2.0',
        'NSRequiresAquaSystemAppearance': False,  # 다크모드 지원
    },
)
