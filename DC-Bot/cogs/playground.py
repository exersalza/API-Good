from etc.config import CUR

CUR.execute("SELECT ID, Text FROM roll_text WHERE Name='API-Goose';")
fetcher = CUR.fetchall()

id_ = [item[0] for item in fetcher]
value = [item[1] for item in fetcher]

CUR.execute(" SELECT roll_txt_val FROM tokens WHERE name='API-Goose';")
counter = CUR.fetchone()

for i in range(counter[0]):
    print(id_[i], value[i])

