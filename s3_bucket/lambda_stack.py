from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,

)


from constructs import Construct

class lambda_stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

# first lambda name 
        my_lambda = _lambda.Function(
            self,
            "api-lambda",
            runtime=_lambda.Runtime.PYTHON_3_13,
            code=_lambda.Code.from_asset('lambda'),
            handler='hello.handler',
            description="this is demo code",
            architecture=_lambda.Architecture.X86_64,
            function_name="api-to-lambda-cdk",
        )

        # connect with api
        lambda_api= apigw.LambdaRestApi(
            self,
            "endpoint",
            handler=my_lambda,
            rest_api_name="api-to-lambda-cdk",
        )

        print(lambda_api)