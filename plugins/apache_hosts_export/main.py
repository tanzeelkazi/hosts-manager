
import re

from __main__ import Version


DISPLAY_NAME = 'Apache Hosts Export'
VERSION = Version.get()


def main(config):
    hosts_map_dict = {}

    for file_name in config['files']:
        print "\t%s" % file_name
        parse_file(file_name, hosts_map_dict)

    return hosts_map_dict


def parse_file(file_name, hosts_map_dict):
    default_ip = '127.0.0.1'
    last_matched_ip = default_ip
    lines = None


    with open(file_name, "r") as f:
        lines = f.readlines()


    for line in lines:
        # Start tag for VirtualHost with IP
        match = re.match('<VirtualHost ([^*\:>]+)(?:\:[\d]+)?>', line)

        if match:
            last_matched_ip = match.group(1)
            continue

        # End tag for VirtualHost
        match = re.match('</VirtualHost>', line)

        if match:
            last_matched_ip = default_ip
            continue


        match = re.match('^[\s]*ServerName [\s]*([\S]+)[\s]*\n$', line)

        if match:
            host_name = match.group(1)

            if not last_matched_ip in hosts_map_dict:
                hosts_map_dict[last_matched_ip] = []

            if not host_name in hosts_map_dict[last_matched_ip]:
                hosts_map_dict[last_matched_ip].append(host_name)

    return hosts_map_dict
