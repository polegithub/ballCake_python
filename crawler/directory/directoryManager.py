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


        content = 'data/Douban/'

        if type == 1:
             content =  content + 'Book'
        elif type == 2:
            content =   content + 'Movie'
        elif type == 3:
            content =   content + 'Music'
        else:
            content =  content + 'Other'

        if os.path.isdir(content) == False :
             os.mkdir(content)

        return content


