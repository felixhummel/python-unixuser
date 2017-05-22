#!/usr/bin/env python
# encoding: utf-8


class NamedThing(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name


class User(NamedThing):
    def __matmul__(self, host):
        assert isinstance(host, Host)
        return UnixUser(self, host)


class Host(NamedThing):
    def __init__(self, name):
        self.name = name


class UnixUser(NamedThing):
    def __init__(self, user, host):
        self.user = user
        self.host = host

    def __str__(self):
        return str(self.user) + '@' + str(self.host)


def test():
    user = User('alice')
    host = Host('example.com')
    unixuser = user @ host
    print(unixuser)
    assert str(unixuser) == 'alice@example.com', str(unixuser)


if __name__ == '__main__':
    test()
