
import datetime as dt


x = dt.datetime.now()

print(x)
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)
print(x.microsecond)


print()

t = dt.datetime(2021,12,2,9,34,45)
print(t)

#strftime() 


n = dt.datetime.now()

print(x.strftime('%A')) #weakday full version
print(x.strftime('%a')) #weakday sort version
print(x.strftime('%B')) #Month full version
print(x.strftime('%b')) #month sort version
print(x.strftime('%Y')) #year full version
print(x.strftime('%y')) #year sort version
