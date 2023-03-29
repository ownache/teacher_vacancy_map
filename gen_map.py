import csv, re

name_spec=[
    r"區(.*)國民",
    r"市立(.*)國民",
    r"市立(.*)實驗",
    r".*立(.*)國小",
    r"(.*)國小",
]

str_placemark="\
<Placemark><name>{}({})</name>\n\
\t<Point><coordinates>{},{}</coordinates></Point>\n\
</Placemark>\n"

str_doc="<Document \
xmlns=\"http://www.opengis.net/kml/2.2\" \
xmlns:atom=\"http://www.w3.org/2005/Atom\" \
xmlns:gx=\"http://www.google.com/kml/ext/2.2\">\n\
<name>{}</name>\n{}\
</Document>\n"

def wrap_folder(name, str_placemarks):
    return "<Folder><name>{}</name>\n".format(name)+str_placemarks+"</Folder>\n"

def wrap_map(name, str_folders):
    return str_doc.format(name, str_folders)

def school_name_parser(name):
    for i in name_spec:
        tmp=re.search(i, name)
        if tmp:
            return tmp.group(1)

def gen_map(csv_vacancy="vacancy_list.csv", csv_gps="gps_raw.csv", map_name="teacher_vacancy_map.kml", title="teacher vacancy map"):
    data={}
    with open(csv_vacancy, encoding='utf-8') as fp:
        rows=csv.reader(fp)
        cols=next(rows)[1:]
        for r in rows:
            data[r[0]]=r[1:]

    data_gps={}
    with open(csv_gps, encoding='utf-8') as fp1:
        rows=csv.reader(fp1)
        for r in rows:
            data_gps[r[0]]=r[1:]

    data_all={}
    for i in data:
        for j in data_gps:
            if j in school_name_parser(i):
                data_all[i]={'name':i, 'gps':[float(ii) for ii in data_gps[j]], 'data':[int(ii) for ii in data[i]]}

    str_folders=""
    for i, folder_i in enumerate(cols):
        str_placemarks=""
        for j in data_all:
            if data_all[j]['data'][i]>0:
                str_placemarks+=str_placemark.format(data_all[j]['name'], data_all[j]['data'][i], data_all[j]['gps'][0], data_all[j]['gps'][1])

        str_folders+=wrap_folder(folder_i, str_placemarks)

    str_map=wrap_map(title, str_folders)
    with open(map_name,'w') as fp:
        fp.write(str_map)

if __name__=="__main__":
    gen_map()