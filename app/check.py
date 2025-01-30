import MonsterLab.monster_data
print(dir(MonsterLab.monster_data))

from MonsterLab.monster_lab import Monster

random_monster = Monster()

def seed(self, amount: int):
        """
        Seed the database with a specified number of random Monster documents.
        """
        monsters = [Monster().to_dict() for _ in range(amount)]  # Use Monster to create random monsters
        self.collection.insert_many(monsters)