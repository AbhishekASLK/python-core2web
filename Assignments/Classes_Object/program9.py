class Dominoz:
    def location(self):
        print("Narhe")

    @staticmethod
    def rawmaterial():
        print("import raw material")

    @classmethod
    def ownerofbranch(cls):
        print("owner")

narhe = Dominoz()
narhe.location()
narhe.rawmaterial()
narhe.ownerofbranch()
