# spectrum_image
use radio to show image in spectrum <br>  

通过SDR设备，发射无线信号，实现在频谱上显示图片的功能  <br>  
效率比较低，因为FFT算法是用python实现的，改成调用库就可以快点一点了  <br>  

##使用方法  <br>
  python3 spectrumImage.py test.jpg <br>  
  hackrf_transfer -t out.txt -f 490e6 -s 4e6 -a 0 -x 32 <br>  
  然后就可以在你的频谱瀑布上看见了  <br>  
  
##使用效果  <br>

  ![](https://github.com/cqb98/spectrum_image/raw/master/example/show_doge.png)   <br>   
  ![](https://github.com/cqb98/spectrum_image/raw/master/example/showRunning.png)   <br>   
  ![](https://github.com/cqb98/spectrum_image/raw/master/example/show_apple.png)  <br>  
  ![](https://github.com/cqb98/spectrum_image/raw/master/example/show_example.png)  <br> 

##基本思路  <br>
  图片取行->傅立叶逆变换->转化成适合hackrf的数据->保存成文件 <br>  
  
