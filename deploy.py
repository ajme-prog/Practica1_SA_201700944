from __future__ import with_statement

import fabric, boto
import boto.ec2, time
from fabric.api import *
from fabric.colors import green, yellow
from boto.ec2.connection import EC2Connection

ACCESS_KEY_ID = "AKIAVKBGLV6KAMCSJ4CS"
SECRET_ACCESS_KEY = "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"

REPOS = [
    ("/path/to/repo", "origin", "master")
]


def _connect():
    return EC2Connection(ACCESS_KEY_ID, SECRET_ACCESS_KEY)

def _getInstances():
    connection = _connect()
    reservations = connection.get_all_instances()
    instances = []

    print ""
    print green("** Getting instances **")

    for reservation in reservations:
        for instance in reservation.instances:
            print "Instance: %s (%s) @ %s" % (instance.id, instance.state, instance.public_dns_name)
            instances.append(instance.public_dns_name)

    return instances
    
@task(alias="d")
def deploy():
    _getInstances()