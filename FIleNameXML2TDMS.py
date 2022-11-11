from FIleName import IFileName

class XML2TDMS(IFileName):
    __input_filename:str =""
    __output_filename:str ="" 
   
    @property
    def input_filename(self):
     return self.__input_filename
    
    @input_filename.setter
    def input_filename(self,in_file):
      self.__input_filename = in_file

    @property
    def output_filename(self):
     return self.__output_filename
    
    @input_filename.setter
    def output_filename(self,out_file):
     self.__output_filename = out_file
     
     
    @property
    def exe_cmd_filename(self):
     return self.__execution_filename
    
    @exe_cmd_filename.setter
    def exe_cmd_filename(self,cmd_path):
     self.__execution_filename = cmd_path
     
    def construct_process_str(self) -> str:
        return  "{} -c \"{}\" \"{}\" ".format(self.ExecutionFilePath, self.__input_filename,self.__output_filename)