
# Eleos infrastructure

This infrastructure is built with the AWS Cloud Development Kit (CDK).

## Initial setup

You will need the following setup:

 * Node.js and NPM are required to generate and run a CDK application
 * Install the AWS CDK: `npm install --rlobal aws-cdk`
 * To generate a new project, run: `cdk init app --language python`
 * The entry point for the app will be: `./app.py`

## Development

To get started with development:

 * Activate the virtual environment: `source .venv/bin/activate`
 * Install/upgrade dependencies by running: `pip install --upgrade -r requirements.txt`
 * Edit infrastructure code in: `./eleos/eleos_stacl.py`
 * Check differences to be deployed by running: `cdk diff`
 * Deploy infrastructure changes by running `cdk deploy`

NB you will need to have AWS credentials to run `cdk deploy`.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
