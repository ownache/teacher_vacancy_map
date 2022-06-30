# 準備
* Python
    * Pandas
    * pyKML
* 開缺 csv 檔案

# 建立方法
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

## 建立 kml 檔案
先把學校、科別、缺額建立成 vacancy_list.csv ，然後執行程式：
```
python map_gen.py
```
輸出會存在 map_test.kml 裡面，直接到 google my map 匯入圖層，就可以得到基本的開缺地圖了。

