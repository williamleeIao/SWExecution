from SWOperation  import ISWoperation
from FIleName import IFileName
import subprocess

class TDR(ISWoperation):

    def RunCommand(self,cmd_str:IFileName):
        print ("at TDR")
        subprocess.run(cmd_str.construct_process_str()) 

tdr = TDR()
tdr.RunCommand()