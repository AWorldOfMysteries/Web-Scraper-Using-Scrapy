import re

url = "https://hi.wikipedia.org/wiki/%E0%A4%B5%E0%A4%BF%E0%A4%B6%E0%A5%87%E0%A4%B7:%E0%A4%B8%E0%A4%AD%E0%A5%80_%E0%A4%AA%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A0/%E0%A5%A6"

if re.search(r'%E0%A4%B5%E0%A4%BF%E0%A4%B6%E0%A5%87%E0%A4%B7', url):
    print("Found")

else:
    print("Absent")
https://hi.wikipedia.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%87%E0%A4%A3%E0%A5%80:%E0%A4%AE%E0%A4%BE%E0%A4%A8%E0%A4%B5%E0%A4%B6%E0%A4%BE%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A5%8D%E0%A4%B0