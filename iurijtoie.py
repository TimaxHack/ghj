import  os
#blob:https://moidom.citylink.pro/8840450b-77f0-4754-a1b1-20defa264c73

papks = 'out'
names = '1234567890768967867968'
if not os.path.exists(papks):
    os.mkdir(papks)

os.system(f"ffmpeg.exe -i https://s1.moidom-stream.ru/s/public/0000000103.m3u8 {papks}/{names}.jpg")
