# Plugins
This directory contains all the plugins that can be used with _Hosts Manager_.

Information on configuration and usage for each plugin should be listed under the README file for the plugin itself.

Even if you have a plugin in this directory, it will only be processed if it is listed as an active-plugin under `active_plugins` in `./config.py`.

```
active_plugins = [
    'apache_hosts_export'
]
```

Contents:

- [Installing plugins](#installing-plugins)
  - [A word of caution](#a-word-of-caution)
- [Uninstalling plugins](#uninstalling-plugins)
- [Creating Plugins](#creating-plugins)
  - [Step 1: Start with a name](#step-1-start-with-a-name)
  - [Step 2: Choose the plugin-key](#step-2-choose-the-plugin-key)
  - [Step 3: Create the plugin directory and `__init__.py`](#step-3-create-the-plugin-directory-and-__init__py)
  - [Step 4: Create the main file - `main.py`](#step-4-create-the-main-file-mainpy)
  - [Step 5: `DISPLAY_NAME` and `VERSION`](#step-5-display_name-and-version)
  - [Step 6: The `main` method](#step-6-the-main-method)
  - [Step 7: Activation and configuration](#step-7-activation-and-configuration)
  - [Step 8: Running `hm` and testing our plugin](#step-8-running-hm-and-testing-our-plugin)
  - [Step 9: Returning a hosts-map](#step-9-returning-a-hosts-map)

## Installing plugins
Copy the plugin folder to this directory. List the plugin folder name under `active_plugins` and configure according to the instructions that came with the plugin itself.

```
active_plugins = [
    'apache_hosts_export',
    '<new_plugin_name>'
]
```

It is _very important_ that you retain the folder name of the plugin as dictated by the author.

The next time you run `hm build` it should start working with your new plugin.

### A word of caution!
Any time you install a new plugin make sure it behaves as expected by setting your `output_file_path` to a test file.

_CHECK ANY CODE RUN AS SUDO; IT COULD BE HARMFUL!!!_

## Uninstalling plugins
If you want to temporarily disable a plugin from running, you can just remove it from the `active_plugins` configuration.

If you have a config like this:

```
active_plugins = [
    'apache_hosts_export',
    'my_plugin_name'
]
```

, and you want to disable `my_plugin_name`, you can either comment it out (prefix with `#`) or delete the line entirely.

```
active_plugins = [
    'apache_hosts_export',
    
    # this plugin is now inactive
    #'my_plugin_name'
]
```

If you wish to remove the plugin completely, remove the name from the `active_plugins` config FIRST, and then proceed to delete the plugin folder from within the `./plugins/` directory.

## Creating Plugins
This section will set you up with how to create plugins for _Hosts Manager_.

### Step 1: Start with a name
Since the script is written in Python, all plugins are loaded as a Python module.

Choose a name with the following recommendations:

- Avoid starting the name with numbers `0-9`
- Avoid using dots in the name `.`
- Avoid any invalid file-name characters.
  - Although this is fine for the _display_ name,
    remember that your plugin name is going to be
    used as the folder directory.

These recommendations are only in place to make choosing a plugin-key easier.

For our example we name our plugin `My First Plugin`.

### Step 2: Choose the plugin-key
Use the plugin name you have from step 1 for this step.

Lowercase the name and replace spaces and punctuation with underscores `_` to get a key name.

`My First Plugin` becomes `my_first_plugin`.

This is just a recommendation. Create a key-name that is easily associated with your plugin name.


### Step 3: Create the plugin directory and `__init__.py`
Under `./plugins/` create the plugin directory using the plugin-key you created above.

In our case, the plugin-key is `my_first_plugin`

```
$ cd ./plugins/
$ mkdir my_first_plugin
```

In our case, this will create `./plugins/my_first_plugin/`.

Before we proceed to the next step, we should create a `__init__.py` file.

Assuming you are still in the `./plugins/` folder from the last command:

```
$ cd my_first_plugin
$ touch __init__.py
```

Every plugin is accessed as a python module and hence the `__init__.py` file is necessary (Python devs should already know this).

### Step 4: Create the main file - `main.py`
_Hosts Manager_ is designed to hook into the `main.py` file of plugins to run code.

Create the `main.py` file:

```
$ touch main.py
```

At this point you should have an empty `main.py` file. We still have a few steps before we can start writing code for our plugin.

### Step 5: `DISPLAY_NAME` and `VERSION`
Every plugin _must_ expose the display name and version of the plugin. Whenever the plugin is run, the script _always_ prints these out as the first line before running the rest of the plugin code.

The purpose of these properties is to help users to diagnose any plugin related issues.

Open `main.py` and put these properties in:

```
DISPLAY_NAME = 'My First Plugin'
VERSION = '0.1.0'
```

If you are a veteran python dev, read the rest of this step, otherwise, skip to step 6.

If you are a veteran python dev, your implementation for these properties can go beyond simple strings as long as the value the script gets enumerated in the end is a string.

For example, under the `Apache Host Export` plugin the version is derived from a `Version` class.

```
VERSION = Version.get() # returns the version as a string
```

### Step 6: The `main` method
The script calls the `main` method in your `main.py` file with a `config` argument.

Add the following to your `main.py` file below your `VERSIONS` declaration.

```
def main(config):
    # TODO: remove
    print 'My first plugin works!!'

    # plugin code goes here

    # return hosts-map dictionary object
    return {}
```

We are NOT ready to run our plugin yet. Before we do that, we need to activate the plugin and optionally also add a configuration under `./config.py`.

### Step 7: Activation and configuration
Open `./config.py` and add the plugin to the `active_plugins` list.

```
active_plugins = [
    #'apache_hosts_export',
    'my_first_plugin'
]
```

This activates the plugin to run on the next `hm build` command.

While we are in here, you should ensure the `output_file_path` is configured to a test file so that we can test our plugin.

```
output_file_path = 'hosts.txt'
```

You can optionally add a configuration for the plugin.

```
plugin_config = {
    "apache_hosts_export": { ... },

    "my_first_plugin": {
        "foo": 'abc',
        "bar": [],
        "baz": {}
    }
}
```

We will update the example code to use our configuration.

```
def main(config):
    print "Value of foo = %s" % config['foo']

    # TODO: remove
    print 'My first plugin works!!'

    # plugin code goes here

    # return hosts-map dictionary object
    return {}
```

### Step 8: Running `hm` and testing our plugin
Before running `hm` we should make sure that the output file is a test file. The plugin is NOT supposed to write to `hosts` directly. Instead it returns a `hosts-map` dictionary object. But we will get to that later.

Run `hm build` and you should see the following output

```
$ hm build
TK host manager v0.1.0

Config file loaded

...

Active-plugins:
	my_first_plugin
1 plugin(s) active

Running: 'my_first_plugin'
My First Plugin v0.1.0
Value of foo = abc
My first plugin works!!
Done

Writing hosts file:
	hosts.txt
Done
```

Woohoo! Our plugin works!!

Check the `hosts.txt` file in the project (NOT plugin) directory.

```
...

# tkhm - username - START


# default - START

127.0.0.1		testdomain.local

# default - END


# tkhm - username - END
```

We don't see our plugin output here yet. This is fine because to see the output here we need to return a hosts-map from the `main` method. We will do this in step 9.

#### Absent and empty configurations
In the event that a configuration is absent (or empty) from `./config.py` for the plugin, which can happen either because the user forgot to configure OR the plugin doesn't require a configuration, the script passes in an empty dictionary to `config`.

So the `config` in `def main(config)` will be `{}`. It is recommended that you throw an exception in your plugin code in case an important configuration directive is missing.

### Step 9: Returning a hosts-map
Plugins are NOT supposed to write to the hosts file directly. Instead they are supposed to written a dictionary object with the hosts-map.

In your plugins `main.py`, modify the `return` statement as follows:

```
    # return hosts-map dictionary object
    return {
        "127.0.0.1": [
            'testdomain1',
            'testdomain2.local'
        ],

        "192.168.0.99": [
            'testdomain3',
            'www.testdomain.com'
        ]
    }
```

Save and run `hm build` again, and now look at `hosts.txt`.

```
...
# tkhm - username - START


# default - START

127.0.0.1		testdomain.local

# default - END



# my_first_plugin - START

192.168.0.99	testdomain3 www.testdomain.com
127.0.0.1		testdomain1 testdomain2.local

# my_first_plugin - END


# tkhm - username - END
```

Wheeeee!! You've got your first plugin up and running.

Now use your python chops to automate your process under the main method. Whatever is possible under Python goes.

If you need to see an example working plugin in action you can always go see the code under `Apache Hosts Export`.
