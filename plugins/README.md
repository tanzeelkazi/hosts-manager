# Plugins
This directory contains all the plugins that can be used with _Hosts Manager_.

Information on configuration and usage for each plugin should be listed under the README file for the plugin itself.

Even if you have a plugin in this directory, it will only be processed if it is listed as an active-plugin under `active_plugins` in `./config.py`.

```
active_plugins = [
    'apache_hosts_export'
]
```

## Installing plugins
Copy the plugin folder to this directory. List the plugin folder name under `active_plugins` and configure according to the instructions that came with the plugin itself.

```
active_plugins = [
    'apache_hosts_export',
    '<new_plugin_name>'
]
```

The next time you run `hm build` it should start working with your new plugin.

_A word of caution!_ Any time you install a new plugin make sure it behaves as expected by setting your `output_file_path` to a test file.

_CHECK ANY CODE RUN AS SUDO; IT COULD BE HARMFUL!!!_

## Creating Plugins
TODO: Fill this section
