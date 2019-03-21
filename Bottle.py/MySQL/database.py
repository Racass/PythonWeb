from abc import ABC, abstractmethod

class DataBase:

    def __init__(self, autoCommit: bool):
        self.autoCommit = autoCommit
        self.myDB = self.getDBConn()
        super().__init__()
    @abstractmethod
    def execModQuery(self, query: str) -> int:
        raise NotImplementedError
    @abstractmethod
    def execReadQuery(self, query: str) -> tuple:
        raise NotImplementedError
    @abstractmethod
    def commit(self):
        raise NotImplementedError
    @abstractmethod
    def getDBConn(self):
        raise NotImplementedError