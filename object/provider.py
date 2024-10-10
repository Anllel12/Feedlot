class Provider:
    def __init__(self, id=None, name='', cif=''):
        self._id = id
        self._name = name
        self._cif = cif

    # Getters and Setters
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_cif(self):
        return self._cif

    def set_cif(self, cif):
        self._cif = cif

    def __repr__(self):
        return f"Provider(id={self._id}, name='{self._name}', cif='{self._cif}')"
