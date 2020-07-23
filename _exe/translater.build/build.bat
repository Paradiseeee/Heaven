pyinstaller -F -w translater.py -i translater.ico 
cd dist
move translater.exe ../
cd ../

rmdir /S /Q build
rmdir /S /Q dist
rmdir /S /Q __pycache__
del translater.spec

exit
