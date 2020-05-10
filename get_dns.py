# -*- coding: utf-8 -*-


class DNSParser():

    def __init__(self, domain):
        '''Initializing'''
        self.domain = domain


if __name__ == '__main__':

    parser = DNSParser('github.com')
    print(parser.domain)
