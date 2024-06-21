import pymongo
print(pymongo.__version__)

client = pymongo.MongoClient("mongodb://localhost:27017/")

mydb=client['Employee']  #will create a db or use an existing database

imformation = mydb.employeeInformation

record = {
    "firstname":"James",
    "department":"Analytics",
    "age":25
}

imformation.insert_one(record)