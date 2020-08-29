import requests

from core.exception.KiteError import KiteLoginError, KiteTwoFAError


class TokenGenerator:

    def __init__(self, db):
        self.db = db
        config_data = self.db.get_application_config()
        self._user_id = config_data["user_id"]
        self._password = config_data["password"]
        self._two_fa = config_data["two_fa"]
        self._api = config_data["api"]

        self._login_url = "https://api-mobile.kite.trade/trusted/kiteandroid/user/" + self._user_id + "/login?"
        self._two_fa_url = "https://api-mobile.kite.trade/trusted/kiteandroid/user/" + self._user_id + "/twofa?"
        self.header = {
            'X-Kite-version': '3',
            'X-Kite-mobile-version': '3.1',
            'X-Kite-UserID': self._user_id,
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.4; Motorola Moto X Build/KTU84P)',
            'Host': 'api-mobile.kite.trade',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'Content-Length': '152',
        }

    def _auth_login(self):
        payload = {
            'password': self._password,
            'user_id': self._user_id,
        }
        data = requests.post(self._login_url, data=payload, headers=self.header).json()
        if not data["status"] == 'error':
            return data
        else:
            raise KiteLoginError()

    def _auth_two_fa(self, request_id):
        payload = {
            "user_id": self._user_id,
            "twofa_value": self._two_fa,
            "request_id": request_id,
        }
        data = requests.post(self._two_fa_url, data=payload, headers=self.header).json()
        if not data["status"] == 'error':
            return data
        else:
            raise KiteTwoFAError()

    def generate_token(self):
        login_data = self._auth_login()
        request_id = login_data["data"]["request_id"]
        user_data = self._auth_two_fa(request_id)
        access_token = user_data["data"]["access_token"]
        return access_token
