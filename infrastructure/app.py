#!/usr/bin/env python

from time import sleep
from list_stacks import pull_stacks
from aws_cdk import App, Stack, Tags, Environment
from eleos.eleos_stack import EleosStack

# regions
london = "eu-west-2"
# account numbers
dev_test_acc = "113725134633"
lms_stag_prod_acc = "131458236732"
tampontaxi_stag_prod = "677304537696"
##### other account numbers to be added here

# Odoo versions
odoo_16 = "odoo:16"
odoo_15 = "odoo:15"
odoo_14 = "odoo:14"

# Environments
dev = "dev"
test = "test"
stage = "stage"
prod = "prod"

### naming convention  = account - odoo version - environment

app = App()


def get_account():
    try:
        account = pull_stacks()[2]
        alias = pull_stacks()[3]
        print(f"Working in account: {alias}")
        return account
        sleep(2)
    except Exception as error:
        print("Failed account check!")
        print(f"{error}")


## Below are the stacks defined in each account, add remove or edit here ##

########################################################################
#                       eleos-dev-test account                         #
########################################################################
acc = get_account()
if acc == dev_test_acc:
    Eleos_dev_stack2 = EleosStack(
        app,
        "dev-test-16-dev",  # this is the construct_id used to call the stack
        env=Environment(account=dev_test_acc, region=london),
        odoo_version=odoo_16,
        environ=dev,
    )

    Eleos_dev_stack = EleosStack(
        app,
        "dev-test-14-dev",
        env=Environment(account=dev_test_acc, region=london),
        odoo_version=odoo_14,
        environ=dev,
    )

    Tags.of(Eleos_dev_stack2).add("tag", "ODOO 16 DEV")
    Tags.of(Eleos_dev_stack).add("tag", "DEV")

########################################################################
#                       lms-stag-prod-acc                              #
########################################################################
if acc == lms_stag_prod_acc:
    Eleos_lms_stag_prod = EleosStack(
        app,
        "lms-stag-prod-15-stag",
        env=Environment(account=lms_stag_prod_acc, region=london),
        odoo_version=odoo_15,
        environ=stage,
    )

    Tags.of(Eleos_lms_stag_prod).add("tag", "STAGE")

########################################################################
#                      tampontaxi-stag-prod                            #
########################################################################
if acc == tampontaxi_stag_prod:
    Eleos_tampontaxi_stag_prod = EleosStack(
        app,
        "tampontaxi-stag-prod-14-stag",
        env=Environment(account=tampontaxi_stag_prod, region=london),
        odoo_version=odoo_14,
        environ=stage,
    )

    Tags.of(Eleos_tampontaxi_stag_prod).add("tag", "STAG-SERVERLESS")

########################################################################
app.synth()


# If you don't specify 'env', this stack will be environment-agnostic.
# Account/Region-dependent features and context lookups will not work,
# but a single synthesized template can be deployed anywhere.
# Uncomment the next line to specialize this stack for the AWS Account
# and Region that are implied by the current CLI configuration.
# env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
# Uncomment the next line if you know exactly what Account and Region you
# want to deploy the stack to. */
# env=cdk.Environment(account='123456789012', region='us-east-1'),
# For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
