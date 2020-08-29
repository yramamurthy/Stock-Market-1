from kiteconnect import KiteConnect, KiteTicker

from core.kite.TokenGenerator import TokenGenerator
from core.util.Time import Time


class Kite:
    def __init__(self, db):
        self.db = db
        self.config_data = self.db.get_application_config()
        last_updated = Time.convert_to_time(self.get_last_token_time()).date()

        if not Time.today().date() == last_updated:
            self.update_token()
            self.config_data = self.db.get_application_config()

        self.data_api = KiteConnect(api_key=self.config_data["api"])
        self.data_api.set_access_token(self.config_data["access_token"])
        self.socket_api = KiteTicker(self.config_data["api"], self.config_data["access_token"])

    def get_last_token_time(self):
        return self.config_data["last_updated"]

    def update_token(self):
        access_token = TokenGenerator(self.db).generate_token()
        user_id = self.config_data["user_id"]
        self.db.update_token(user_id, access_token)
