#!/usr/bin/env python3

""" Script to poll the UPS (via apcupsd) and pushing the data to statsd server
    to view the data in an Graphite/Grafana environment.
"""

import subprocess
import statsd
import config as cfg


apc_status = {}

# which status messages to publish. We use upsname as part of the topic
interesting = ('battv', 'linev', 'loadpct', 'mbattchg', 'timeleft')
# apcaccess command
command = ['apcaccess', 'status']


statsd_client_ups = statsd.StatsClient(host=cfg.statsd_config['host'],
                                       port=cfg.statsd_config['port'], prefix="ups")

proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

while True:
    # get STDOUT of process
    stdout = proc.stdout.readline().decode(errors='ignore')

    (key, spl, val) = stdout.partition(': ')
    key = key.rstrip().lower()
    val = val.split(' ')[0]
    apc_status[key] = val

    if stdout == '' and proc.poll() is not None:
        break

# Process returned an error
if proc.returncode != 0:
    error = "%s failed (%s)" % ("APC_Status", ' '.join(command))
    raise Exception(error)

# send values to statsd server
for values in interesting:
    statsd_client_ups.gauge(values, float(apc_status[values]), rate=1, delta=False)

