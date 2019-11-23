# net-sandbox

juniper-vmx - AWS CloudFormation template, that creates stack with
VPC and single EC2 bare-metal instance with CentOS and Ansible

ansible/vmx_centos_prepare.yml -
Ansible playbook that installs prerequisites for Juniper vMX virtual machines

Notes - https://github.com/sgrade/_Lab/blob/master/Juniper/aws_vmx_sandbox.txt

IMPORTANT!
After deletion of the stack, don't forget to check if all the resources are
deleted

To ssh to the EC2 instance:
- get the DNS name in EC2 console
- ssh centos@ec2_instance_dns_name
