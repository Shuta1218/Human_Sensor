import machine
import prequests
import time
import ntptime
import ufirebase as firebase
rtc = machine.RTC()
ntptime.NTP_DELTA = ntptime.NTP_DELTA -32400
ntptime.settime()

url = "https://script.google.com/macros/s/AKfycbwsxZ2bPELKn0YcQ0bywYvCRUK9hLXBnqjJcQS5vVFhdazy-zPIjgWFNVSw6u9rlWxU/exec?count="



SW1 = 13

sw1 = machine.Pin(SW1, machine.Pin.IN)

count = 0
while True:
    # 反応があったときだけ記録する（１＝反応あり）
    if sw1.value() == 1:
        count += 1
        print('-----')
        print(str(count) + 'count')
        print(rtc.datetime())
        # firebase.patch("sensor_time",{str(rtc.datetime()[4]):count})
        url=url+str(count)
        sensor = prequests.get(url)
        sensor.close()
        time.sleep(5)
        url = "https://script.google.com/macros/s/AKfycbwsxZ2bPELKn0YcQ0bywYvCRUK9hLXBnqjJcQS5vVFhdazy-zPIjgWFNVSw6u9rlWxU/exec?count="
        
        
        
        



# 謎文字化けする
# while True:
#     if sw1.value() == 1:
#         print ('反応あり')
#         time.sleep(1)
#     elif sw1.value() == 0:
#         print ('反応なし')
#         time.sleep(1)