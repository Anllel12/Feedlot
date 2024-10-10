class Calf:
    def __init__(self, crotal=None, weight=0.0, gender='', nationality=''):
        self._crotal = crotal
        self._weight = weight
        self._gender = gender
        self._nationality = nationality

    # Getters and Setters
    def get_crotal(self):
        return self._crotal

    def set_crotal(self, crotal):
        self._crotal = crotal

    def get_weight(self):
        return self._weight

    def set_weight(self, weight):
        self._weight = weight

    def get_gender(self):
        return self._gender

    def set_gender(self, gender):
        self._gender = gender

    def get_nationality(self):
        return self._nationality

    def set_nationality(self, nationality):
        self._nationality = nationality

    def __repr__(self):
        return f"Calf(crotal={self._crotal}, weight={self._weight}, gender='{self._gender}', nationality='{self._nationality}')"
