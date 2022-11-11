from abc import ABC,abstractclassmethod
from SW_Execution.FIleName import IFileName

class ISWoperation(ABC):
    @abstractclassmethod
    def RunCommand(self,cmd_str:IFileName):
        raise NotImplementedError

