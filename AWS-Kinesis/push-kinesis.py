#https://alpharm.hashnode.dev/processing-real-time-weather-data-with-aws-kinesis-and-lambda-storing-in-s3-and-monitoring-with-cloudwatch

import boto3
import random
import time
import json

session = boto3.Session(
    aws_access_key_id='id',
    aws_secret_access_key='key',
    region_name='region'
)
kinesis_client = session.client('kinesis')
stream_name='order-streams'

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
def put_records_to_kinesis(data):
    """put record to kinesis stream"""
    try:
        response = kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey=str(data['order_id'])
        )
        print(f"Record sent {data}")
    except Exception as e:
        print(f"Error sending data to kinesis: {str(e)}")
        
if __name__ == '__main__':
    try:
        while True:
            put_records_to_kinesis(generate_order_data())
            
            time.sleep(10)
    except KeyboardInterrupt:
        print(f"stopped manually !!!!!!")            