from aws_cdk import (
    # Duration,
    RemovalPolicy,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
from aws_cdk import aws_ecs_patterns
from aws_cdk import aws_ecs
from aws_cdk import aws_ecr


class EleosStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ecr_repository = aws_ecr.Repository(
            self, "EcrRepository",
            repository_name="eleos",
            removal_policy=RemovalPolicy.DESTROY)

        task_image_options = aws_ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
            image=aws_ecs.ContainerImage.from_registry(
                name=ecr_repository.repository_name),
            container_port=8069)

        aws_ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "FargateService",
            assign_public_ip=True,
            desired_count=2,
            memory_limit_mib=1024,
            cpu=512,
            task_image_options=task_image_options)
