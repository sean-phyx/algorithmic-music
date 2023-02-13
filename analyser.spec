# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['algorithmic-music\\src\\music-analyser-app\\music_analyser_app\\build\\analyser.py'],
    pathex=[],
    binaries=[],
    datas=[('algorithmic-music\\src\\music-analyser-app\\music_analyser_app\\build\\assets\\frame0\\', '.\\algorithmic-music\\src\\music-analyser-app\\music_analyser_app\\build\\assets\\frame0\\'), ('C:\\Users\\armat\\Documents\\algorithmic-music\\algorithmic-music\\required\\customtkinter', '.\\customtkinter')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Chord Analyser',
    datas=[('algorithmic-music\\src\\music-analyser-app\\music_analyser_app\\build\\assets\\frame0\\', '.'), ('C:\\Users\\armat\\Documents\\algorithmic-music\\algorithmic-music\\required\\customtkinter', '.\\customtkinter')],
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
    icon='algorithmic-music/src/music-analyser-app/music_analyser_app/build/assets/frame0/app_icon.png'
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='analyser',
)
