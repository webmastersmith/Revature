import json
import boto3

client = boto3.client('ec2')
instance1 = 'i-0b2c69b9e2789466e'

def stop_instance(client, instance1):
    response = client.stop_instances(
        InstanceIds=[ instance1 ],
        # Hibernate=True|False,
        # DryRun=True
        # Force=True|False
    )
    print( json.dumps(response, indent=2, default=str))



stop_instance(client, instance1)