#!/usr/bin/python
import pyrax
import time

pyrax.set_credential_file(".creds")
cs = pyrax.cloudservers

def build(name,num,flavor,image):
    flavor = [flav for flav in cs.flavors.list() if flav.ram == flavor][0]
    image = [img for img in cs.images.list() if image in img.name][0]
    n = 1
    servers = []
    while n <= num:
        server_name = name + str(n)
        server = cs.servers.create(server_name,image.id,flavor.id)
        servers.append(server)
        n += 1
    time.sleep(60)
    for server in servers:
        server.get()
        print "Name: ", server.name
        print "Status: ", server.status
        print "Password: ", server.adminPass
        print "Networks: ", server.networks["public"]

build("test",3,512,"CentOS 6.3")
