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
     
    def construct_process_str(self) -> str:
        return  "{} -c \"{}\" \"{}\" ".format(self.ExecutionFilePath, self.__input_filename,self.__output_filename)