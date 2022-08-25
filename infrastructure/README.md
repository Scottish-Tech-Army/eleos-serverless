
# Eleos infrastructure

This infrastructure is built with the AWS Cloud Development Kit (CDK).

## Initial setup

 * Full setup details can be found at [AWS CDK Getting Started](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)
 * A getting started tutorial from AWS can be found [here](https://aws.amazon.com/getting-started/guides/setup-cdk/)

You will need the following setup:

 * Node.js and NPM are required to generate and run a CDK application
 * Install the AWS CDK: `npm install --global aws-cdk`
 * To generate a new project, make and move into a new directory, run: `cdk init app --language python`
 * Activate the virtual environment: `source .venv/bin/activate`
 * Install/upgrade dependencies by running: `pip install --upgrade -r requirements.txt`
 * To be able to run tests with pytest run `pip install --upgrade -r requirements-dev.txt`
 * The entry point for the app will be: `./app.py`

## To work with the lastest code in this repo
 * Make sure you have completed the initial setup steps
 * Clone the repo `git clone https://github.com/Scottish-Tech-Army/eleos-serverless.git`
 * Move into the cloned directory `cd eleos-serverless`
 * Best to make a local development branch `git switch nameofyouruniquebranch`
 * Move into the infrastructure directory, where the cdk code is kept `cd infrastructure`
 * Create a virtual environment as .venv `python -m venv .venv`
 * Activate the virtual environment with `source .venv/bin/activate`
 * Install/upgrade dependencies by running: `pip install --upgrade -r requirements.txt`
 * To be able to run tests with pytest also run `pip install --upgrade -r requirements-dev.txt`
 * Continue to Development below

## Development

To get started with development:

 * Activate the virtual environment if it is not already active `source .venv/bin/activate`
 * Edit infrastructure code in: `./eleos/eleos_stack.py`
 * Synthesise the CloudFormation template with `cdk synth`
 * Check differences to be deployed by running: `cdk diff`
 * Deploy infrastructure changes by running `cdk deploy`

## Tidy Up when you have finished
 * Destroy the deployed app with `cdk destroy` in development to avoid extra costs
 * Deactivate the vitual environment `deactivate`

NB you will need to have AWS credentials to run `cdk deploy`.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
