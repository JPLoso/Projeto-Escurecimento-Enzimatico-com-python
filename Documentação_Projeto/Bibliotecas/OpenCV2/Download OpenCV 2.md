Fonte - https://docs.opencv.org/4.x/da/df6/tutorial_py_table_of_contents_setup.html

Download 
(ubuntu)
```
sudo apt-get install python3-opencv
```
(windows) 
```
Below Python packages are to be downloaded and installed to their default locations.

1. Python 3.x (3.4+) or Python 2.7.x from [here](https://www.python.org/downloads/).
   
2. Numpy package (for example, using `pip install numpy` command).

3. Matplotlib (`pip install matplotlib`) (_Matplotlib is optional, but recommended since we use it a lot in our tutorials_).
   
- Install all packages into their default locations. Python will be installed to `C:/Python27/` in case of Python 2.7.
- After installation, open Python IDLE. Enter **import numpy** and make sure Numpy is working fine.
- Download latest OpenCV release from [GitHub](https://github.com/opencv/opencv/releases) or [SourceForge site](https://sourceforge.net/projects/opencvlibrary/files/) and double-click to extract it.
- Goto **opencv/build/python/2.7** folder.
- Copy **cv2.pyd** to **C:/Python27/lib/site-packages**.
- Copy the **opencv_world.dll** file to **C:/Python27/lib/site-packages**
- Open Python IDLE and type following codes in Python terminal.
```

importar
```
import cv2 as cv
print(cv.__version__)
```
se for executar sem erros, Foi baixado com sucesso