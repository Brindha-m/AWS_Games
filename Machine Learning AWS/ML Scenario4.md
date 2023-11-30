## Scenario 4 - Set up ML Environment with Amazon SageMaker

> ## Amazon SageMaker

### Step 1: Explore SageMaker Notebooks

Explore the following SageMaker notebook images:

- ![Image 1](https://github.com/Brindha-m/AWS_Games/assets/72887609/6db9376f-bc88-4333-a7ea-dcca057dfffc)
- ![Image 2](https://github.com/Brindha-m/AWS_Games/assets/72887609/47928e24-e332-41f4-ac0d-62a49995e688)
- ![Image 3](https://github.com/Brindha-m/AWS_Games/assets/72887609/061f008c-5619-49da-bf60-7dadf7d3e883)
- ![Image 4](https://github.com/Brindha-m/AWS_Games/assets/72887609/2ed2a656-d029-4ce4-bc17-583d386b7c02)
- ![Image 5](https://github.com/Brindha-m/AWS_Games/assets/72887609/cf518847-9cd2-4fd5-bcaa-96cdfa558499)
- ![Image 6](https://github.com/Brindha-m/AWS_Games/assets/72887609/ca34b346-721c-4a8c-a197-673e9481f824)
- ![Image 7](https://github.com/Brindha-m/AWS_Games/assets/72887609/e2e33eeb-866f-4507-b23d-fa20624432d3)
- ![Image 8](https://github.com/Brindha-m/AWS_Games/assets/72887609/e5464ae4-29e2-468c-b524-eedf8c98452b)
- ![Image 9](https://github.com/Brindha-m/AWS_Games/assets/72887609/8347e465-5995-436e-909c-9d5b66c1a008)

- ![Image 10](https://github.com/Brindha-m/AWS_Games/assets/72887609/ed06b947-40a7-4d0a-a25a-8b4e4bd2c877)

### Step 2: Set up SageMaker Environment

1. Open the terminal and run the following commands:
    - `whoami`
    - `pwd`
    - `ls`

2. Download ML sample projects from GitHub:
    ```bash
    git clone https://github.com/aws/amazon-sagemaker-examples.git
    ```

3. In the left sidebar, click the File Browser (folder) icon.


![Image 1](https://github.com/Brindha-m/AWS_Games/assets/72887609/aa611a94-37b9-455d-9178-365b4e5d6d4b)
![Image 2](https://github.com/Brindha-m/AWS_Games/assets/72887609/627bbea9-9b88-4a65-8333-40f2969c63bf)
![Image 3](https://github.com/Brindha-m/AWS_Games/assets/72887609/2337537d-7dec-41d7-a514-2322dbd90d5f)

#### Instructions for Running Sample Projects:

- In the kernel environment, run each cell in the provided file.
- The code is about reviewing a film: 0 - negative review, 1 - positive review.

- ![Image 11](https://github.com/Brindha-m/AWS_Games/assets/72887609/d7bb76bc-9559-411e-8ef5-7ded9eef44e9)

- ![Image 12](https://github.com/Brindha-m/AWS_Games/assets/72887609/7a789f94-be63-46f1-9c4f-e5edd529e781)

- ![Image 13](https://github.com/Brindha-m/AWS_Games/assets/72887609/dd343a45-ecb8-42b6-b24b-783f55fd21fb)

- ![Image 14](https://github.com/Brindha-m/AWS_Games/assets/72887609/a96ef610-06bc-48ff-a6e4-04cd5b6e2ece)

- ![Image 15](https://github.com/Brindha-m/AWS_Games/assets/72887609/37a25d40-2cbf-4f35-946e-963d4e276bf3)

- ![Image 16](https://github.com/Brindha-m/AWS_Games/assets/72887609/e4da333c-b1f0-4c6b-a61d-6b4d0377b797)

- Copy the provided endpoint name: `mxnet-training-2023-11-30-16-07-35-079`

![Image 17](https://github.com/Brindha-m/AWS_Games/assets/72887609/5cf22490-e3ed-48ee-8a80-4d78f3c7f658)
![Image 18](https://github.com/Brindha-m/AWS_Games/assets/72887609/acc85e9f-74d5-478f-a23f-63031cec06f8)
![Image 19](https://github.com/Brindha-m/AWS_Games/assets/72887609/82bd61cb-3314-4956-b8af-f1a3a8c79e0a)
![Image 20](https://github.com/Brindha-m/AWS_Games/assets/72887609/34819391-2a81-4ced-bd75-98dd15a8bb1e)

![Image 21](https://github.com/Brindha-m/AWS_Games/assets/72887609/35a53bb3-d066-47ac-8f31-2265988f9a17)
![Image 22](https://github.com/Brindha-m/AWS_Games/assets/72887609/c719973e-0fb8-4353-942b-ef07c903cf30)

- Ensure the provided code is in the Amazon Lambda function.

![Image 23](https://github.com/Brindha-m/AWS_Games/assets/72887609/47bb612d-4e3d-411e-b34b-5237a6690b33)

![Image 24](https://github.com/Brindha-m/AWS_Games/assets/72887609/bc9ad3b7-921a-4a97-a7e0-c1ad997a3cbe)
![Image 25](https://github.com/Brindha-m/AWS_Games/assets/72887609/0f372aa8-87ce-4e7c-a875-65bcfd043b46)
![Image 26](https://github.com/Brindha-m/AWS_Games/assets/72887609/64177588-cf3c-4212-a46d-168f6261a1c6)

**Code in Lambda Function:**
```python
# Test Data of 3 movie reviews
client = boto3.client('sagemaker-runtime')
test_file = io.StringIO('["The movie was horrible","This should be awarded an Oscar","I did not like the ending"]')
payload = test_file.getvalue()
```

![Image 27](https://github.com/Brindha-m/AWS_Games/assets/72887609/27bace3d-decf-46e7-af90-db3d85118926)


