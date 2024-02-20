class Customer:
    def __init__(self, first, last, id, phone, debt, date):
        self._first = first
        self._last = last
        self._id = id
        self._phone = phone
        self._debt = debt
        self._date = date
    
    @property
    def id(self):
        print("getting id")
        return self._id

    @property
    def debt(self):
        return self._debt 
    
    add_debt(self)

