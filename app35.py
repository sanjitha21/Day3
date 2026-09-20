# Config list
config = ['Type=ethernet', 'Interface=eth0', 'Onboot=yes', 'bootproto=static']

# Create config dict
config_dict = {}
for item in config:
    key, value = item.split('=', 1)
    config_dict[key.lower()] = value

print(config_dict)

# 1. Dict operation: access a value
print('Interface:', config_dict.get('interface'))

# 2. Dict operation: update a value
config_dict.update({'bootproto': 'dhcp'})
print('Updated bootproto:', config_dict['bootproto'])

# 3. Dict operation: remove a key
config_dict.pop('onboot')
print('After removing onboot:', config_dict)
