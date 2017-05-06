
import re


PLUGIN_DISPLAY_NAME = 'Apache Hosts Export'


class Version:
    MAJOR = 0
    MINOR = 1
    PATCH = 0
    META = ''

    @classmethod
    def get(cls):
        version = str(cls.MAJOR) + \
                  '.' + str(cls.MINOR) + \
                  '.' + str(cls.PATCH)

        if len(cls.META) > 0:
            version += '-' + cls.META

        return version


def parse_file(file_name):
    hosts = []
    lines = []

    with open(file_name, "r") as f:
        lines = f.readlines()

    for line in lines:
        match = re.match('^[\s]+ServerName ([\S]+)[\s]*\n$', line)

        if match:
            hosts.append(match.group(1))

    return hosts

def get_hosts_map_dict(hosts):
    hosts_map_dict = {
        "127.0.0.1": hosts
    }

    return hosts_map_dict

def main(config):
    print "%s v%s" % (PLUGIN_DISPLAY_NAME, Version.get())

    hosts = []

    for file_name in config['files']:
        print "\t%s" % file_name
        hosts += parse_file(file_name)

    hosts_map_dict = get_hosts_map_dict(hosts)

    return (
        ('apache_hosts_export', hosts_map_dict),
    )
