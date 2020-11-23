class Portfolio():
    def __init__(self, account_number:str = None):
        self.account_number = account_number
        self.positions = {}
        self.positions_count = 0
        self.market_value = 0.0
        self.profit_loss = 0.0
        self.risk_tolerance = 0.0

    def add_position(self, symbol:str, asset_type:str, purchase_date:str = None, quantity:int = 0, purchase_price:float = 0.0):
        self.positions[symbol] = {}
        self.positions[symbol]['symbol'] = symbol
        self.positions[symbol]['asset_type'] = asset_type
        self.positions[symbol]['purchase_date'] = purchase_date
        self.positions[symbol]['quantity'] = quantity
        self.positions[symbol]['purchase_price'] = purchase_price

        return self.positions

    def add_positions(self, positions: list[dict]):
        if isinstance(positions, list):
            for position in positions:
                self.add_position(
                    symbol=position['symbol'],
                    asset_type=position['asset_type'],
                    purchase_date=position.get('purchase_date', None),
                    quantity=position.get('quantity', 0),
                    purchase_price=position.get('purchase_price', 0.0)
                )

        else:
            raise TypeError('Input into function must be a list of dictionaries')

        return self.positions

    def remove_position(self, symbol):
        if symbol in self.positions:
            del self.positions[symbol]
            return (True, f'{symbol} was successfully deleted')

        else:
            return (False, f'{symbol} does not exist in the portfolio')

    def total_allocation(self):
        pass

    def risk_exposure(self):
        pass

    def total_market_value(self):
        pass

    def is_stock_in_portfolio(self, symbol):
        if symbol in self.positions:
            return True
        return False

    def is_profitable(self, symbol, current_price):
        purchase_price = self.positions[symbol]['purchase_price']
        if current_price >= purchase_price:
            return True
        return False