# process_sniffer
packet sniffer of specific process with wireshark!


![bandicam 2023-05-16 18-03-19-555](https://github.com/thewh1teagle/process_sniffer/assets/61390950/6af6ea0d-66cd-450b-99ea-ff80d9046ded)
## Setup
1. Install [wireshark](https://www.wireshark.org/download.html)
2. install Python dependencies
```shell
pip3 install -r requirements.txt
```



## Usage:
redirect stdout from Python into wireshark  
from `cmd` (only `cmd` support pipe):
```shell
python sniff.py -p chrome.exe | "C:\Program Files\Wireshark\Wireshark.exe" -k -i -
```
It will open wireshark and display all the packets arrived in that process name (from chrome.exe).
