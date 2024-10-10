class Guide:
    def __init__(self, num_guide=None, cost=0.0, price_males=0.0, price_females=0.0, date=None,
                 num_male=0, num_female=0, kg_male=0.0, kg_female=0.0, provider=None):
        self._num_guide = num_guide
        self._cost = cost
        self._price_males = price_males
        self._price_females = price_females
        self._date = date
        self._num_male = num_male
        self._num_female = num_female
        self._kg_male = kg_male
        self._kg_female = kg_female
        self._provider = provider

    # Getters and Setters
    def get_num_guide(self):
        return self._num_guide

    def set_num_guide(self, num_guide):
        self._num_guide = num_guide

    def get_cost(self):
        return self._cost

    def set_cost(self, cost):
        self._cost = cost

    def get_price_males(self):
        return self._price_males

    def set_price_males(self, price_males):
        self._price_males = price_males

    def get_price_females(self):
        return self._price_females

    def set_price_females(self, price_females):
        self._price_females = price_females

    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    def get_num_male(self):
        return self._num_male

    def set_num_male(self, num_male):
        self._num_male = num_male

    def get_num_female(self):
        return self._num_female

    def set_num_female(self, num_female):
        self._num_female = num_female

    def get_kg_male(self):
        return self._kg_male

    def set_kg_male(self, kg_male):
        self._kg_male = kg_male

    def get_kg_female(self):
        return self._kg_female

    def set_kg_female(self, kg_female):
        self._kg_female = kg_female

    def get_provider(self):
        return self._provider

    def set_provider(self, provider):
        self._provider = provider

    def __repr__(self):
        return (f"Guide(num_guide={self._num_guide}, cost={self._cost}, price_males={self._price_males}, "
                f"price_females={self._price_females}, date={self._date}, num_male={self._num_male}, "
                f"num_female={self._num_female}, kg_male={self._kg_male}, kg_female={self._kg_female}, "
                f"provider={self._provider})")
