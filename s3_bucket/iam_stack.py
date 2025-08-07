from aws_cdk import (
    Stack,
    aws_iam as iam
)
from constructs import Construct

class iam_user_Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create a user
        user = iam.User(self, "user", user_name="admin_user", password="12345678", password_reset_required=True)

        # assign value as access key
        access_key = iam.AccessKey(self, "access-key", user=user)
        
        # attach policy 
        attach_policy = iam.Policy(self, 
                                   "admin-policy", 
                                   policy_name="admin-access-cli", 
                                   statements=[
                                       iam.PolicyStatement(
                                           actions=["*"],
                                           resources=["*"],
                                       )
                                   ],
                                   )

        attach_policy.attach_to_user(user)
        

# from aws_cdk import (
#     core as cdk,
#     aws_iam as iam,
# )

# class IamUserStack(cdk.Stack):
#     def __init__(self, scope: cdk.App, id: str, props=None) -> None:
#         super().__init__(scope, id, props)

#         user = iam.User(self, 'IamUser',
#                         user_name='iam-user')

#         policy = iam.Policy(self, 'Policy',
#                             policy_name='IamUserPolicy',
#                             statements=[
#                                 iam.PolicyStatement(
#                                     actions=['s3:ListBucket'],
#                                     resources=['arn:aws:s3:::*'],
#                                 )
#                             ])

#         policy.attach_to_user(user)