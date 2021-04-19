pyinstaller --onefile --hidden-import=ffpyplayer.threading --hidden-import=ffpyplayer.player.queue --hidden-import=ffpyplayer.player.frame_queue --hidden-import=ffpyplayer.player.decoder --hidden-import=ffpyplayer.player.clock --hidden-import=ffpyplayer.pic --hidden-import=ffpyplayer.tools --hidden-import=ffpyplayer.player.core --paths C:\Users\Daniel\AppData\Local\Programs\Python\Python39\share\ffpyplayer\ffmpeg\bin main.py
mv dist/main.exe ./
rm -r build/ 
rm -r dist/
