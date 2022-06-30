import re
import pandas as pd
from pykml.factory import KML_ElementMaker as KML
from lxml import etree

def get_school_name(full_name):
    tmp=re.search(r"區(.*)國民", full_name)
    if tmp:
        return tmp.group(1)
    
    tmp=re.search(r"市立(.*)國民", full_name)
    if tmp:
        return tmp.group(1)
    
    tmp=re.search(r"市立(.*)實驗", full_name)
    if tmp:
        return tmp.group(1)

    print("unknown: {}".format(full_name))
    return ""

def fld_gen(fld, fld_name, d_gps, d_num):
    for i in range(len(d_num)):
        school_name=d_num["name"][i]
        school_name=get_school_name(school_name)
        cnt=d_num[fld_name][i]
        ii=d_gps.index[d_gps["name"]=="縣立{}國小".format(school_name)]
        if len(ii)==1 and cnt>0:
            fld.append(KML.Placemark(
                KML.name("{}({:d})".format(school_name, cnt)),
                KML.Point(
                    KML.coordinates("{},{}".format(d_gps.lon[ii[0]], d_gps.lat[ii[0]]))
                )
            ))
        elif cnt==0:
            print("no position:{}".format(school_name))
        else:
            print("sth wrong:{}".format(school_name))
    
    return fld
        
if __name__=="__main__":
    d_gps=pd.read_csv("gps_data.csv", header=0)
    d_num=pd.read_csv("vacancy_list.csv", header=0)

    fld_s=["一般", "英語文", "自然科學", "音樂", "視覺藝術", "體育一般"]

    doc_t=KML.Document(KML.name("111新北教甄開缺地圖"))
    
    for nn in fld_s:
        ff=KML.Folder(KML.name(nn))
        doc_t.append(fld_gen(ff, nn, d_gps, d_num))

    with open("map_test.kml", "wb") as fp:
        fp.write(etree.tostring(doc_t, pretty_print=True, encoding='UTF-8'))
    
