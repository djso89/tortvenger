# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/home/djso89/tortvenger/Battle'],
             binaries=[],
             datas=[],
             hiddenimports=['ffpyplayer.threading', 'ffpyplayer.player.queue', 'ffpyplayer.player.frame_queue', 'ffpyplayer.player.decoder', 'ffpyplayer.player.clock', 'ffpyplayer.pic', 'ffpyplayer.tools', 'ffpyplayer.player.core'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
