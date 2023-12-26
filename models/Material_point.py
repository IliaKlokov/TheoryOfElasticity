class Material_point:
    rx1 = None
    rx2 = None
    rx3 = None
    def __init__(self, rx1, rx2, rx3):
        self.rx1 = rx1
        self.rx2 = rx2
        self.rx3 = rx3
#у нас изменения только в осях х1 и х2, нужно ли тогда вообще х3?