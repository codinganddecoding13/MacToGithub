hosts = open('/etc/hosts')
print(hosts.read(3))
print(hosts.tell())