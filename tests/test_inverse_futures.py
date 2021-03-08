from .utils import get_btc_candles, get_btc_and_eth_candles, set_up, single_route_backtest


def test_can_detect_inverse_futures():
    single_route_backtest('TestCanDetectInverseFutures', is_futures_trading=True, is_inverse_futures=True)
