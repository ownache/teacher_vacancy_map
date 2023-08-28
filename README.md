# 準備
* 開缺 csv 檔案

# 建立方法
修改 input.ini 檔案，其中：
* VacancyListCSV: csv 檔案路徑，裡面存放各學校開缺情況
* SchoolGpsCSV: csv 檔案路徑，裡面存放學校 gps 座標
* MapName: 輸出檔名，副檔名為 kml
* MapTitle: 地圖標題

完成後儲存 input.ini，在資料夾中空白處右鍵，點選"在終端中開啟"。接著輸入指令：
```
gen_map.exe inputs.ini
```
kml 檔案就會在資料夾中產生。

# 其他細節
## 抓取學校 GPS 資料
調整 parse_school.py 內的程式碼，修改成目標縣市的網址：
```python
response = urllib.request.urlopen("https://school.qmap.tw/Taipei/")
```
調整 Regex，縮小抓取的學校範圍：
```python
target=re.compile(r"<td><a href=\"(.*)\"><u>(.*國小)</u></a></td>")
```
然後執行程式：
```
python parse_school.py
```
輸出會儲存在 gps_raw.csv 裡面。但因為資料老舊，可能會有缺漏，之後再手動補上即可。修改後的資料存在 gps_data.csv 裡面，每年的更動幅度應該不大。

資料來源：https://school.qmap.tw/



