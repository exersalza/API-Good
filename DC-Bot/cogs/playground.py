from etc.config import CUR, db

CUR.execute("INSERT INTO users (BotName, UserID, ServerID, Bans, Warnings) VALUES (123, 123, 1232, 1, 3)")
db.commit()
