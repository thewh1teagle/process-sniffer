# process_sniffer

## Setup
1. Install wireshark
2. install Python dependencies
```shell
pip3 install -r requirements.txt
```

## Usage:
redirect stdout from Python into wireshark
```shell
python sniff.py -p chrome.exe | "C:\Program Files\Wireshark\Wireshark.exe" -k -i -
```
It will open wireshark and display all the packets arrived in that process name (from chrome.exe).