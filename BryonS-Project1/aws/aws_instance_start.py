import json
import boto3

client = boto3.client('ec2')
instance1 = 'i-0b2c69b9e2789466e'


def start_instance(client, instance1):
    response = client.start_instances(
        InstanceIds=[instance1],
        # DryRun=True
    )
    print( json.dumps(response, indent=2, default=str))


start_instance(client, instance1)
