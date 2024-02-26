import os
from time import sleep

ads=[
    "Buy this python book..",
    "Try this Py course..",
    "Drink a lot of water (2L per day minimum)"
    ]
ads_duration=[
    1.0,
    2.0,
    3.0
]

index=0
while True:
    ad= ads.pop(0)
    dur=ads_duration.pop(0)
    os.system("cls")
    print(f">>{ad}<<")
    sleep(dur)
    ads.append(ad)
    ads_duration.append(dur)


    