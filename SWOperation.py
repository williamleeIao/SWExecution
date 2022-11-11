from abc import ABC,abstractclassmethod
from FIleName import IFileName

class ISWoperation(ABC):
    @abstractclassmethod
    def RunCommand(self,cmd_str:IFileName):
        raise NotImplementedError

