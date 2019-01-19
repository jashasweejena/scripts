import pyperclip
import sys

mac = sys.argv[1]

converted = " "

length = len(mac)

x = 0

for i in range(0, length, 2):
    converted = converted + ":" + (mac[x:i])
    x = i

final = converted[3 : len(converted)]
print(final)

pyperclip.copy(final)

