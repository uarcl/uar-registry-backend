from social_core.backends.oauth import BaseOAuth2

class UARCLOAuth2(BaseOAuth2):
    """UAR registry OAuth authentication backend"""
    name = 'uarcl-oauth'
    AUTHORIZATION_URL = 'https://auth.uar.cl/api/oauth/login/authorize'
    ACCESS_TOKEN_URL = 'https://auth.uar.cl/api/oauth/token'
    USERINFO_URL = 'https://auth.uar.cl/api/oauth/userinfo'
    ACCESS_TOKEN_METHOD = 'POST'
    DEFAULT_SCOPE = ['openid', 'email', 'profile']
    REDIRECT_STATE = False
    STATE_PARAMETER = True
    ID_KEY = 'sub'
    EXTRA_DATA = [
        ('fullname', 'fullname'),
        ('expires_in', 'expires'),
        ('doc_number','doc_number'),
    ]

    def get_user_details(self, response):
        """Return user details from UAR registry account"""
        return {'username': response.get('username'),
                'userid': response.get('sub'),
                'email': response.get('email') or '',
                'fullname': response.get('fullname'),
                'country': response.get('country'),
                'doc_number':response.get('doc_number'),
                'year_of_birth': response.get('year_of_birth')}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        return self.get_json('https://auth.uar.cl/api/oauth/userinfo',headers={'Authorization': 'Bearer {0}'.format(access_token)})

