import boto3


def get_instances(access_key, secret_key, region_name='us-east-1'):
    ec2 = boto3.resource('ec2',
                         aws_access_key_id=access_key,
                         aws_secret_access_key=secret_key, region_name=region_name)
    instances = ec2.instances.filter(Filters=[{
        'Name': 'instance-state-name',
        'Values': ['running', 'stopped']}])

    ec2info = [i.id for i in instances]
    return ec2info
