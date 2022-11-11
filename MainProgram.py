from SWOperation import ISWoperation
from FIleName import IFileName
from DeCompress import TDR
from FIleNameXML2TDMS import XML2TDMS
import ntpath

#Upper level test code
def main_program_process_flow(tdr : ISWoperation, fileinstances : IFileName):
    fileinstances.input_filename =""
    fileinstances.exe_cmd_filename =""
    tdr.RunCommand(fileinstances)

def process_file_name(filepath:str) ->str:
    file_location, XML_path_name = ntpath.split(filepath)
    XML_path_name = XML_path_name.replace("_COMPRESSED.tdr", ".xml")
    return XML_path_name

if __name__ == "__main__":
    
    file_path = "" 
    tdr = TDR()
    compress_process = XML2TDMS()
    compress_process.input_filename = file_path
    compress_process.output_filename = process_file_name(file_path)
    compress_process.exe_cmd_filename = "some path"
    main_program_process_flow(tdr,compress_process)