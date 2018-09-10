import boto3
import yaml


def set_dependant_resources(resource, configs):
    resource_type = resource["EvaluationResultIdentifier"]["EvaluationResultQualifier"]["ResourceType"].replace("::","").replace("AWS","")
    resource_id = resource["EvaluationResultIdentifier"]["EvaluationResultQualifier"]["ResourceId"]

    # If S3 Bucket is listed Object need to be exluded as a dependency
    if resource_type == "S3Bucket":
        configs["accounts"]["369932205291"]["filters"]["S3Object"].append({"property": "Bucket", "value": resource_id})
        resource_id = "s3://{}".format(resource_id)

    configs["accounts"]["369932205291"]["filters"][resource_type].append(resource_id)

def get_compliant_resources():
  session = boto3.Session()
  aws_config = session.client('config')
  response = aws_config.get_compliance_details_by_config_rule(
      ConfigRuleName='tags-compliance',
      ComplianceTypes=[
          'NON_COMPLIANT',
      ],
  )
  return response["EvaluationResults"]

# Read the template file
with open("config_template_cr_labs.yaml", 'r') as stream:
    try:
        configs = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

resources = get_compliant_resources()
for resource in resources:
    set_dependant_resources (resource, configs)

# Save the definitive config
with open("config.yaml", "w") as config:
    try:
        yaml.dump(configs, config)
    except:
        print ("exception")
