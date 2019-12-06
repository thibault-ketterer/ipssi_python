
percent = 0.999
days = 365.25
daysdiff = days - (days * percent)
print(daysdiff)
hourdiff = daysdiff * 24
print(hourdiff)
minutediff = (hourdiff - int(hourdiff)) * 60
print(minutediff)
secondsdiff = (minutediff - int(minutediff)) * 60
print(secondsdiff)
