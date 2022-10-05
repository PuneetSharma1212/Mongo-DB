import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
testdb = client['testdb']
employee1 = testdb['Table1']
employee = [{'name': 'John', 'age': 34, 'department': 'IT'},
            {'name': 'Kris', 'age': 44, 'department': 'Sales'},
            {'name': 'Mike', 'age': 40, 'department': 'Operations'},
            {'name': 'Jordon', 'age': 30, 'department': 'IT'}]
employee1.insert_many(employee)