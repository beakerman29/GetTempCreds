from getcreds import keyrings
import argparse
import sys

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--profile", help="The profile you would like to get temporary okta creds for", type=str, default="test-view")
args = parser.parse_args()


def get_credentials():
    try:
        #Make sure we have a valid profile and current token
        keyrings.create_creds(args.profile)
        account = keyrings.find_key("aws session for " + args.profile)
        credentials = keyrings.get_creds("aws-okta-login", account)
    except Exception as e:
        print("We could not get the credentials you asked for because of an error")
        print("Error was: {}".format(e))
        sys.exit(1)
    return credentials






