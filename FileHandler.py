import os

class FileHandler:
    def create_dir(self, path):
        #TODO: check if path is valid
        #TODO: check if it folder or file
        if os.path.exists(path):
            pass
            #TODO: enter this path
        else:
            if os.path.isdir(path):
                pass
                #TODO: create new dir...where?
            if os.path.isfile(path):
                pass
                # TODO: create new file... where?



        os.mkdir(path)