import boto3

client = boto3.client('ec2')
instance1 = 'i-0b2c69b9e2789466e'

def check_status(client, instance1):
    res = client.describe_instances(
        InstanceIds = [instance1]
    )
    # print(json.dumps(res, indent=2, default=str))
    #boto3 converts response to python dict

    # request response code
    metadata = res.get('ResponseMetadata')
    print('HTTP response code: ', metadata.get('HTTPStatusCode'))

    # zone
    zone = res.get('Reservations')[0].get('Instances')[0].get('Placement').get('AvailabilityZone')
    print('Zone: ', zone)
    
    # ip address assigned to ec2 terminal
    network_interface = res.get('Reservations')[0].get('Instances')[0].get('NetworkInterfaces')[0].get('Association')
    try:
        public_dns_name = network_interface.get('PublicDnsName')
        public_ip = network_interface.get('PublicIp')
        print('Public Ip: ', public_ip)
        print('Dns Name: ', public_dns_name)
    except:
        print('Public Ip: No Ip')
        print('Dns Name: No Dns Name')

    # status of running server
    state = res.get('Reservations')[0].get('Instances')[0].get('State')
    print('Status code: ', state.get('Code'), ' (0:pending, 16:running, 32:shutting-down, 48:terminated, 64:stopping, 80:stopped)')
    print('Status name: ', state.get('Name'))



check_status(client, instance1)
