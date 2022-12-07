#!/usr/bin/env python

from time import sleep
from list_stacks import pull_stacks
from aws_cdk import App, Stack, Tags, Environment
from eleos.eleos_stack import EleosStack

# regions
london = 'eu-west-2'
# account numbers
dev_test_acc = '113725134633'
lms_stag_prod_acc = '131458236732'
##### other account numbers to be added here

# Odoo version
odoo_16 = 'odod:16'
odoo_15 = 'odoo:15'
odoo_14 = 'odoo:14'

# Environments
dev = 'dev'
test = 'test'
test2 = 'test2' ##temp
stage = 'stage'
prod = 'prod'

### naming convention  = account - odoo version - environment

app = App()
acc = pull_stacks()[2]
alias = pull_stacks()[3]
print(f'Working in account: {alias}')
sleep(2)

## Below are the stacks defined in each account, add remove or edit here ##

########################################################################
#                       eleos-dev-test account                         #
########################################################################
if acc == dev_test_acc:
    Eleos_test_stack = EleosStack(app, 
        'dev-test-15-test', # this is the construct_id used to call the stack
        env=Environment(account=dev_test_acc, region=london),
        odoo_version = odoo_15,
        environ = test,
        )

    Eleos_test2_stack = EleosStack(app, 
        'dev-test-15-test2',
        env=Environment(account=dev_test_acc, region=london),
        odoo_version = odoo_15,
        environ = test2,
        )

    Eleos_dev_stack = EleosStack(app,
        'dev-test-15-dev',
        env=Environment(account=dev_test_acc, region=london),
        odoo_version = odoo_15,
        environ = dev,
        )

    Tags.of(Eleos_test_stack).add('tag', 'TEST')
    Tags.of(Eleos_test2_stack).add('tag', 'TEST2')
    Tags.of(Eleos_dev_stack).add('tag', 'DEV')

########################################################################
#                       lms-stag-prod-acc                              #
########################################################################
if acc == lms_stag_prod_acc:
    Eleos_lms_stag_prod = EleosStack(app,
        'lms-stag-prod-15-stag',
        env=Environment(account=lms_stag_prod_acc, region=london),
        odoo_version = odoo_15,
        environ = stage,
        )
    Tags.of(Eleos_lms_stag_prod).add('tag', 'STAGE')

########################################################################

app.synth()


    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.
    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.
    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */
    #env=cdk.Environment(account='123456789012', region='us-east-1'),
    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html