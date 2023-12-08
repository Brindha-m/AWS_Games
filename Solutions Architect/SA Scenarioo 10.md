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

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/427c6097-48b4-486b-82ce-27f8edbcc185">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/009b653d-fde4-4518-bb4d-d960a468d714">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/dd2fd38f-bd86-4756-ab19-f530896e133b">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/df86ebfa-6b6b-4b43-a4b3-4583e44cd2ff">

## Commands in Cloud9 IDE.


### Setup and Configuration

#### 1. Unzip the lab_code.zip:
    
    unzip lab_code.zip
   
  <img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/daa1a395-4209-4d8d-baf6-4c08dbdb57af">
  
<br>

#### 2. Install Docker:
    ```
    ./install_scripts/install_docker.sh
    
    ```
  <img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/0bb633ee-d0bc-4062-abe3-4f31b070c255">

<br>

#### 3. Set the AWS region (default to us-east-1 if not configured):
    ```
    region=$(aws configure get region)
    region=${region:-us-east-1}
    
    ```
  <img width="619" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/3e57d650-30dd-417d-9086-1d911e3cc2a1">

<br>

### Repository Creation

#### 4. Create a repository name:
    ```bash
    repo_name="my_app"
 
    ```
<br>

#### 5. Get AWS account and create a repository in Amazon ECR:
    ```
    account=$(aws sts get-caller-identity --query Account --output text)
    
    fullname="${account}.dkr.ecr.${region}.amazonaws.com/${repo_name}:latest"
    
    aws ecr create-repository --repository-name "${repo_name}"
    ```
  <img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/fa1d0265-31b8-48da-980f-dc80a03ece95">
  <img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/4ce7e7ca-4cf3-4dd3-ab99-200ce514a919">

<br>

### Docker Image Management

#### 6. Retrieve authentication token and log in to ECR:
    ```
    aws ecr get-login-password --region ${region} | docker login --username AWS --password-stdin ${fullname}
    ```

  <img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/440e3204-4457-4413-a66d-9b4aa8b95815">

<br>

#### 7. Build, tag, and verify Docker images locally:
    ```
    cd ~/environment/first_app
    
    docker build -t ${repo_name} .
    
    docker images --filter reference=my_app
   
    ```
  <img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/fe93d63e-32dd-4549-819b-010fa103b26c">
  <img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/a2b3657c-5296-4f17-bb48-3aad3e053c16">

<br>

### Push Docker Image to ECR

#### 8. Push Docker image to Amazon ECR:
    ```
    docker tag ${repo_name} ${fullname}
    
    docker push ${fullname}
    ```
  <img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/9914e0ca-fa18-49b2-b98e-32d93abaddac">

<br>

#### 9. Compile and push the image of second_app to Amazon ECR:
    ```
    cd ~/environment/install_scripts/
    
    ./push_second_app.sh
    
    ```
  <img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/5f66a5d8-1231-4b4a-9dbf-cd263d01afaa">

#### 10. Review logs from push_second_app.sh and proceed to the next step.


## Navigate to ECR..

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/5806a4fe-4e22-4d58-9422-f611212263cd">
<img src="https://github.com/Brindha-m/AWS_Games/assets/72887609/085cafbe-2e45-4345-b4b9-8fb9322ffccb">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/f6d10b19-4fe1-4b57-9e06-93d172c2ed46">

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/161ba2a8-a1b1-42cf-b98a-fd3c6d51aae9">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/4f55aa4c-aac7-4666-872d-294903be2a79">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/0ae8ec51-317a-45a9-8e52-ebc7e7e0fa1e">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/e2011ed2-733c-4ed4-a67b-71a61d63fb57">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/9a91ebfc-8cac-4751-8270-35ea84a4a865">

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/0964a47a-b7b9-4d21-a7b7-a3d13be76334">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/e364880e-1275-4c49-b93a-9f8166b6b938">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/7c6137d8-601a-4839-bbef-51f6499e0e22">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/533e707b-fbda-40f9-8839-a7aa0877b6f7">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/c94c4616-dba1-41f3-805d-c3837a771fbc">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/9e09b984-1876-4791-8ae6-066b08e3906e">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/ac11c61f-a5d1-49ca-81a9-fd2b4f77c541">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/a22440a8-4405-46c5-847d-a720c352cc83">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/c2ac3627-cad8-4b1b-ad9d-f429cbf06bc9">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/a882eabe-49fe-4051-b5e2-44c8fc0e49c7">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/efbcc3c2-082d-45a0-9a3e-6116bf98a081">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/8f38c690-f742-4920-ac3c-9669816277e1">
<img src = "https://github.com/Brindha-m/AWS_Games/assets/72887609/976907cd-c1ab-405b-9cec-8b9dcf6cd998">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/e89ded58-3202-4b63-8fc1-64fb3db36fc7">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/d72735dd-ff63-4594-b1a5-0461a334ab21">
