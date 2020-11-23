import pandas as pd

from td.client import TDClient
from td.utils import TDUtilities

from datetime import datetime
from datetime import time
from datetime import timezone

milliseconds_since_epoch = TDUtilities().milliseconds_since_epoch


class PyRobot():
    def __init__(self, client_id:str , redirect_uri: str, credentials_path: str = None, trading_account: str = None):
        self.client_id = client_id
        self.redirect_uri = redirect_uri
        self.credentials_path = credentials_path
        self.trading_account = trading_account
        self.session = self._create_session()
        self.trades = {}
        self.historical_prices = {}
        self.stock_frame = None

    def _create_session(self):
        td_client = TDClient(
            client_id=self.client_id,
            redirect_uri=self.redirect_uri,
            credentials_path=self.credentials_path
        )
        td_client.login()

        return td_client


    @property
    def is_pre_market_open(self):
        # TODO: take into account holidays, weekends, and days that stock market is not open in general
        pre_market_start_time = datetime.now().replace(hour=12, minute=00, second=00, tzinfo=timezone.utc).timestamp()
        actual_market_start_time = datetime.now().replace(hour=13, minute=30, second=00, tzinfo=timezone.utc).timestamp()
        current_time = datetime.now().replace(tzinfo=timezone.utc).timestamp()

        if actual_market_start_time >= current_time >= pre_market_start_time:
            return True #we are in pre_market
        return False

    @property
    def is_regular_market_open(self):
        # TODO: take into account holidays, weekends, and days that stock market is not open in general
        actual_market_start_time = datetime.now().replace(hour=13, minute=30, second=00, tzinfo=timezone.utc).timestamp()
        actual_market_end_time = datetime.now().replace(hour=20, minute=30, second=00, tzinfo=timezone.utc).timestamp()
        current_time = datetime.now().replace(tzinfo=timezone.utc).timestamp()

        if actual_market_end_time>=current_time>=actual_market_start_time:
            return True
        return False

    @property
    def is_post_market_open(self):
        #TODO: take into account holidays, weekends, and days that stock market is not open in general
        post_market_end_time = datetime.now().replace(hour=22, minute=30, second=00, tzinfo=timezone.utc).timestamp()
        actual_market_end_time = datetime.now().replace(hour=20, minute=00, second=00, tzinfo=timezone.utc).timestamp()
        current_time = datetime.now().replace(tzinfo=timezone.utc).timestamp()

        if post_market_end_time >= current_time >= actual_market_end_time:
            return True  # we are in post_market
        return False

    def create_portfolio(self):
        pass

    def create_trade(self):
        pass

    def get_current_quotes(self):
        pass

    def get_historical_prices(self):
        pass

    def create_stock_frame(self):
        pass
