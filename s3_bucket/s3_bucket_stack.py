from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3
)
from constructs import Construct

class S3BucketStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        bucket = s3.Bucket(self, 
                           "my-demo-bucekt", 
                           bucket_name="demo-cdk--t-d-g")