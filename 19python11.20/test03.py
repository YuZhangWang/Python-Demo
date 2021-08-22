# P151 5.6
import datetime as dt

Dateformat = dt.datetime(1999, 8, 8, 1, 30, 0)

print(Dateformat.strftime("%Y-%m-%d %H:%M:%S"))
print(Dateformat.strftime("%Y,%B,%d %H:%M:%S"))
print(Dateformat.strftime("%Y-%b-%d %H:%M:%S"))
print(Dateformat.strftime("%y-%m-%d %H:%M:%S"))
print(Dateformat.strftime("%y,%B,%d %H:%M:%S"))
print(Dateformat.strftime("%y-%b-%d %H:%M:%S"))
print(Dateformat.strftime("%Y-%m-%d %I%p"))
print(Dateformat.strftime("%Y.%m.%d %H-%M-%S"))
print(Dateformat.strftime("%Y,%m,%d %A"))
print(Dateformat.strftime("%Y,%m,%d %a"))
