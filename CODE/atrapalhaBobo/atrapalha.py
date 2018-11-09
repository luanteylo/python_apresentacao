from easygui import msgbox


import random, time

from time import strftime
from datetime import datetime


def isNowInTimePeriod(startTime, endTime, nowTime):
    if startTime < endTime:
        return nowTime >= startTime and nowTime <= endTime
    else: #Over midnight
        return nowTime >= startTime or nowTime <= endTime


def decision(probability):
	return random.random() < probability


m_start = '11:00AM'
m_end = '12:00AM'

t_start='2:00PM'
t_end='5:00PM'

n_start='9:00PM'
n_end='04:00AM'

erros = ['A catastrophic system error is issued. The z/TPF system performs an IPL.', 
		'Network dropped connection because of reset',
		'WARNING: PROGRAMMING BUG IN E2FSCK!  OR SOME BONEHEAD (YOU) IS CHECKING A MOUNTED (LIVE) FILESYSTEM.',
		'Failed to startup SSH session: Socket Error: success',
		'Error: Keyborad not Found',
		'ERROR: Bailling out, you are on your own. Good Luck.',
		'Setup is unable to Locate a Suitable version of  Directx on your Machine. Please reset it.',
		'500 Internal Server Error!']

while True:

	prob = 0
	timeNow = datetime.strptime(strftime("%I:%M%p"), "%I:%M%p")

	# check period
	if isNowInTimePeriod(datetime.strptime(m_start, "%I:%M%p"), datetime.strptime(m_end, "%I:%M%p"), timeNow):
		prob = 0.10 # 10%
	elif isNowInTimePeriod(datetime.strptime(t_start, "%I:%M%p"), datetime.strptime(t_end, "%I:%M%p"), timeNow):
		prob = 0.50 # 50%
	elif isNowInTimePeriod(datetime.strptime(n_start, "%I:%M%p"), datetime.strptime(n_end, "%I:%M%p"), timeNow):
		prob = 0.25 # 25%

	if prob != 0 and decision(prob):
		msgbox(random.choice(erros))


	sleep_time = random.randint(1, 60)
	time.sleep(sleep_time * 60)

