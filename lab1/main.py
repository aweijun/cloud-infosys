import boto3

AWS_REGION = 'us-east-1'

def create_instance(ec2_resource, number): 
    instances = ec2_resource.create_instances(
        ImageId='ami-02396cdd13e9a1257',
        MinCount=1,
        MaxCount=number,
        InstanceType='t2.micro',
        KeyName='cloud-infosys'
    )

    for instance in instances:
        # print(f'EC2 instance "{instance.id}" has been launched')
        instance.wait_until_running()
        print('EC2 instance has been started')


if __name__ == '__main__':
    ec2 = boto3.resource('ec2', region_name = AWS_REGION)
    create_instance(ec2, 2)