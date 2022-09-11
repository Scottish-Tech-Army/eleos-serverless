import aws_cdk as core
from aws_cdk.assertions import Template, Match
from eleos.eleos_stack import EleosStack



def test_dbname_matches():
    app = core.App()
    stack = EleosStack(app, "eleos")
    template = Template.from_stack(stack)
    
    template.has_resource_properties("AWS::RDS::DBCluster", {
        "DatabaseName": "postgres"
        })

def test_dbuser_matches():
    app = core.App()
    stack = EleosStack(app, "eleos")
    template = Template.from_stack(stack)

    template.has_resource_properties("AWS::RDS::DBCluster", {
        "MasterUsername": "odoo"
        })

def test_task_definition_mount_points():
    app = core.App()
    stack = EleosStack(app, "eleos")
    template = Template.from_stack(stack)

    template.has_resource_properties("AWS::ECS::TaskDefinition",
        Match.object_like( {
            "ContainerDefinitions": [
                   {
                    "Environment": [
                        {
                        "Name": "DB_PORT_5432_TCP_ADDR",
                        "Value": {
                            "Fn::GetAtt": [
                                "postgres6BBC2FA4",
                                "Endpoint.Address"
                                ]
                            }
                        }
                    ],
                    "Essential": True,
                    "Image": "odoo:latest",
                    "LogConfiguration": {
                        "LogDriver": "awslogs",
                        "Options": {
                            "awslogs-group": {
                                "Ref": "odooFargateServiceTaskDefodooContainerLogGroupB787C48A"
                                },
                            "awslogs-stream-prefix": "odooFargateService",
                            "awslogs-region": {
                                "Ref": "AWS::Region"
                                }
                            }
                        },
                    "MountPoints": [
                        {
                        "ContainerPath": "/var/lib/odoo",
                        "ReadOnly": False,
                        "SourceVolume": "odooVolume"
                        }
                        ],
                    "Name": "odooContainer",
                    "PortMappings": [
                       {
                         "ContainerPort": 8069,           
                         "Protocol": "tcp"
                       }
                     ],
                     "Secrets": [
                       {
                         "Name": "POSTGRES_PASSWORD",
                         "ValueFrom": {
                           "Fn::Join": [
                             "",
                             [
                               {
                                 "Ref": "postgresSecretAttachmentE987A31D"
                               },
                               ":password::"
                             ]
                           ]
                         }
                       }
                     ]
                   }
                 ],
                 "Cpu": "512",
                 "ExecutionRoleArn": {
                   "Fn::GetAtt": [
                     "odooFargateServiceTaskDefExecutionRoleC8AE90B9",
                     "Arn"
                   ]
                 },
                 "Family": "eleosodooFargateServiceTaskDefDD9DFCA8",
                 "Memory": "2048",
                 "NetworkMode": "awsvpc",
                 "RequiresCompatibilities": [
                   "FARGATE"
                 ],
                 "TaskRoleArn": {
                   "Fn::GetAtt": [
                     "odooFargateServiceTaskDefTaskRoleA7B2D8EF",
                     "Arn"
                   ]
                 },
                 "Volumes": [
                   {
                     "EfsVolumeConfiguration": {
                       "AuthorizationConfig": {
                         "AccessPointId": {
                           "Ref": "odooEfsAccessPoint59A957B6"
                         },
                         "IAM": "ENABLED"
                       },
                       "FileSystemId": {
                         "Ref": "odooEfsFileSystemD23A9885"
                       },
                       "TransitEncryption": "ENABLED"
                     },
                     "Name": "odooVolume"
                   }
                 ]
             }
        ))