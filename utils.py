import boto3

from config import REGION


def get_instances(access_key, secret_key, region_name=REGION):
    ec2 = boto3.resource('ec2',
                         aws_access_key_id=access_key,
                         aws_secret_access_key=secret_key, region_name=region_name)
    ec2_info = [{"instance_id": i.get('InstanceId'), "instance_state": i.get("InstanceState").get("Name"),
                 "availability_zone": i.get("AvailabilityZone")} for i in
                ec2.meta.client.describe_instance_status()['InstanceStatuses']]
    return ec2_info
