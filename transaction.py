from datetime import datetime


class Transaction:
    VALID_OUTFLOW_CATEGORIES = [
        "rent",
        "tuition",
        "utilities",
        "cell",
        "internet",
        "food",
        "clothes",
        "transportation",
        "insurance",
        "entertainment",
        "loan",
        "moustafa",
        "sharaf",
        "therapy",
        "installments",
        "deposit",
        "travel",
        "loan",
        "other"
    ]

    VALID_INFLOW_CATEGORIES = [
        "salary",
        "overtime",
        "deposit",
        "scholarship",
        "family",
        "friends",
        "loan"
    ]

    def __init__(self,
                 category: str,
                 amount: float,
                 month: int,
                 year: int,
                 type: str) -> None:
        self.amount = self.validate_amount(amount)
        self.category = self.validate_category(category=category,
                                               type=type)
        self.month = self.validate_month(month)
        self.year = self.validate_year(year)
        self.type = self.validate_type(type)


    def validate_category(self, category: str, type: str) -> str:
        category_lower = category.lower()
        if type == 'inflow' and category_lower not in Transaction.VALID_INFLOW_CATEGORIES:
            raise ValueError(f"Invalid inflow category. Must be one of {self.VALID_INFLOW_CATEGORIES}.")
        if type == 'outflow' and category_lower not in Transaction.VALID_OUTFLOW_CATEGORIES:
            raise ValueError(f"Invalid outflow category. Must be one of {self.VALID_OUTFLOW_CATEGORIES}.")
        return category_lower

    @staticmethod
    def validate_amount(amount: float) -> float:
        if not isinstance(amount, (float, int)) or amount < 0:
            raise ValueError("Amount must be a non-negative number.")
        return float(amount)

    @staticmethod
    def validate_month(month: int) -> int:
        if not isinstance(month, int) or not (1 <= month <= 12):
            raise ValueError("Month must be an integer between 1 and 12.")
        return month

    @staticmethod
    def validate_year(year: int) -> int:
        current_year = datetime.now().year
        if not isinstance(year, int) or not (current_year - 2 <= year <= current_year + 2):
            raise ValueError(f"Year must be an integer between {current_year - 2} and {current_year + 2}.")
        return year

    @staticmethod
    def validate_type(type: str) -> str:
        type_lower = type.lower()
        if type_lower not in ['inflow', 'outflow']:
            raise ValueError("Type must be either 'inflow' or 'outflow'.")
        return type_lower

    def to_dict(self) -> dict:
        """Convert the Transaction object to a dictionary."""
        return {
            'category': self.category,
            'amount': self.amount,
            'month': self.month,
            'year': self.year,
            'type': self.type
        }
