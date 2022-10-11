#!/usr/bin/env python3

#import aws_cdk as cdk
from aws_cdk import App, Stack, Tags, Environment
from eleos.eleos_stack import EleosStack

# regions
london = 'eu-west-2'
# account numbers
dev_test_acc = '113725134633'
##### other account numbers to be added here

# Odoo version
odoo_15 = 'odoo:15'
odoo_14 = 'odoo:14'

# Environments
dev = 'dev'
test = 'test'
stage = 'stage' #?
prod = 'prod'

# name account - odoo version - environment

app = App()

# dev-test account
Eleos_test_stack = EleosStack(app, 
    'dev-test-15-test', # this is the construct_id used to call the stack
    env=Environment(account=dev_test_acc, region=london),
    odoo_version = odoo_15,
    environ = test,
    )

Eleos_dev_stack = EleosStack(app,
    'dev-test-15-dev',
    env=Environment(account=dev_test_acc, region=london,),
    odoo_version = odoo_15,
    environ = dev,
    )

Tags.of(Eleos_test_stack).add('tag', 'TEST')
Tags.of(Eleos_dev_stack).add('tag', 'DEV')

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