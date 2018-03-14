import controller.exceptions as Exceptions

def bookselected(function):
    def inspect(*args,**kwargs):
        if(args[0].context.current_book is None):
            raise Exceptions.BookNotSelected

        function(*args,**kwargs)
    return  inspect


def chapterselected(function):
    def inspect(*args,**kwargs):
        if(args[0].context.current_chapter is None):
            raise Exceptions.ChapterNotSelected

        function(*args,**kwargs)
    return  inspect

def pageselected(function):
    def inspect(*args,**kwargs):
        if(args[0].context.current_page is None):
            raise Exceptions.PageNotSelected

        function(*args,**kwargs)
    return  inspect

def labelselected(function):
    def inspect(*args,**kwargs):
        if(args[0].context.current_label is None):
            raise Exceptions.LabelNotSelected

        function(*args,**kwargs)
    return  inspect

