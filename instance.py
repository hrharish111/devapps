import argparse
import boto.ec2
import sys
access_key = ''
secret_key = ''
csv_file = open('ib4.csv','a+')
instance_name=[]
Region=[]
instance_id=[]
instance_state=[]
instance_ip_address=[]
instance_public_dns_name=[]
def get_ec2_instances(region):
    ec2_conn = boto.ec2.connect_to_region(region,
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key)

    reservations = ec2_conn.get_all_instances()
    for reservation in reservations:

        for inst in reservation.instances:     
            instance_name.append(inst.tags.get('Name'))
            print region
            Region.append(region)
            instance_id.append(inst.id)
            instance_state.append(inst.state)
            instance_ip_address.append(inst.ip_address)
            instance_public_dns_name.append(inst.public_dns_name)
    
            
                 
                 


def main():

    header = "Tag Name,Region,Instance ID,Instance State,Instance IP,DNS_Name\n"
    csv_file.write(header)
    global access_key
    global secret_key

    
    access_key = sys.argv[1]
    secret_key = sys.argv[2]
    regions = []
    for i in range(0,len(sys.argv)):
		
	if i > 2:  
		regions.append(str(sys.argv[i]))


    for region in regions: get_ec2_instances(region)
    
    for i in range(0,len(instance_name)):
	
        header1 = "%s,%s,%s,%s,%s,%s\n"%(instance_name[i],Region[i],instance_id[i],instance_state[i],instance_ip_address[i],instance_public_dns_name[i])
	
	csv_file.write(header1)
        print header1 
    csv_file.flush()
    csv_file.close()   
if  __name__ =='__main__':main()
