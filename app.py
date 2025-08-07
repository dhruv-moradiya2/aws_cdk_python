#!/usr/bin/env python3
import os
import aws_cdk as cdk
from s3_bucket.s3_bucket_stack import S3BucketStack
from s3_bucket.ec2_instance_stack import Ec2InstanceStack
from s3_bucket.lambda_stack import lambda_stack
from s3_bucket.iam_stack import iam_user_Stack

app = cdk.App()

# for s3 bucket deploy
S3BucketStack(app, "S3BucketStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #########################################################################
    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    #########################################################################

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #############################################################
    #env=cdk.Environment(account='12345678', region='us-east-1'),
    #############################################################

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

# for ec2 deploy
Ec2InstanceStack(app, "EC2Instance", 

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    #env=cdk.Environment(account='12345678', region='us-east-1'),
                      
    )

# for api with lambda deploy
lambda_stack(app, "lambda-stack-api",
    
    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    #env=cdk.Environment(account='12345678', region='us-east-1'),
    
    )

# for i am user 
iam_user_Stack(app, "iam-user", 
               
    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    #env=cdk.Environment(account='12345678', region='us-east-1'),

    )

app.synth()
