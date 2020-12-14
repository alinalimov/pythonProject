from pythonApp import horoscope

month = input("what month were you born?\n")
day = input("on what day were you born?\n")
# zodiac_signs = list(
#     "capricorn" "aquarius" "pices" "aries" "taurus" "gemini" "cancer" "leo" "virgo" "libra" "scorpio" "Sagittarius")
# print (zodiac_signs[0])

months_list = \
{'January': {'delimiter': '19', 'before': 'capricorn', 'after': 'aquarius', 'names': ['jan', 'january', '1']},
'February': {'delimiter': '18', 'before': 'aquarius', 'after': 'aquarius', 'names': ['feb', 'February', '2']},
'March': {'delimiter': '20', 'before': 'aquarius', 'after': 'pices', 'names': ['mar', 'March', '3']},
'April': {'delimiter': '19', 'before': 'pices', 'after': 'aries', 'names': ['apr', 'April', '4']},
'May': {'delimiter': '20', 'before': 'aries', 'after': 'taurus', 'names' :['may', 'may', '5']},
'June': {'delimiter':'21', 'before':'taurus', 'after':'gemini', 'names' : ['jun','june', '6']},
'July': {'delimiter': '22', 'before': 'gemini', 'after': 'cancer', 'names': ['jul', 'july', '7']},
'August': {'delimiter': '22', 'before': 'cancer', 'after': 'leo', 'names':['aug', 'august', '8']},
'September': {'delimiter': '22', 'before': 'leo', 'after': 'virgo','names' :['sep', 'september', '9']},
'October': {'delimiter': '23', 'before': 'virgo', 'after': 'libra','names':['oct', 'october', '10']},
'November': {'delimiter': '22', 'before': 'libra', 'after': 'scorpio','names': ['nov', 'november', '11']},
'December': {'delimiter': '21', 'before': 'scorpio', 'after': 'sagittarius','names':['dec', 'december', '12']}
 }
for each_month in months_list :
    if month in months_list[each_month]['names']:
        month = each_month
    break

if int(day) < int(months_list[month]['delimiter']):
    your_sign = months_list[month]['before']
else :
    your_sign = months_list[month]['after']

print("your sign is " + your_sign)

horoscope.get(your_sign)