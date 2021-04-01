# LeagueScripts
League OCR using opencv and tesseract
It continously screenshots the area of the screen that holds the healthbar of the dragon when activated and passes the data in the form of a matrix into the tesseract API which then sends back the text to be 
compared to the current smite damage level. If the health is less than the smite damage, then the "smite" command is auto outputed to the user's keyboard.  


<p align="center">
  <img src="https://github.com/chun1213/LeagueScripts/blob/main/imgs/image2.png" width="600" />
</p>
This is a screenshot I got online and not mine.

<h2>Requirements:</h2>
This script is meant to be used while playing League of Legends.
In order to use this script, you will need to have tesseract installed and change the directories on line 57 and 58. 

```python 
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
tessdata_dir_config = r'--tessdata-dir "D:\Program Files (x86)\Tesseract-OCR\tessdata" --psm 8 --oem 4 -c tessedit_char_whitelist=0123456789'
```
 Change the directories on these lines to your tesseract installation and the tessdata. 
 <b> Make sure to only change the directory and not anything else! </b>
 
 <h2>Tech Used:</h2>
 This program uses OpenCV and Tesseract in Python
