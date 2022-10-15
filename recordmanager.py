class Record_mgr:
    
    
    def __init__(self,):
        self.currentFile = ''


    def store_record(self, partial_path, fileName, record):
        
        # stop if record is invalid or path is invalid
        if(record['type'] != 'password'):
            return "failure"
        
        # write to path
        self.currentFile = partial_path + fileName
        recordFile = open(r"" + self.currentFile , "w")
        for i in record.keys():
            recordFile.write(record[i] + ' /' + i)

            recordFile.close()

    def get_record(self, partial_path, fileName):
        # stop if path is invalid
        if(False):
            return "failure"
        
        # read file
        self.currentFile = partial_path + fileName
        recordFile = open(r"" + self.currentFile, "r")
        record = []
        record.append(recordFile.readline())
        
        recordFile.close()


    def delete_record(self,):
        pass
    

    def get_current_file(self,):
        pass 