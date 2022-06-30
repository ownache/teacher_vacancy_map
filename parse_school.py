import re
import urllib.request

if __name__=="__main__":
    response = urllib.request.urlopen("https://school.qmap.tw/Taipei/")
    html_raw = response.read().decode("UTF-8").split("\n")
    fp2=open("gps_raw.csv", "w")
    school_list=[]

    target=re.compile(r"<td><a href=\"(.*)\"><u>(.*國小)</u></a></td>")

    for line_i in html_raw:
        tmp=target.search(line_i)
        if tmp:
            print("name:{}, url_id:{}".format(tmp.group(2),tmp.group(1)))
            response = urllib.request.urlopen("https://school.qmap.tw"+tmp.group(1))
            html = response.read().decode("UTF-8")
            gps_d=re.search(r"<span class=\"label label-info\">座標</span>&nbsp;(.*);<br>", html).group(1)
            fp2.write("{},{}\n".format(tmp.group(2), gps_d))

    fp2.close()