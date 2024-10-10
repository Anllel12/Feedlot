class Belong:
    def __init__(self, num_guide=None, num_crotal=None):
        self._num_guide = num_guide
        self._num_crotal = num_crotal

    # Getters and Setters
    def get_num_guide(self):
        return self._num_guide

    def set_num_guide(self, num_guide):
        self._num_guide = num_guide

    def get_num_crotal(self):
        return self._num_crotal

    def set_num_crotal(self, num_crotal):
        self._num_crotal = num_crotal

    def __repr__(self):
        return f"Belong(num_guide={self._num_guide}, num_crotal={self._num_crotal})"
