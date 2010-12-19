from qtvis.ystockquote import get_historical_prices

class InvalidQuoteID(KeyError):
    """Unable to fetch prices from yahoo/google"""



class Root(object):
    __name__ = None
    __parent__ = None

    def __init__(self):
        self._cache = dict()

    def __getitem__(self, key):
        if key not in self._cache:
            quote = Quote(key)
            try:
                quote.fetch_historic()
            except InvalidQuoteID:
                raise
            self._cache[key] = quote
        return self._cache[key]

    def get(self, key, default=None):
        try:
            item = self.__getitem__(key)
        except KeyError:
            item = default
        return item

    def __iter__(self):
        session= DBSession()
        query = session.query(MyModel)
        return iter(query)

root = Root()

def root_factory(request):
    return root

class Quote(object):

    def __init__(self, ticker_id):
        self.ticker_id = ticker_id.split(',')
        self.hist = {}

    def fetch_historic(self):
        for id in self.ticker_id:
            self.hist[id] = get_historical_prices(id, "20100901", "20101001")
        if not self.hist:
            raise InvalidQuoteID("Couldn't get prices for %s" % self.ticker_id)
