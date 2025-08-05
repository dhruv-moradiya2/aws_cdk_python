from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    CfnOutput 
)
from constructs import Construct

class Ec2InstanceStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # choose defualt vpc
        vpc = ec2.Vpc.from_lookup(self, "defualtvpc", is_default=True)

        # create new sg in aws 
        sg = ec2.SecurityGroup(
            self,
            "mysecuritygroup",
            vpc=vpc,
            allow_all_outbound=True,
            description="allow only ssh, http and https",
            security_group_name="ec2_group_cdk"
        )

        # ssh 22
        sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.SSH, "allow ssh")
        
        # http 22
        sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.HTTP, "allow http")

        # https 443 
        sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.HTTPS, "allow https")

        # ec2 main details 
        instance = ec2.Instance(
            self,
            "ec2Instance",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux2(),
            vpc=vpc,
            security_group=sg,
            key_name="deops-key"
        )

        # print pub ip for ec2 
        instance_pub_ip=CfnOutput(self, "instancepubip", value=instance.instance_public_ip)
        

        print("ec2 public ip:", instance_pub_ip)