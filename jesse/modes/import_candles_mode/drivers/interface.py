from abc import ABC, abstractmethod


class CandleExchange(ABC):
    def __init__(self, name: str, endpoint: str, count: int, sleep_time: float, backup_exchange):
        self.name = name
        self.endpoint = endpoint
        self.count = count
        self.sleep_time = sleep_time
        self._backup_exchange_class = backup_exchange
        self._backup_exchange = None

    @property
    def backup_exchange(self):
        if self._backup_exchange_class is None:
            return None

        if self._backup_exchange is None:
            self._backup_exchange = self._backup_exchange_class()

        return self._backup_exchange

    @abstractmethod
    def fetch(self, symbol: str, start_timestamp: int):
        pass

    @abstractmethod
    def get_starting_time(self, symbol: str) -> int:
        pass
