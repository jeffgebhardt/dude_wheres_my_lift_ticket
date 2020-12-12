from datetime import datetime

class Validator:

    @staticmethod
    def validate_date_not_lapsed(self, reservation_date):
        if reservation_date >= datetime.now():
            return False

        return True
