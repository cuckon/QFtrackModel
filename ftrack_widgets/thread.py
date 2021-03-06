from Qt import QtCore


class QueryThread(QtCore.QThread):
    responsed = QtCore.Signal(list)

    def __init__(self, parent=None):
        self._query = None
        super(QueryThread, self).__init__(parent)

    def do(self, query):
        if self.isRunning():
            self.terminate()
        self._query = query
        self.fetchMore()

    def canFetchMore(self):
        return self._query._can_fetch_more()

    def fetchMore(self):
        # self.run()
        self.start()

    def run(self):
        if self.canFetchMore():
            next_offset = self._query._next_offset
            self._query._fetch_more()
            self.responsed.emit(self._query._results[next_offset:])
        else:
            self.responsed.emit([])
#
#
# class ThumbnailThread(QtCore.QThread):
#     def
