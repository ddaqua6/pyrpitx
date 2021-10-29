# pyrpitx
<b>Python library for RPiTX</b><br>
This library simplifies transmitting signals by Python scripts, simply import this library (pyrpitx.py) to your code and use the pre-defined functions to command rpitx.<br><br>
Requires rpitx by F5OEO, sox.<br>Required Python packages: afsk, os, time. <br><b>Also requires to have rpitx version 1 in /home/pi/rpitx-1 because of pifm not being present in v2. Please install also the old version of rpitx (v1) to /home/pi/rpitx-1</b><br>
The code directs commands for rpitx to /home/pi/rpitx, if you have rpitx in different folder, please edit the pyrpitx.py file.<br><br>
Learn how to use: simply open pyrpitx.py and study the defined functions, comments are present. All you need to study is what arguments do
each function require (eg. cw(frq, text) or nfm(frq, audio)).<br>
<br>
Please use audio in wav only. All other information about rpitx - <a href="github.com/F5OEO/rpitx">F5OEO</a>.<br><br>
How to install<br>
Simply clone this git into your Raspberry and copy the pyrpitx.py into folder, in which your Python script runs. Then add "import pyrpitx" at the start of your Python script. Please note that you need to have rpitx installed in folder /home/pi/rpitx, otherwise you need to edit the pyrpitx.py.<br>
<br>Requirements installation<br>
afsk: pip install afsk (for APRS)<br>
rpitx: Please see F5OEO's rpitx git for info, install into /home/pi/rpitx. (Software for transmitting)<br>
sox: sudo apt install sox (WAV file processor)<br>
os: pip install os (for running the scripts)<br>
time: pip install time (for timing the events)
