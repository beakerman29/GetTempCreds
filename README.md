# GoOktaBoto

This is a small package designed to help remove the need to constantly create
a module or code to use Okta third party authentication with AWS and your local python packages.

## Requirements
1. aws-okta from https://github.com/segmentio/aws-okta
2. AWS account
3. Okta setup to perform authentication to AWS account

##Installing the module

You can install the module using pypi currently only available in the test repo

```pip3 install -i https://test.pypi.org/simple/ GoOktaBoto ```

## Upgrading the module

```pip3 install --upgrade --no-cache-dir -i https://test.pypi.org/simple/ GoOktaBoto```

## Sample using the module

```
#if you are having problems enable logging
#import logging
#logging.basicConfig()
#LOGGER = logging.getLogger()
#LOGGER.setLevel('DEBUG')
from GoOktaBoto import getcredentials as gc
creds = gc.get_credentials(<yourprofile>)
```

The logging is optional and can be implemented with your code as the module inherits the 
logging level from your main module. For the call you can pass in the profile of your choice. I use the below to enable this
so I can enable it for local credentials when testing my code.

```
import argparse
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--local", help="Run the application using local credentials", action='store_true')
parser.add_argument("--profile", help="What profile to get", default='none')
args = parser.parse_args()
```
using the above you can then test if the parameter local is passed in which case we set it to true and can perform the necessary
lookup and storing of credentials. 