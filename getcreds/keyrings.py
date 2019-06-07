import subprocess
import keyring
import logging
import re
import json
import sys
import shlex

LOGGER = logging.getLogger(__name__)

def find_key(keyname):
    try:
        print ( "Now Searching the keyring for credentials")
        ps = subprocess.Popen(('security', 'find-generic-password','-l', keyname), stdout=subprocess.PIPE)
        output = subprocess.check_output(('grep','acct'), stdin=ps.stdout)
        ps.wait()
        output = output.strip()
        output = output.strip('"')
        account = re.search(r'(?<=\=").*', output)
    except Exception as e:
        LOGGER.debug("Unable to find a key as an error occured")
        LOGGER.debug(str(e))
    return account.group(0)

def get_creds(service, keyname):
    try:
        print ( "Now getting the credentials from key " + keyname)
        creds = keyring.get_password(service, keyname)
        creds = json.loads(creds)
    except Exception as e:
        LOGGER.debug("Unable to retrieve credentials for service " + service + " for user " + keyname)
        LOGGER.debug(str(e))
    return creds

def create_creds(profile):
    try:
        print ("Making sure we have a fresh token")
        command = "aws-okta exec " + profile + " -- aws --version"
        ps = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
        while True:
          output = ps.stdout.readline()
          if output == '' and ps.poll() is not None:
            break
          if output:
            if not "UserId" or "Account" or "Arn" in output: 
              print output.strip()
        rc = ps.poll()
    except Exception as e:
        LOGGER.debug("Not able to verify Session Token")
        LOGGER.debug(str(e))
        sys.exit(1)

def get_token(service, token):
    try:
        print ( "Now getting the token from key " + token)
        token = keyring.get_password(service, token)
    except Exception as e:
        LOGGER.debug("Unable to retrieve token for service " + service + " for token name " + token)
        LOGGER.debug(str(e))
    return token