from GoOktaBoto import keyrings
import sys


def get_credentials(profile):
    try:
        # Make sure we have a valid profile and current token
        keyrings.create_credentials(profile)
        account = keyrings.find_key("aws session for " + profile)
        credentials = keyrings.get_credentials("aws-okta-login", account)
    except Exception as e:
        print("We could not get the credentials you asked for because of an error")
        print("Error was: {}".format(e))
        sys.exit(1)
    return credentials






