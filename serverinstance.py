import boto.ec2

reg = "ap-southeast-1"
access_key = "AKIAJHJBI6HUTHFUD3RA"
secret_key = "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"
ec2_conn = boto.ec2.connect_to_region(reg,aws_access_key_id = access_key,
                                            aws_secret_access_key=secret_key)

p = ec2_conn.run_instances(
    'ami-6ac2a85a',
    key_name='nitheesh_oregon',
    instance_type='t1.micro',
    security_groups=['nitheesh_oregon']
)
print p
