#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException


"""
Methods here will run a scan, parse the output, and return an HTML report. 
Much of this code is pulled straight from the libnmap documentation.
"""


# start a new nmap scan on localhost with some specific options
def do_scan(targets, options):
    nmproc = NmapProcess(targets, options)

    # TODO: Add progress bar here. Look into the run_background function.
    rc = nmproc.run()
    if rc != 0:
        raise RuntimeWarning("Scan failed: {0}".format(nmproc.stderr))

    try:
        parsed = NmapParser.parse(nmproc.stdout)
    except NmapParserException as e:
        raise RuntimeWarning("Exception raised while parsing scan: {0}".format(e.msg))

    return parsed


def produce_html(nmap_report):
    """
    Results required for the html report:
      1. Host identification (definitely ip address, include hostname if returned)
      2. Is the host up?
      3. Ports and status (just if they're open)

    :param nmap_report: a parsed NmapProcess.stdout result
    :return: an html string with the results of the scan
    """


# print scan results from a nmap report
def print_scan(nmap_report):
    print("Starting Nmap {0} ( http://nmap.org ) at {1}".format(
        nmap_report.version,
        nmap_report.started))

    for host in nmap_report.hosts:
        if len(host.hostnames):
            tmp_host = host.hostnames.pop()
        else:
            tmp_host = host.address

        print("Nmap scan report for {0} ({1})".format(
            tmp_host,
            host.address))
        print("Host is {0}.".format(host.status))
        print("  PORT     STATE         SERVICE")

        for serv in host.services:
            pserv = "{0:>5s}/{1:3s}  {2:12s}  {3}".format(
                    str(serv.port),
                    serv.protocol,
                    serv.state,
                    serv.service)
            if len(serv.banner):
                pserv += " ({0})".format(serv.banner)
            print(pserv)
    print(nmap_report.summary)


if __name__ == "__main__":
    report = do_scan("127.0.0.1", "-sV")
    if report:
        print_scan(report)
    else:
        print("No results returned")
