import os
import io
import boto3
import json
import csv
import logging

# It is good practice to use proper logging.
# Here we are using the logging module of python.
# https://docs.python.org/3/library/logging.html

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Endpoint name from the Environment variable
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']

# ##When testing for island friendly vehicles uncomment these lines
# value_0 = "not-friendly"
# value_1 = "island-friendly"

##When testing for spy drones uncomment these lines
value_0 = "friendly-drone"
value_1 = "spy-drone"


def lambda_handler(event, context):
  
   # Using sagemaker boto3 client.
   # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html
   sagemaker_runtime = boto3.client('sagemaker-runtime')
   
   # Reading the data payload from the test event
   data = json.loads(json.dumps(event))
   #payload = data['data']
   
   
   # Sending the payload to the Sagemaker Endpoint using Invoke Endpoint API
   # Boto3 info: https://boto3.amazonaws.com/v1/documentation/api/1.9.42/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.invoke_endpoint
   
   results = []
   
   for i in range(0,3):
      payload = data['data'+str(i)]
      print(payload)
      endpoint_response = sagemaker_runtime.invoke_endpoint(
                                             EndpointName=ENDPOINT_NAME,
                                             ContentType='text/csv',
                                             Body=payload
                                             )
   
      logger.info(endpoint_response)
      result = json.loads(endpoint_response['Body'].read().decode())
      if result > .5:
         results.append(value_1)
      else:
         results.append(value_0)
   
   return results   
   
   
"""
You can use the code below to create a test event.

Island-Friendly: The below test data will result in 2 island-friendly vehicles and one non-friendly.

{
  "data0": "2458,92.0,27,11248.0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0",
  "data1": "2081,70.0,30,6938.0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0",
  "data2": "4967,68.0,15,36229.0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0"
}


Spy-Drones: The below test data will result in spy-drone, friendly-drone, spy-drone due to the flight duration, transponder, max-altitude, and max speed

{
  "data0": "36,1.0,22,14",
  "data1": "15,1.0,8,7",
  "data2": "25,1.0,40,35"
}
"""

