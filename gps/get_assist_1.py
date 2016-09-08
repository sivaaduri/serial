import requests
r = requests.get("http://online-live1.services.u-blox.com/GetOnlineData.ashx?token=5pEAcGuLwk-Nw3rqXOmqzA;gnss=gps;datatype=eph,alm;format=aid;lon=-83.726285;lat=42.231925;pacc=10;filteronpos")
filess=open("GPS_assist.txt",'wb')
filess.write(r.content)
filess.close()
print r.status_code
print r.headers
print r.content