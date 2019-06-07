import subprocess
import keyring
import logging
import re
import json
import sys

LOGGER = logging.getLogger(__name__)


def find_key(key_name):
    try:
        print("Now Searching the keyring for credentials")
        ps = subprocess.run(['security', 'find-generic-password','-l', key_name], capture_output=True, text=True
    , check=True).stdout
        for line in ps.splitlines():
            if 'acct' in line:
                account = line.strip()
                account = account.strip('"')
                account_final = re.search(r'(?<=\=").*', account)
    except Exception as e:
        LOGGER.debug("Unable to find a key as an error occurred")
        LOGGER.debug(str(e))
    return account_final.group(0)


def get_credentials(service, key_name):
    try:
        print("Now getting the credentials from key " + key_name)
        credentials = keyring.get_password(service, key_name)
        credentials = json.loads(credentials)
    except Exception as e:
        LOGGER.debug("Unable to retrieve credentials for service " + service + " for user " + key_name)
        LOGGER.debug(str(e))
    return credentials


def create_credentials(profile):
    try:
        print("Making sure we have a fresh token")
        subprocess.run(['aws-okta', 'exec', profile, '--', 'aws', '--version'], stdout=subprocess.PIPE, check=True)
        print("Fresh session created for " + profile)
    except Exception as e:
        LOGGER.debug("Not able to verify Session Token")
        LOGGER.debug(str(e))
        sys.exit(1)


def get_token(service, token):
    try:
        print("Now getting the token from key " + token)
        token = keyring.get_password(service, token)
    except Exception as e:
        LOGGER.debug("Unable to retrieve token for service " + service + " for token name " + token)
        LOGGER.debug(str(e))
    return token
