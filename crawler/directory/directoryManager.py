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
        if os.path.isdir(content) == False :
             os.mkdir(content)

        if type == 1:
            return  (content + 'book')
        elif type == 2:
            return  content + 'movie'
        elif type == 3:
            return  content + 'music'
        else:
            return content + 'other'

