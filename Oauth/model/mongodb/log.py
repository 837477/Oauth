from model.mongodb import Model


class Log(Model):
    def insert_log(self, document):
        self.col.insert_one(self.schemize(document))
