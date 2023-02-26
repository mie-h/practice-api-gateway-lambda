import json

"""
For testing:
curl -X GET "https://4j4b97ntr0.execute-api.us-west-1.amazonaws.com/test_stage/transactions?transaction_id=1&amount=100"
"""

def lambda_handler(event, context):
    print(event)
    transaction_id = event['queryStringParameters']['transaction_id']
    transaction_amount = event['queryStringParameters']['amount']
    
    print(f"transaction_id: {transaction_id}")
    print(f"transaction_amount: {transaction_amount}")

    transaction_response = {}
    transaction_response['transaction_id'] = transaction_id
    transaction_response['transaction_amount'] = transaction_amount

    response = {}
    response['statusCode'] = 200
    response['body'] = json.dumps(transaction_response)

    return response


def main():
    event = {'params': {'transaction_id': 1, 'amount': 100}}
    lambda_handler(event, None)

if __name__ == "__main__":
    main()