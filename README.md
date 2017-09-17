# apc_ups_monitoring
This is a script to push statistic values from an APC UPS to a Statsd/Grafana setup.


## Configuration file
The statsd server settings are configured the [CONFIG][config.py] file.

```python
statsd_config = {'host': 'host.name',
                 'port': '8125'}

```

## Install Crontab
The easiest way to update your Graphite/Graphana diagrams continuously is to install a cronjob. You can add th following line to your crontabs and that's it.

    * * * * * /path/to/repo/apc_ups_monitoring/apc_ups_monitoring.py >/dev/null 2>&1

## License
This program is distributed under the terms of the GNU GPL v3. See the [LICENSE][license] file for more details.

[license]: https://raw.githubusercontent.com/cs-networks/apc_ups_monitoring/master/LICENSE
[config.py]: https://raw.githubusercontent.com/cs-networks/apc_ups_monitoring/master/config.py
