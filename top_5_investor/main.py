import csv
from collections import defaultdict

def top_investors(records, n=5):
    # Create a dictionary to store investors and their investments
    investor_data = defaultdict(lambda: [set(), 0])

    # Process the transaction records
    for record in records:
        investor_id, syndicate_id, amount, _ = record
        investor_data[investor_id][0].add(syndicate_id)  # Add syndicate to the investor's set
        investor_data[investor_id][1] += float(amount)  # Add the transaction amount


    # Sort the investors by the number of unique syndicates they've invested in and total amount
    sorted_investors = sorted(investor_data.items(), key=lambda x: (-len(x[1][0]), -x[1][1]) )

    # Get the top n investors
    top_n_investors = sorted_investors[:n]

    return top_n_investors

if __name__ == "__main__":
    # Read transaction records from a CSV file (replace 'transactions.csv' with your file)
    records = []
    with open('transactions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            records.append(row)

    # Call the top_investors function and print the results
    top_investors_list = top_investors(records, n=5)
    for i, (investor_id, (syndicates, total_amount)) in enumerate(top_investors_list, start=1):
        print(f"Top {i}: Investor {investor_id}, Syndicates: {len(syndicates)}, Total Amount: ${total_amount}")
