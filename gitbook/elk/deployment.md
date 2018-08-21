# Deployment

## Steps to deploy ELK stack on AWS

Run the following script to bring up the elk stack in your AWS environment

```bash
deploy-elk-stack-infra
```

**Please Note: This script may take up to 10 minutes to complete**

This script will

* Use the stored AWS credentials to deploy elk stack in your AWS account using a custom AMI
* It will print the information to access the machine if successful
* Please save this returned information for later use

> If you see any error, please inform one of the trainers


![ELK Stack deployment success](images/deploy-elk-infra-sucess.png)


## Send details to trainers via Slack DM

* Please send the IP address output of the above script with your unique name in slack DM to `@madhuakula`
* Trainers will add the given IP address in DNS records to access the elk stack using below domain 


## Accessing the ELK stack

* Now, you can use the below URL to access the ELK stack with following credentials

```bash
http://elk.$uniquename.cloudsec.training
```

* Credentials for logging in to the basic authentication

```bash
username: elkadmin
password: AutomatedDefence@321
```

* Below is the command to ssh into the ELK stack

```bash
ssh ubuntu@$elk_machine_ip
```