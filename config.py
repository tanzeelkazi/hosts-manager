
# you can change these to test paths to check the output
hosts_file_path = '/etc/hosts'
output_file_path = hosts_file_path


# List of active plugins irrespective of their
# presence in the /plugins/ folder
# Ensure a comma exists in the end when there
# is only 1 value in this list.
# That is the only way Python recognizes a tuple
active_plugins = (
    #'apache_hosts_export',
)

plugin_config = {
    "apache_hosts_export": {
        "files": (
            '/etc/apache2/other/sites_conf/10-projects.conf',
        )
    }
}
