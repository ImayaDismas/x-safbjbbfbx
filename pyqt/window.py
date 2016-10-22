#!/usr/bin/env python
import sys
import configparser

config = configparser.RawConfigParser()

# Please note that using RawConfigParser's set functions, you can assign
# non-string values to keys internally, but will receive an error when
# attempting to write to a file or when you get it in non-raw mode. Setting
# values using the mapping protocol or ConfigParser's set() does not allow
# such assignments to take place.
config.add_section('Settings')
config.set('Settings', 'an_int', '150')
config.set('Settings', 'a_bool', 'true/false')
config.set('Settings', 'a_float', '3.1415')
config.set('Settings', 'baz', 'fun')
config.set('Settings', 'bar', 'Python')
config.set('Settings', 'foo', '%(bar)s is %(baz)s!')

# Writing our configuration file to 'settings.config'
with open('settings.config', 'w') as configfile:
    config.write(configfile)
