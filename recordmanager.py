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


    def get_record(self,):
        pass


    def delete_record(self,):
        pass
    

    def get_current_file(self,):
        pass 