import datetime
import platform

#System Current DATE
y = datetime.datetime.now()
print("\n" , y)

#Return the year
print(y.year)
print(y.strftime("%A"))

#Create Date Objects
print(datetime.datetime(2019,1,19))

#Get the hour ,time and second
x = datetime.datetime.strptime("10::23::45" , "%H::%M::%S").time()
print(x.hour , x.minute , x.second)

# Directives Used : %a	Weekday, short version	Wed	
# Directives Used : %A	Weekday, full version	Wednesday	
# Directives Used : %w	Weekday as a number 0-6, 0 is Sunday	3	
# Directives Used : %d	Day of month 01-31	31	
# Directives Used : %b	Month name, short version	Dec	
# Directives Used : %B	Month name, full version	December	
# Directives Used : %m	Month as a number 01-12	12	
# Directives Used : %y	Year, short version, without century	18	
# Directives Used : %Y	Year, full version	2018	
# Directives Used : %H	Hour 00-23	17	
# Directives Used : %I	Hour 00-12	05	
# Directives Used : %p	AM/PM	PM	
# Directives Used : %M	Minute 00-59	41	
# Directives Used : %S	Second 00-59	08	
# Directives Used : %f	Microsecond 000000-999999	548513	
# Directives Used : %z	UTC offset	+0100	
# Directives Used : %Z	Timezone	CST	
# Directives Used : %j	Day number of year 001-366	365	
# Directives Used : %U	Week number of year, Sunday as the first day of week, 00-53	52	
# Directives Used : %W	Week number of year, Monday as the first day of week, 00-53	52	
# Directives Used : %c	Local version of date and time	Mon Dec 31 17:41:00 2018	
# Directives Used : %x	Local version of date	12/31/18	
# Directives Used : %X	Local version of time	17:41:00	
# Directives Used : %%	A % character	% 