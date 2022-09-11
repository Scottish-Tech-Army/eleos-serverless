# eleos-serverless
### Repo for demonstration of AWS serverless environment for Eleos project

 > Setup and development instructions can be found in ./infrastructure/README.md

### Current Situation
 * STA infrastructure for Odoo based deployments use Terraform to create AWS cloud services utilising EC2 for compute.
 * STA Terraform code contains a separate code base for each environment in each account, increasing risk of errors.
 * No implimentation of CI/CD principles.
 * Terraform account restricts numbers of users in free tier, users must be added and removed manually to be able to manage resources.

### Objectives
 * Reduce the cost burden of AWS services to the STA and stakeholders.
 * Create IaC with a single codebase for all accounts and environments.
 * Impliment CI/CD.
 * Reduce admin tasks involved with managment of users.

### Tasks
 * Migrate to AWS serverless services - has been identified as a way to redude the cost burden.
 * Leverage AWS IaC service AWS Cloud Development Kit (CDK) to create IaC - no need to also manage Terraform accounts.
 * Create CI/CD pipeline with testing - faster and safer development and deployment of resources.

### Requirements / Identified resources*
 * Odoo Docker image for use in containers. 
 * AWS serverless compute using Fargate to manage ECS container cluster.
 * AWS serverless storage for Postgres database using RDS - Odoo requires a Postgres database.
 * AWS EFS for various static files used by Odoo and possibly custom Odoo modules.
 * AWS S3 bucket for transfer of custom Odoo Modules to EFS.
 * AWS Route53 for DNS routing.

 * GitHub actions for CI/CD using OIDC.

*Subject to change.

### Implimentation
 * AWS CDK code is written in Python as per a vote of the platform team.

### Draft Target Infrastructure

<img src="https://github.com/Scottish-Tech-Army/eleos-serverless/blob/main/images/DraftArchitecture.png">
