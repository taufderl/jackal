#!/usr/bin/env python3
import sys

from elasticsearch import ConnectionError, TransportError
from elasticsearch_dsl.connections import connections
from jackal.core import HostSearch, RangeSearch, ServiceSearch, UserSearch, config
from jackal.utils import print_error, print_notification
from jackal.documents import Host, Range, Service, User


def main():
    services = ServiceSearch()
    hosts = HostSearch()
    ranges = RangeSearch()
    users = UserSearch()
    try:
        print_notification("Connected to: {} [{}]".format(connections.get_connection().info()['cluster_name'], config.get('jackal', 'host')))
    except (ConnectionError, TransportError):
        print_error("Cannot connect to the elasticsearch instance")
        sys.exit(1)

    print_notification("Index: {}".format(config.get('jackal', 'index')))
    host_count = hosts.count()
    if not host_count is None:
        print_notification("Number of hosts defined: {}".format(hosts.count()))
        print_notification("Number of ranges defined: {}".format(ranges.count()))
        print_notification("Number of services defined: {}".format(services.count()))
        print_notification("Number of users defined: {}".format(users.count()))



if __name__ == '__main__':
    main()
