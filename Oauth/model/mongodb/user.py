from model.mongodb import Model


class User(Model):
    def upsert_user(self, document):
        self.col.update_one(
            {'id': document['id']},
            {'$set': self.schemize(document)},
            upsert=True
        )
