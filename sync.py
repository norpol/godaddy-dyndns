#!/usr/bin/env python
import json
import logging
import pif
import requests
import socket

logging.basicConfig(
    format='%(asctime)s %(message)s',
    level=logging.ERROR)
log = logging.getLogger()

def should_update(domain, subdomain):
    try:
        domain = "{0}.{1}".format(subdomain, domain)
        log.debug('domain: %s', domain)
        old_ip = socket.gethostbyname(domain)
        log.debug('old_ip: %s', old_ip)

        public_ip = pif.get_public_ip('dyndns.com')
        log.debug('public ip: %s', public_ip)

        if old_ip != public_ip:
            return public_ip
    except:
        log.exception('should_update')
    return None

def update_dns(public_ip, key, secret, domain, subdomain):
    auth = {'Authorization': "sso-key {0}:{1}".format(key, secret)}
    r = requests.put('https://api.godaddy.com/v1/domains/{0}'\
                     '/records/A/{1}'.format(domain, subdomain),
                     headers=auth,
                     json=[{'data': public_ip}])
    log.info(r.status_code)
    if r.status_code != 200:
        log.error(r.json())

def main():
    with open('conf.json') as conf_file:
        conf = json.load(conf_file)
    # to avoid the bad ones more vailable in pif.utils.list_checkers()
    ip = should_update(conf['domain'], conf['subdomain'])
    if ip:
        update_dns(ip, **conf)

if __name__ == '__main__':
    main()
