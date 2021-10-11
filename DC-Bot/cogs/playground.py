from datetime import datetime
print(type(datetime.utcnow()), type(datetime.now().time('%Y-%m-%d %H:%M:%S.%f')), type(datetime.now()))
