from model.mongodb import Model


class GoogleUsers(Model):
    def upsert_user(self, document: dict):
        self.col.update_one(
            {'id': document['id']},
            {'$set': self.schemize(document)},
            upsert=True
        )
