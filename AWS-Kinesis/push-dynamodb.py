#https://medium.com/@shrutighoradkar101/ingest-data-in-dynamodb-with-python-a307ac34170d
import boto3
import random
import time

session = boto3.Session(
    aws_access_key_id='id',
    aws_secret_access_key='key',
    region_name='region'
)

dynamodb = session.resource('dynamodb')
table = dynamodb.Table('order-table')
def generate_order_data():
    """Generate order data"""
    orderId = random.randint(1,10000)
    product_name=random.choice(['Laptop', 'Phone', 'Tablet', 'Headphones', 'Charger'])
    quantity=random.randint(1,5)
    price = str(round(random.uniform(500.0,10000.0),2))
    return{
        'order_id': orderId,
        'product_name': product_name,
        'quantity': quantity,
        'price': price
    }
def insert_dynamodb(data):
    """Insert data into dynamodb"""
    try:
        table.put_item(Item=data)
        print(f"Data inserted {data}")
    except Exception as e:
        print(f"Error{str(e)}")
        
if __name__ == '__main__':
    try:
        while True:
            insert_dynamodb(generate_order_data())
            
            time.sleep(20)
    except KeyboardInterrupt:
        print(f"stopped manually !!!!!!")            