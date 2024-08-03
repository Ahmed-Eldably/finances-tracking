from transaction import Transaction

category = "Rent"
amount = 100
month = 8
year = 2024
type = "outflow"



transaction_outflow = Transaction(
    category=category,
    amount=amount,
    month=8,
    year=year,
    type=type
)

transaction_outflow_dict = transaction_outflow.to_dict()

print(transaction_outflow_dict)





