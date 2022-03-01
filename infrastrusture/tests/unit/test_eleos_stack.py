import aws_cdk as core
import aws_cdk.assertions as assertions

from eleos.eleos_stack import EleosStack

# example tests. To run these tests, uncomment this file along with the example
# resource in eleos/eleos_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = EleosStack(app, "eleos")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
