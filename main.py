import pymongo as pm

def insert_document(collection, data):
    return collection.insert_one(data).inserted_id

def find_document(collection, elements, multiple=False):
    if multiple:
        results = collection.find(elements)
        return [r for r in results]
    else:
        return collection.find_one(elements)

def update_document(collection, query_elements, new_values):
    collection.update_one(query_elements, {'$set': new_values})

def delete_document(collection, query):
    collection.delete_one(query)

"""
familyDB
    family(id_member, name, surname, patronymic, birthdate)
    goal(id_goal, denomination, category)
    transact(id_transaction, id_member, id_organisation, id_goal, summ, date)
    organisation(id_organisation, denomination,  name, surname, patronymic, birthdate)
"""
dest = "C:\Program Files\MongoDB\Server\5.0\bin\mongo.exe"
if __name__ == '__main__':
    client = pm.MongoClient()
    db = client.familyDB
    collectionfamily = db.family
    collectiongoal = db.goal
    collectiontransact = db.transact
    collectionorganisation = db.organisation
    collection_list = [collectionorganisation, collectiontransact, collectiongoal, collectionfamily]
    for coll in collection_list:
        print(find_document(coll, {}))
