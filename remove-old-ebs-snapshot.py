from datetime import datetime, timedelta
import boto3
import csv

STATUS = 'Not delete'
# if job type is DELETE then delete the snapshots 
JOB_TYPE = 'DELETE'
DAYS = 15

ec2 = boto3.resource('ec2')

#List(ec2 snapshot)
snapshots = ec2.snapshots.all()
list_of_snapshots = [ s for s in snapshots]
delete_from_date = datetime.now() - timedelta(days=DAYS)
print delete_from_date
mydd = {"Snapshot ID":"" ,"Size":"" , "Description":"" , "Started":"" , "script_datetime":datetime.now(),"status":STATUS } 

with open('snapshotlistAll.csv', 'w') as csvfile:
        fieldnames = ['Snapshot ID' ,'Size' , 'Description' , 'Started','script_datetime','status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for l in list_of_snapshots:
            #print l
	    mydd = {"Snapshot ID":"" ,"Size":"" , "Description":"" , "Started":"" , "script_datetime":datetime.now(),"status":STATUS }
            if JOB_TYPE == 'DELETE':
	            snapshot_create_date = datetime.fromtimestamp(int(l.start_time.strftime('%s')))
	            if snapshot_create_date < delete_from_date:
	                mydd["status"] = "deleted"
			print l
	            # add line for actual delete as l.delete() it will delete when job type is DELETE


            mydd["Snapshot ID"] = l.snapshot_id
            mydd["Size"] = l.volume_size
            mydd["Description"] = l.description
            mydd["Started"] = l.start_time
            writer.writerow(mydd)
