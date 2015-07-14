#!/usr/bin/env python2

import os, sys, getopt, subprocess

#Default Test to run
test = "short"

#List of drives to ignore
ignored = ['/dev/sdb']

#Location to store result of checks
log = "/tmp/"


def usage():
	print("Usage:\n\t-h, --help\t\tDisplay this\n\t-t, --test <test_type>\tType of test to run (short, long, badblocks)")

#check if user is root, else invoke sudo
if os.geteuid() == 0:
	command = []
else:
	command = ['sudo']

try:
	opts, args = getopt.getopt(sys.argv[1:],'ht:',['test=', 'help'])
except getopt.GetoptError:
	usage()
	exit(1)
if len(opts) > 0:
	for opt, arg in opts:
		if opt in ('-t', '--test'):
			test = arg
		elif opt in ['-h', '--help']:
			usage()
			exit(0)
		else:
			usage()
			exit(1)
else:
	usage()
	exit(1)
smartscan = list(command)
smartscan.extend(['smartctl', '--scan'])
drives = subprocess.check_output(smartscan).split('\n')[:-1]
for i in drives:
	i = i.split()
	if i[0] not in ignored:
		cmd = list(command)
		if test in ['short', 'long']:
			cmd.extend(['smartctl', '-t', test, i[0]])
			subprocess.call(cmd)
		elif test in ['badblocks']:
			cmd.extend(['badblocks', '-o', log + test + i[0].replace('/', '-'), i[0]])
			subprocess.Popen(cmd)
		else:
			print("Invalid options. Valid: short, long, badblocks")

exit(0)
