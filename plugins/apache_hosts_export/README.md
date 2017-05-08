# Apache Hosts Export
This plugin is designed to work with the _Hosts Manager_ script.

This plugin will read any files configured to parse under the config and map `ServerName` directives to their corresponding IP addresses.

## Installation
This plugin is available out-of-the-box for _Hosts Manager_. No special installation is necessary.

Read the configuration section before using the plugin for the first time

## Configuration

### Activating the plugin
The plugin needs to be set as active under `./config.py` of _Hosts Manager_.

Remove the hash `#` in front of the plugin-name in the config to make active.

```
active_plugins = [
    'apache_hosts_export'
]
```

### Listing Apache config files to parse
A sample configuration exists under `./config.py`.

```
plugin_config = {
    "apache_hosts_export": {
        "files": [
            '/etc/apache2/other/sites_conf/10-projects.conf'
        ]
    }
}
```

The `apache_hosts_export` is the key for the configuration of this plugin. DO NOT CHANGE IT.

Under the `files` array add/remove the absolute path to the files that you need to parse automatically.

## Uninstall
Since this plugin is part of _Hosts Manager_, it is NOT recommended to uninstall it.

You can disable it, however, by either commenting-out (prefix with `#`) or removing the plugin-name from the `active_plugins` list.

```
active_plugins = [
    #'apache_hosts_export'
]
```
