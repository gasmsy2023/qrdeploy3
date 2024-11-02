import os
import sys

# Add your site packages directory to path
SITE_PACKAGES_PATH = '/home/gahmuti/virtualenv/certificate.virtualmindshub.com/3.10/lib/python3.10/site-packages'
if SITE_PACKAGES_PATH not in sys.path:
    sys.path.append(SITE_PACKAGES_PATH)

# Add project directory to path
PROJECT_PATH = '/home/gahmuti/certificate.virtualmindshub.com'
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)

from qrcertificate.wsgi import application
