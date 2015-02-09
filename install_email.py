from crontab import CronTab
import config
import os
import sys

sys_path = os.path.dirname(os.path.realpath(__file__))
cmd = "python '" + sys_path + "/email_send.py'"
print sys_path
print cmd
#configure flickr search

def writeSlice(start, end, time):

	#Time of Day to send
	h = str(int(time[:2]))
	m = str(int(time[3:]))

	#Generate months to send
	m_s = int(start[:2])
	m_e = int(end[:2])

	#Gen days to send
	d_s = int(start[3:])
	d_e = int(end[3:])

	if (m_s > m_e) or (m_s == m_e and d_s > d_e) or (d_s > 31) or (d_e > 31) or (m_s > 12) or (m_e > 12):
		raise Exception('Incorrect Dates')
	else:
		d_s = str(d_s)
		d_e = str(d_e)
		numJob = 1
		mon_1 = m_s
		if m_s == (m_e - 1):
		    numJob = 2
		    mon_2 = m_e
		elif m_s <= (m_e - 2):
		    numJob = 3
		    mon_2 = m_e
		    mon_3 = str((m_s+1))+'-'+str((m_e-1))

		slices = []  
		if numJob > 1:
		    slices.append(m + ' ' + h + ' '+d_e+'-31 '+str(mon_1)+' *')
		    slices.append(m + ' ' + h + ' 1-'+d_e+' '+str(mon_2)+' *')
		else:
		    slices.append(m + ' ' + h + ' '+d_s+'-'+d_e+' '+str(mon_1)+' *')
		if numJob > 2:
		    slices.append(m + ' ' + h + ' 1-31 '+str(mon_3)+' *')
		return slices


if __name__ == "__main__":
	#Grab from Config File when to send
	start = config.date_settings['date_start']
	end = config.date_settings['date_end']
	time = config.date_settings['time_to_send']

	cron = CronTab()
	sli = writeSlice(start, end, time)
	for x in xrange(0, len(sli)):
		print sli[x]
		job = cron.new(command=cmd, comment='Job Command Created by install_email.py')
		job.setall(sli[x])
		cron.write()

