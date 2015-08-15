__author__ = 'chengpoleness'

import os

class contentClass:

    def __init__(self):
        print ('conent-init')
        pass

    def getContentForRoot(self):
        pass

    def getContentForDouBan(self,type):

        # BOOK : 1
        # MOVIE: 2
        # MUSIC :3


        content = 'data/douban/'

        if type == 1:
             directory =  content + 'Book'
             content = directory + '/Book'
        elif type == 2:
            directory =   content + 'Movie'
            content = directory + '/Movie'
        elif type == 3:
            directory =   content + 'Music'
            content = directory + '/Music'
        else:
            directory =  content + 'Other'
            content = directory + '/Other'

        print('directory:',directory,'content:',content)
        if os.path.isdir(directory) == False :
             os.makedirs(str(directory))

        return content


