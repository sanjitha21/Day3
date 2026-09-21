# Config list
config = ['Type=ethernet', 'Interface=eth0', 'Onboot=yes', 'bootproto=static']

config_dict = {}
for item in config:
    key, value = item.split('=', 1)
    config_dict[key.lower()] = value

print(config_dict)
print('Interface:', config_dict.get('interface'))

config_dict.update({'bootproto': 'dhcp'})
print('Updated bootproto:', config_dict['bootproto'])

config_dict.pop('onboot')
print('After removing onboot:', config_dict)
