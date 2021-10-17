from etc.config import CUR

CUR.execute("SELECT ID, Text FROM roll_text WHERE Name='API-Goose'")
fetcher = CUR.fetchall()

ID = [item[0] for item in fetcher]
Value = [item[1] for item in fetcher]

print(option1[1], option2[1])

