paart
=====

Requires libsasl2-dev and libldap2-dev for AD integration


Sample settings_local.py for AD integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import ldap, logging
from django_auth_ldap.config import LDAPGroupType, LDAPSearch, ActiveDirectoryGroupType

logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

# makes sure this works in Active Directory
ldap.set_option(ldap.OPT_REFERRALS, 0)

AUTH_LDAP_SERVER_URI = "ldap://10.42.6.107:389"
AUTH_LDAP_BIND_DN = 'cn=lean,ou=016,ou=Hosting,dc=Elaf-HA,dc=local'
AUTH_LDAP_BIND_PASSWORD = 'xxxxxxx'
AUTH_LDAP_USER_SEARCH = LDAPSearch('ou=016,ou=Hosting,dc=Elaf-HA,dc=local', ldap.SCOPE_SUBTREE, '(sAMAccountName=%(user)s)')

AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=Hosting,dc=Elaf-HA,dc=local", ldap.SCOPE_SUBTREE, "(objectClass=group)")
AUTH_LDAP_GROUP_TYPE = ActiveDirectoryGroupType()

AUTH_LDAP_MIRROR_GROUPS = True
AUTH_LDAP_GLOBAL_OPTIONS = {
    ldap.OPT_X_TLS_REQUIRE_CERT: False,
    ldap.OPT_REFERRALS: False,
}

# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    'email': 'userPrincipalName'
}

# This is the default, but I like to be explicit.
AUTH_LDAP_ALWAYS_UPDATE_USER = True

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)
