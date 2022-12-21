from abc import ABC, abstractmethod

class CollectedData:

    @abstractmethod
    def retrive_data(self) -> list:
        pass