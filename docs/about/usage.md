---
id: usage
title: Usage
---

Once you have installed nymea successfully you can start the nymead daemon. There are two ways to start nymead:

* Starting nymea as daemon (service)
* Starting nymea as application (terminal application)

In order to get help, just type in the terminal _nymead -h_:

```bash
$ nymead -h

Usage: nymead [options]

nymea is an open source IoT (Internet of Things) server, 
which allows to control a lot of different devices from many different 
manufacturers. With the powerful rule engine you are able to connect any 
device available in the system and create individual scenes and behaviors 
for your environment.

nymead 0.9.0 © 2014-2019 nymea GmbH
Released under the GNU GENERAL PUBLIC LICENSE Version 2.

API version: 1.3

Options:
  -h, --help                                Displays this help.
  -v, --version                             Displays version information.
  -n, --no-daemon                           Run nymead in the foreground, not
                                            as daemon.
  -p, --print-all                           Enables all debug categories.
                                            Single debug categories can be
                                            disabled again with -d parameter.
  -l, --log <logfile>                       Specify a log file to write to, if
                                            this option is not specified, logs
                                            will be printed to the standard
                                            output.
  --session                                 If specified, all D-Bus interfaces
                                            will be bound to the session bus
                                            instead of the system bus.
  -d, --debug-category <[No]DebugCategory>  ...
```

Also a manual page is available:

```bash
$ man nymead
```

By default, nymead will start as a daemon. If you want to start nymead as an application, you can pass the parameter -n and it will start in the foreground.

If you want to see a special debug category, you can pass that category to the parameter. You can find all available categories in the help message (nymead -h):

> **Example:** Start nymea in the foreground and enable the JSON-RPC and Hardware and disable the DeviceManager debug messages:

```bash
$ nymead -n -d JsonRpc -d Hardware -d NoDeviceManager
```

## Systemd service

The nymea package also provides a systemd service, which allows you to start, stop, restart and get the status of the nymea-daemon.

### Start the service:

```bash
$ sudo systemctl start nymead
```

### Stop the service:

```bash
$ sudo systemctl stop nymead
```

### Restart the service:

```bash
$ sudo systemctl restart nymead
```

### Get the status of the service:

```bash
$ sudo systemctl status nymead
```
### Autostart nymea

If you want to auto start nymead on boot, you can enable the service by calling the following command:

```bash
$ sudo systemctl enable nymead
```
Created symlink from _/etc/systemd/system/multi-user.target.wants/nymead.service_ to _/etc/systemd/system/nymead.service_

### Disable autostart nymea

If you want to disable auto starting nymead on boot, use the following command:

```bash
$ sudo systemctl disable nymead
```
Removed symlink _/etc/systemd/system/multi-user.target.wants/nymead.service_

### Debug output

If you have nymead running in the background (as daemon and started with systemd) you can see the live debug out by monitoring the log file. You can do that with the following command:

```bash
$ journalctl -f -u nymead
```

## Start as application

```bash
$ nymead -n -p
```

### Add a custom plugins path

If you want nymead to load plugins from a custom directory, like a build directory of a nymea plugin, you can add the path to the environment variable by passing the following command:

```bash
$ sudo NYMEA_PLUGINS_PATH=/path/to/plugin nymead -n -p
```
As an alternative, you can also export the environment variable NYMEA_PLUGINS_PATH for the current bash session like this:

```bash
$ export NYMEA_PLUGINS_PATH=/path/to/plugin
$ nymead -n -p
```
You can also export mulitiple paths by splitting them with the : character:

```bash
$ export NYMEA_PLUGINS_PATH=/path/to/plugin:/path/to/other/plugin
$ nymead -n -p
```
You can check in the debug output if the path will be used to load plugins and which plugins where loaded from that directories. 
