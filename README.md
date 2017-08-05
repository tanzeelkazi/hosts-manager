# Hosts Manager

_Version 1.4.0_

This module is aimed at simplifying management of the system `hosts` file for developers like myself. Although it is simple to edit `hosts` files on machines to test our projects, managing them however, across machines or even over time is a drudging task.

This project was done with the aim of managing the hosts file with relatively simple configs and without the need to install a lot of dependencies.

The script is also extensible via plugins to automate custom workflows. One plugin, `Apache Hosts Export`, which I needed for myself, I have made available out-of-the-box with this package. It searches for `ServerName` directives in the given list of apache config files and maps them to `127.0.0.1` (localhost) automatically.

A sample output in hosts file looks like this:

```
# tkhm - username - START
# tkhm - vX.Y.Z

# apache_hosts_export - START

127.0.0.1		sampledomain myproject.local

# apache_hosts_export - END



# manual-hosts-maps - 00-default_conf.py - default - START

127.0.0.1		testdomain.local

# manual-hosts-maps - 00-default_conf.py - default - END



# tkhm - username - END
```

As you can see the hosts file clearly denotes the entries added by the script.

The `tkhm - <username>` is a special delimiter for the script to hook onto when performing cleanup operations. DO NOT change or remove these delimiters as it can screw-up the cleanup operation.

As you can see, the script maintains configurations on a per-user basis. So two-or-more users can easily use this script without blowing away each other's configuration on the same machine.

> It is possible to clear out everyone's config on the machine
> with the `clean-all` command but the script asks to confirm
> your actions before proceeding. It is assumed anyone with
> `sudo` rights is responsible enough to take the best actions
> for the system.

The script is designed NOT to delete entries in the hosts file except what it itself has put in. It is important, however, that you DO NOT modify the `tkhm` delimiters in any way as this WILL mess up the start and end of the cleanup operation. The script aborts without writing to the output file if it is unable to determine the start and end points of its configuration.

Contents:

- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
    - [Manual hosts configuration](#manual-hosts-configuration)
    - [config.py](#configpy)
        - [hosts\_file\_path](#hosts_file_path)
        - [output\_file\_path](#output_file_path)
        - [active\_plugins](#active_plugins)
        - [plugin\_config](#plugin_config)
- [Execution Syntax](#execution-syntax)
    - [build](#build)
    - [clean](#clean)
    - [clean-all](#clean-all)
- [Checking Versions](#checking-versions)
- [Uninstall](#uninstall)
- [Plugins](#plugins)


## Requirements
The script is primarily designed to:

- run on a unix-like environment
- run on Python 2.7+ (Python 3+ does NOT work)

It assumes the location of the system `hosts` file as `/etc/hosts`. Although it is NOT written specific to any OS, it may NOT be possible to run this on Windows.


## Installation
Simply clone (or download) the git repository to a directory of your choice.

You should add the directory to your system `PATH` variable to make the script run from any directory. The script is agnostic to where it is run from (it switches to the script directory when running operations).

It is recommended that you check the package configuration before first-run.


## Configuration
The module configuration is under `./config.py`. It has comments to make it as self-explanatory as possible.

### Manual hosts configuration
Manual host mapping configuration is placed under `./hosts_maps/`. The script consumes any file in this directory ending in `_conf.py` as a configuration file. See `./hosts_maps/00-default_conf.py` to start adding your hosts.

A typical configuration looks like this:

```
{
    # key
    "default": {
        # ip
        "127.0.0.1": [
            # list of hostnames
            'testdomain.local'
        ]
    }
}
```

This outputs the following to the hosts file:

```
# manual-hosts-maps - 00-default_conf.py - default - START

127.0.0.1		testdomain.local

# manual-hosts-maps - 00-default_conf.py - default - END
```

But you can also easily nest configurations like this:

```
{
    "top_level_key": {
        "sub_level_1_key": {
            ...
                "sub_level_n_key": {
                    "127.0.0.1": [
                        # list of hostnames
                        'testdomain.local'
                    ]
                }
        }
    }
}
```

The script will parse nested configurations and hosts-maps belonging to each branch of the tree and print them separately in the hosts file.

```
# manual-hosts-maps - 00-default_conf.py - top_level_key - sub_level_1_key - ... - sub_level_n_key - START

127.0.0.1		testdomain.local

# manual-hosts-maps - 00-default_conf.py - top_level_key - sub_level_1_key - ... - sub_level_n_key - END
```

That's all there is to a manual-hosts configuration.

> If this your first-time configuring the script then
> read on to the end of the configuration section to make
> sure you don't miss other important configuration directives.


### config.py
The config file is a collection of variables that dictates the behavior of the script.

#### hosts\_file\_path
This should be a string denoting the absolute path to your system hosts file. As is obvious the default value is `/etc/hosts`.

#### output\_file\_path
This should be the location of the output file.

Note that by default the build generates a `./hosts.txt` file with the intended output instead of writing back to the system's `hosts` file. This is done to give you time to check the script's output before the system file's are overridden.

Once you have confidence in the execution you should uncomment the following line in the config to start writing to the system's hosts file directly.

```
output_file_path = hosts_file_path
```

Note: Writing to the system's hosts file needs elevated privileges. You will have to run the script with `sudo`. ALWAYS be aware of what you run as `sudo`.

#### active\_plugins
This is list of the active plugins for the script.

Plugins for the script are under `./plugins/<plugin_name>`. Only plugin-names listed under this config variable will be run. Make sure the plugin-name is entered correctly and the plugin exists when modifying this value.

#### plugin\_config
Plugin specific configurations are entered under the relevant keys in this portion of the config file.

For now it contains a default config for the `Apache Hosts Export` plugin that comes with the package. Users can update this config to suit their purpose.


## Execution Syntax
The script has 3 primary commands:

- build
- clean
- clean-all


### build
You would normally run the script as follows to build your hosts file:

```
$ hm build
```

By default the module is configured to write to `./hosts.txt`. This is done for 2 reasons:
- so that you can test your output before overriding the system hosts file
- you don't have to run the script with `sudo`

It is possible to have the script automatically override the system hosts file on each build. Under `config.py`, uncomment the line that points to `hosts_file_path`.

```
# output_file_path = 'hosts.txt'
output_file_path = hosts_file_path
```

You WILL have to run this script as `sudo` for it to write directly to the system hosts file. You can do this once you have confidence in the scripts' behavior.

```
$ sudo hm build
```


### clean
The script allows you to remove your configuration from the hosts file by running:

```
$ hm clean
```

This will only clear the current-user's configuration from the hosts file.


### clean-all
As a sysadmin (or as a power-user) if you want to clean up all the configuration added by this module from all users in the hosts file run:

```
$ hm clean-all
```

You will be shown a message to confirm your actions.

```
    THIS WILL CLEAR THE HM HOSTS-CONFIG FOR ALL USERS.
    Are you sure you want to do this? [y/N]
```

Type `y` and `<enter>` to confirm. Any other value aborts the script.


## Checking Versions
_Hosts Manager_ uses [semantic versioning 2.0.0](http://semver.org/spec/v2.0.0.html).

Run the script using the `-v` or `--version` argument.

```
$ hm -v
X.Y.Z
```

```
$ hm --version
X.Y.Z
```

## Uninstall
To uninstall this package first clean-up all the configuration that it has added to the hosts file.

```
$ hm clean
```

This will only clean up the configuration for the current user.

If you wish to uninstall the package for ALL users on the system run `clean-all` instead:

```
$ hm clean-all
```

Once you have successfully replaced the clean hosts file you can delete the package directory and you are done with the uninstall.

## Plugins
The script is extensible via plugins added to the `./plugins/` folder. This is useful to set up automated processes to create host-maps.

One plugin `Apache Hosts Export` is available out-of-the-box to use. To know more about `Apache Hosts Export` and how to configure it for your use, follow the README file provided under the `./plugins/apache_hosts_export/` directory.

To know more about plugins and how to create your own, follow the README file under `./plugins/`.
