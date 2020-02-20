# spectrum_image
use radio to show image in spectrum

通过SDR设备，发射无线信号，实现在频谱上显示图片的功能
效率比较低，因为FFT算法是用python实现的，改成调用库就可以快点一点了

##使用方法
  python3 spectrumImage.py test.jpg
  hackrf_transfer -t out.txt -f 490e6 -s 4e6 -a 0 -x 32
  然后就可以在你的频谱瀑布上看见了
  
##使用效果

  ![](https://github.com/cqb98/spectrum_image/raw/master/example/showRunning.png)  
  ![](https://github.com/cqb98/spectrum_image/raw/master/example/show_apple.png)  
  ![](https://github.com/cqb98/spectrum_image/raw/master/example/show_example.png)  

##基本思路
  图片取行->傅立叶逆变换->转化成适合hackrf的数据->保存成文件
  
