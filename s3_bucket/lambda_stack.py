from aws_cdk import (
    Stack,
    aws_lambda as _lambda
)
from constructs import Construct

class lambda_stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

# first lambda name 

# runtime lambda

# need handler

# code

