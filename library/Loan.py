class Loan:
    def __init__(self, book, borrower, due_date, loan_date, return_date=None, status=True, cod_loan=None):
        self.book = book
        self.borrower = borrower
        self.due_date = due_date
        self.loan_date = loan_date
        self.return_date = return_date
        self.status = status
        self.cod_loan = cod_loan

    # Getters
    def get_book(self):
        return self.book
    
    def get_borrower(self):
        return self.borrower
    
    def get_due_date(self):
        return self.due_date
    
    def get_loan_date(self):
        return self.loan_date
    
    def get_return_date(self):
        return self.return_date
    
    def get_status(self):
        return self.status
    
    def get_cod_loan(self):
        return self.cod_loan
    
    # Setters
    def set_book(self, book):
        self.book = book
    
    def set_borrower(self, borrower):
        self.borrower = borrower
    
    def set_due_date(self, due_date):
        self.due_date = due_date
    
    def set_loan_date(self, loan_date):
        self.loan_date = loan_date
    
    def set_return_date(self, return_date):
        self.return_date = return_date
    
    def set_status(self, status):
        self.status = status
    
    def set_cod_loan(self, cod_loan):
        self.cod_loan = cod_loan
    
    