def trigger_alert(transaction,message):
    print(transaction,message)

def get_threshold():
    # get threshold logic
    return {}

def calculate_transaction_rate(syndicate):
    # calculate transaction rate logic
    return {}

def calculate_moving_average(syndicate,window_duration):
    # calculate moving average logic
    return {}

def receive_transaction():
    # transaction receive logic
    return {}

def store_transaction():
    # transaction store logic
    return {}

# Function to check threshold alerts
def check_threshold_alert(transaction):
    syndicate_threshold = get_threshold(transaction.syndicate)
    if transaction.amount > syndicate_threshold:
        trigger_alert(transaction, "Threshold exceeded")

# Function to check rate alerts
def check_rate_alert(transaction,window_duration):
    transaction_rate = calculate_transaction_rate(transaction.syndicate)
    moving_average = calculate_moving_average(transaction.syndicate, window_duration)
    
    if transaction_rate > 10 * moving_average:
        trigger_alert(transaction, "Spike in transaction rate")

# Other functions for database operations, alert triggering, etc.

# Transaction data processing
while True:
    transaction = receive_transaction()
    
    # Store the transaction in the database
    store_transaction(transaction)
    
    # Check for threshold alerts
    check_threshold_alert(transaction)
    
    # Check for rate alerts
    check_rate_alert(transaction)

