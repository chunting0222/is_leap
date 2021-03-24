def is_leap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	elif year % 3200 != 0:
		return True
	else:
		return False

year = input('請輸入年份：')
year = int(year)

if is_leap(year):
	print(year, '為閏年')
