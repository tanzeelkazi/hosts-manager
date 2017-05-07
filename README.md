# Host Manager
This module is aimed at simplifying management of the system `hosts` file for developers like myself. Although it is simple to edit `hosts` files on machines to test our projects, managing them however, across machines or even over time is a drudging task.

This project was done with the aim of managing the hosts file with relatively simple configs and without the need to install a lot of dependencies.

The script is also extensible via plugins to automate custom workflows. One plugin, `Apache Hosts Export`, which I needed for myself, I have made available out-of-the-box with this package. It searches for `ServerName` directives in the given list of apache config files and maps them to `127.0.0.1` (localhost) automatically.

The script maintains configurations on a per-user basis. So 2-or-more users can easily use this script without blowing away each other's configuration on the same machine.

It is possible to clear out everyone's config on the machine with the `clean-all` command but the script asks to confirm your actions before proceeding. It is assumed anyone with `sudo` rights is responsible enough to take the best actions for the system.

Under NO circumstances is this script designed to delete entries in the hosts file except what it itself has put in. So existing entries in the hosts files remain untouched

# Installation
Simply clone (or download) the git repository to a directory of your choice.

You can symlink the `hm` executable to `/usr/local/bin` if you wish to run it from any directory. The script is agnostic to where it is run from (it switches to the script directory when running statements).

It is recommended that you check the package configuration before first-run.

# Configuration

The module configuration is under `./config.py`. It has comments to make it as self-explanatory as possible. Note that by default the build generates a `./hosts.txt` file with the intended output instead of overriding the system's `hosts` file. This is done to give you time to check the script's output before going rambo on system files. See the `build` section for details on how to change this behavior.

Manual host mapping configuration is under `./hosts_maps/`. The script consumes any file ending in `_conf.py` as a configuration file. See `./hosts_maps/00-default_conf.py` to start adding your hosts.

# Execution Syntax

The script has 3 primary commands:
- build
- clean
- clean-all

## build
You would normally run the script as follows to build your hosts file:
```
./hm build
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
sudo ./hm build
```

## clean
The script allows you to remove your configuration from the hosts file by running:
```
./hm clean
```

This will only clear the current-user's configuration from the hosts file.


## clean-all
As a sysadmin (or as a power-user) if you want to clean up all the configuration added by this module from all users in the hosts file run:
```
./hm clean-all
```

You will be shown a message to confirm your actions.

```
    THIS WILL CLEAR THE HM HOSTS-CONFIG FOR ALL USERS.
    Are you sure you want to do this? [y/N]
```

Type `y` and `<enter>` to confirm.


# Uninstall
To uninstall this package first clean-up all the configuration that it has added to the hosts file.
```
./hm clean
```

This will only clean up the configuration for the current user.

If you wish to uninstall the package for ALL users on the system run `clean-all` instead:
```
./hm clean-all
```

Once you have successfully replaced the clean hosts file you can delete the package directory and you are done with the uninstall.

# Plugins
TODO: Need to add documentation on how to add new plugins
