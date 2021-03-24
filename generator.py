
"""
Winter 2021
COMP 216-001
Lab 08 - Data Generator

Team members:

1. Vincent Tse - 301050515
2. Santiago Yepes Carrera - 301082274
3. Erwin Joshua Manuel - 301107750
4. Hoi Fong Ho - 301084469
5. Kenneth Austin - 301040904
"""


from random import randint
import matplotlib.pyplot as plt


class Stock:
    """A Class that generates a stock price"""

    # public static variable (enum)
    NEUTRAL = 0
    BULLISH = 1
    BEARISH = 2

    # private static variable
    _DELTA = { NEUTRAL: (-5, 5), BULLISH: (-5, 8), BEARISH: (-8, 5) }

    def __init__(self, start: float, trend: int = 2, volatility: float = 0.0) -> None:
        """Initialize with the given value

        start: the start price of the stock.
        trend: the trend of the stock in the current market. (NEUTRAL, BULLISH, BEARISH)
        volatility: how volatile the stock price is. (0.25 means 25%, 1.2 means 120%)

        Precondition:
            start >= 0.0
            trend in range(3)   # either NEUTRAL, BULLISH, BEARISH
            volatility >= 0
        """

        self._trend = trend
        self._volatility = 1 + volatility

        # start = 125 => scale = 1000
        # start = 800 => scale = 2000
        # TODO 
        self._scale = int(f'1{"0" * len(str(start))}')


        self._base = start / self._scale        # the base value, add or subtract from this
        self._delta = 0.0005                    # the change to add or subtract from the above
        self._cycle = 10                        # this is the length of a cycle. 

    def _generate_normalized(self) -> float:
        """Return a normalized value in the range of 0 - 1
        """

        if self._base <= 0:
            self._base = 0
            return self._base
        
        # stock price too high, need a small pull back
        if self._base >= 0.8:
            self._trend = Stock.NEUTRAL
            
        self._cycle -= 1
        if self._cycle == 0: # end of cycle
            self._cycle = int(randint(5, 12)) # generate new cycle

            self._delta = (randint(Stock._DELTA[self._trend][0], 
                                   Stock._DELTA[self._trend][1]) / 10_000) * self._volatility
        
        self._base += self._delta

        return self._base


    @property
    def price(self) -> float:
        return self._generate_normalized() * self._scale



if __name__ == '__main__':
    # aapl = Stock(125, trend=Stock.BEARISH)
    # y = [aapl.price for x in range(1000)]
    # plt.plot(y, 'b')
    # plt.show()

    tsla = Stock(800, trend=Stock.BEARISH, volatility=1)
    y = [tsla.price for x in range(500)]
    plt.plot(y, 'r')
    plt.title('Stock - TESLA')
    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.show()

    aapl = Stock(125, trend=Stock.NEUTRAL, volatility=0.5)
    y = [aapl.price for x in range(500)]
    plt.plot(y, 'b')
    plt.title('Stock - APPLE')
    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.show()

    gme = Stock(200, trend=Stock.BULLISH, volatility=2.5)   # 250%
    y = [gme.price for x in range(500)]
    plt.plot(y, 'g')
    plt.title('Stock - GAMES STOP')
    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.show()
