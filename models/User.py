class User:
    def __init__(self, row):
        self.id = row[0]
        self.full_name = row[1]
        self.photo_url = row[2]

