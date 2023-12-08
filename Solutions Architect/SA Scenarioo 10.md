## SA Scenario 10
> ## Container Services

* ### Amazon ECR (Elastic Container Service) and ECR (Elastic Container Registry)
* ### Cloud9 - IDE
  
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/02df9f38-92b1-40d2-86f2-8d9cb585cac8">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/3f49876f-0812-429f-9b33-6a6152d3e719">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/2df14b19-dc12-40b5-be9a-f615fa037a41">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/72030914-abbf-4b92-b07f-ce9e0169487b">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/cfb1b193-1936-4142-84fa-882b9308ebc4">

<img src ="https://github.com/Brindha-m/AWS_Games/assets/72887609/739519fc-a2f5-4f03-97e8-0cbedc34ebc9">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/6989266c-d304-45e5-95f3-f53a2f1bc4d4">

## Lets Get started..
## Commands in Cloud9 IDE.

### Setup and Configuration

#### 1. Unzip the lab_code.zip:
    
    unzip lab_code.zip
   

#### 2. Install Docker:
    ```
    ./install_scripts/install_docker.sh
    
    ```

#### 3. Set the AWS region (default to us-east-1 if not configured):
    ```
    region=$(aws configure get region)
    region=${region:-us-east-1}
    
    ```

### Repository Creation

#### 4. Create a repository name:
    ```bash
    repo_name="my_app"
    ```

#### 5. Get AWS account and create a repository in Amazon ECR:
    ```
    account=$(aws sts get-caller-identity --query Account --output text)
    
    fullname="${account}.dkr.ecr.${region}.amazonaws.com/${repo_name}:latest"
    
    aws ecr create-repository --repository-name "${repo_name}"
    ```

### Docker Image Management

#### 6. Retrieve authentication token and log in to ECR:
    ```
    aws ecr get-login-password --region ${region} | docker login --username AWS --password-stdin ${fullname}
    ```

#### 7. Build, tag, and verify Docker images locally:
    ```
    cd ~/environment/first_app
    
    docker build -t ${repo_name} .
    
    docker images --filter reference=my_app
   
    ```

### Push Docker Image to ECR

#### 8. Push Docker image to Amazon ECR:
    ```
    docker tag ${repo_name} ${fullname}
    
    docker push ${fullname}
    ```

#### 9. Compile and push the image of second_app to Amazon ECR:
    ```
    cd ~/environment/install_scripts/
    
    ./push_second_app.sh
    
    ```

#### 10. Review logs from push_second_app.sh and proceed to the next step.


