# OpenCV-Video2ASCII

## 安裝
:warning: 環境需求:Python3 以上、FFmpeg
### 1.下載原碼
```
git clone https://github.com/AloneAlongLife/OpenCV-Video2ASCII.git
```

### 2.運行前請先安裝依賴庫
```
pip install -r requitements.txt
```

### 3.將影片檔放置於根目錄下
```
OpenCV-Video2ASCII
  ├─ .gitignore
  ├─ README.md
  ├─ requirements.txt
  ├─ Start.cmd
  ├─ Video2asciiv5.py
  └─ 你的影片
```

### 4.運行
:information_source: 於Windows命令提示字元中運行時，建議將自型更改為點陣字型、大小8x8以獲得最佳觀賞體驗。
```
python3 Video2asciiv5.py
```

### 5.更新日誌
```
2022/9/3
更新，版本為v6
FPS控制器等待時間由追蹤系統時間更改為追蹤音軌時間
新增Start.cmd

2021/11/20
首次發布，版本為v5
```