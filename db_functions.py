import pymongo

def db_connection(db):
    myclient = pymongo.MongoClient("mongodb://quiz:quizadmin@18.231.78.22:27017/quiz")
    mydb = myclient["quiz"]
    mycol = mydb[db]
    return mycol
