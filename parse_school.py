import re
import urllib.request

def get_gps_data(city_name):
    response = urllib.request.urlopen("https://school.qmap.tw/{}/".format(city_name))
    html_raw = response.read().decode("UTF-8").split("\n")
    fp2=open("gps_raw_{}.csv".format(city_name), "w")
    school_list=[]

    target=re.compile(r"<td><a href=\"(.*)\"><u>(.*國小)</u></a></td>")

    for line_i in html_raw:
        tmp=target.search(line_i)
        if tmp:
            print("name:{}, url_id:{}".format(tmp.group(2),tmp.group(1)))
            response = urllib.request.urlopen("https://school.qmap.tw"+tmp.group(1))
            html = response.read().decode("UTF-8")
            gps_d=re.search(r"<span class=\"label label-info\">座標</span>&nbsp;(.*);<br>", html).group(1)
            if gps_d:
                fp2.write("{},{}\n".format(tmp.group(2), gps_d))
            else:
                print("failed: {}\n".format(tmp.group(2)))

    fp2.close()

if __name__=="__main__":
    city_list=["TaipeiCity", "Taipei", "Keelung", "Yilan", "HsinchuCity", "Hsinchu", "Taoyuan", "Miaoli", "TaichungCity", "Changhua", "Nantou", 
        "ChiayiCity", "Chiayi", "Yunlin", "TainanCity", "KaohsiungCity", "Penghu", "Pingtung", "Taitung", "Hualien"]

    for ci in city_list:
        get_gps_data(ci)
        
