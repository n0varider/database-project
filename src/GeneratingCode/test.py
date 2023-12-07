
import subprocess
import json


entities = {'entities_to_make': 200}
bonds = {'bonds_to_make': 1_000}
buy = {'buys_to_make': 250}


data = {1: entities, 2: bonds, 3: buy}



with open('data.json', 'w') as file:
    json.dump(data, file)

subprocess.run(["python", "MakeEntities.py"])
subprocess.run(["python", "MakeEmploye.py"])
subprocess.run(["python", "MakeAccounts.py"])
subprocess.run(["python", "MakeSeller.py"])
subprocess.run(["python", "MakeBuyer.py"])
subprocess.run(["python", "MakeBuy.py"])
subprocess.run(["python", "MakeBond.py"])
subprocess.run(["python", "MakeTransaction.py"])







