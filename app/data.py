'''My dependencies and libraries'''
from os import getenv
from certifi import where
from dotenv import load_dotenv
from pandas import DataFrame
from pymongo import MongoClient
from MonsterLab.monster_lab import Monster  

class Database:
    '''Here I defined the database class'''
    def __init__(self, collection: str):
        """
        I initialized the Database
        """
        load_dotenv()
        self.database = MongoClient(getenv("DB_URL"), tlsCAFile=where())["MonsterDatabase"]
        self.collection = self.database[collection]

    def seed(self, amount: int):
        """
        I seed the database with random Monster documents.
        """
        monsters = [Monster().to_dict() for _ in range(amount)]  
        try:
            self.collection.insert_many(monsters)
        except Exception as e:
            print(f"Error seeding database: {e}")


    def reset(self):
        """
        Delete all documents.
        """
        self.collection.delete_many({})

    def count(self) -> int:
        """
        Return the number of documents in  collection.
        """
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        """
        Convert the collection documents to a Pandas DataFrame.
        """
        documents = list(self.collection.find({}, {"_id": False}))  
        return DataFrame(documents)

    def html_table(self) -> str:
        """
        Here I convert the DataFrame to an HTML table.
        """
        df = self.dataframe()
        return df.to_html() if not df.empty else None
