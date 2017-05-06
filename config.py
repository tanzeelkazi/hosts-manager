
# Path to the hosts file
hosts_file_path = '/etc/hosts'

# By default the script is configured to write to `hosts.txt`.
# You can switch it to write to the `hosts_file_path` but you will
# need to run the script as `sudo` to write to the system hosts file.
output_file_path = 'hosts.txt'
# output_file_path = hosts_file_path



# List of active plugins irrespective of their
# presence in the /plugins/ folder
# Ensure a comma exists in the end when there
# is only 1 value in this list.
# That is the only way Python recognizes a tuple
active_plugins = (
    #'apache_hosts_export',
)

# Any configurations for your plugins should go here.
# The key should match the plugin name.
plugin_config = {
    "apache_hosts_export": {
        "files": (
            '/etc/apache2/other/sites_conf/10-projects.conf',
        )
    }
}
