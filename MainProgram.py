from SW_Execution.SWOperation import ISWoperation
from SW_Execution.FIleName import IFileName
from SW_Execution.DeCompress import TDR
from SW_Execution.FIleNameXML2TDMS import XML2TDMS
import ntpath

#Upper level test code
def main_program_process_flow(tdr : ISWoperation, fileinstances : IFileName):
    tdr.RunCommand(fileinstances)

def process_file_name(filepath:str) ->str:
    file_location, XML_path_name = ntpath.split(filepath)
    XML_path_name = XML_path_name.replace("_COMPRESSED.tdr", ".xml")
    return XML_path_name

def filehandler(filepath:str, exe_cmd:str) ->IFileName:
    """_summary_
       This function is use for assign the file name into the variable that use in tdr 

    Args:
        filepath (str): _description_
        exe_cmd (str): _description_

    Returns:
        IFileName: IFileName use in the SWOperation program
    """    
    compress_process = XML2TDMS()
    compress_process.input_filename = filepath
    compress_process.output_filename = process_file_name(filepath)
    compress_process.exe_cmd_filename = exe_cmd
    return compress_process

if __name__ == "__main__":  
    file_path = r"C:\Users\willlee\Desktop\MICR9902102PEN_134435C-01L_2332_11-2-2022_4-13-26_8876_COMPRESSED.tdr" 
    tdr = TDR()
    compress_process = filehandler(file_path,"some_cmd")
    main_program_process_flow(tdr,compress_process)