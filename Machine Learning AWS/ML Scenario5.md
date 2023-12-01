## ML Scenario 5
> ## Introduction to Generative Models
> ### Generative - LLM (Large Language Model)

![Image 1](https://github.com/Brindha-m/AWS_Games/assets/72887609/d48ccb17-bb03-4552-9fd6-8abffba78450)
![Image 2](https://github.com/Brindha-m/AWS_Games/assets/72887609/fc55d1e3-3a2a-4c7b-8968-fbebdae9065f)
![Image 3](https://github.com/Brindha-m/AWS_Games/assets/72887609/f098066b-21f6-44a1-9bd3-f89f3f534294)

![Image 4](https://github.com/Brindha-m/AWS_Games/assets/72887609/88ef0c1f-c1e5-4d44-bc15-4e780b32b854)
![Image 5](https://github.com/Brindha-m/AWS_Games/assets/72887609/39e6320b-d076-4ee9-8e04-8ce273ce8675)

![Image 6](https://github.com/Brindha-m/AWS_Games/assets/72887609/43f491bd-c88e-46c7-85d2-5dedd3a3632f)

![Image 7](https://github.com/Brindha-m/AWS_Games/assets/72887609/3f38768d-a4eb-47e9-b660-5c79569b1d53)

![Image 8](https://github.com/Brindha-m/AWS_Games/assets/72887609/36a0a159-351c-4607-9995-24715303b741)
![Image 9](https://github.com/Brindha-m/AWS_Games/assets/72887609/c7e0845c-1577-43fe-bf03-918887974d79)

- ## Services to be used here..
  
| AWS Service             | Purpose                                      |
|-------------------------|----------------------------------------------|
| **Amazon SageMaker**    | Build, Train, and Deploy Machine Learning Models |
| **Amazon S3**           | Scalable Storage in the Cloud                |
| **Amazon Lambda**    | Run code without thinking about servers     |
|**Amazon CloudFront**   | Global Content Delivery Network              |
|**Amazon API Gateway** | Build, Deploy and Manage APIs                |
  
## Let's Get our Hands-on

![Image 10](https://github.com/Brindha-m/AWS_Games/assets/72887609/c8074da6-989c-465c-9e05-7ea13f3441b6)

### Model Sizes:
  * ### Falcon-7b: It is a **7 billion** parameter model trained on 1.5 trillion tokens.
  * ### Falcon-40B: It is a **40 billion** parameter model trained on 1 trillion tokens.

![Image 11](https://github.com/Brindha-m/AWS_Games/assets/72887609/a6e1eb8b-cb8a-4d01-ad48-29f3c1b865c7)

![Image 12](https://github.com/Brindha-m/AWS_Games/assets/72887609/f81c64fb-5a46-4268-9171-d006209e547e)

![Image 13](https://github.com/Brindha-m/AWS_Games/assets/72887609/bfee7d35-1984-43cb-a94e-24126be50f20)

![Image 14](https://github.com/Brindha-m/AWS_Games/assets/72887609/1afe80c0-f3d5-4836-ac5b-16275f426377)

![Image 15]("https://github.com/Brindha-m/AWS_Games/assets/72887609/44fd49ee-c250-48ec-afda-91686643e368)

- Pov -> Your s3 Bucket Contents can be found 👉🏻[Scenario 5 - Generative AI]()

![Image 16](https://github.com/Brindha-m/AWS_Games/assets/72887609/3b8deadc-6ba2-4f32-bb40-b34d12838c72)

- ### To view the list of all Amazon Simple Storage Service (Amazon S3) buckets, in the terminal run the following command:

    ```bash
    aws s3 ls
    ```

- ### To download the lab code, run the following command (replace `<Replace with lab-code bucket name>` with the actual bucket name):

    ```bash
    aws s3 sync s3://<Replace with lab-code bucket name> .
    ```

- #### ⚠️ Make sure to include the space and period `" . "` at the end of the command.


![Image 17](https://github.com/Brindha-m/AWS_Games/assets/72887609/a0d14445-6782-4188-87be-c3f9a9db8339)

- #### Open the Notebook file, wait for the kernel to be idle ( make sure to check in the bottom kernel xBusy)
  
![Image18](https://github.com/Brindha-m/AWS_Games/assets/72887609/c9188fa8-c0db-4717-b134-bcd5b1c2d4b0")

- #### Run Each cells in the notebook

![cells](https://github.com/Brindha-m/AWS_Games/assets/72887609/e8648681-47b0-4f64-9d0c-77aee1b0e957)

![cells](https://github.com/Brindha-m/AWS_Games/assets/72887609/a33f2c22-b0df-4240-8d8e-9f3b6acaf121)

![cells](https://github.com/Brindha-m/AWS_Games/assets/72887609/7b2f83ea-8e04-4fd1-9d4a-c1f4c4ee6e4e)

![cells](https://github.com/Brindha-m/AWS_Games/assets/72887609/c94964bd-fe07-48be-8628-ab86237a734d)

![cells](https://github.com/Brindha-m/AWS_Games/assets/72887609/f0c5f593-a53a-4f8b-bef4-1de70d1e2401)

![cells](https://github.com/Brindha-m/AWS_Games/assets/72887609/2ebf3688-0876-4770-8ad4-d7c7dfb33da4)

- #### File -> Logout and In Amazon SageMaker Studio, copy the endpoint
![SageMaker](https://github.com/Brindha-m/AWS_Games/assets/72887609/0259e42e-36b1-4c11-85a1-387c1843b6c1)

![SageMaker](https://github.com/Brindha-m/AWS_Games/assets/72887609/70f8b471-0c6a-4fbb-b706-79a92c89bfee)

- ###  `Endpoint ---> hf-llm-falcon-7b-instruct-bf16-2023-12-01-14-57-53-790 `

![awsml](https://github.com/Brindha-m/AWS_Games/assets/72887609/2459743d-b3b4-44b8-9b3a-4e6c9f757ba9)

![awsml](https://github.com/Brindha-m/AWS_Games/assets/72887609/d55a798c-d23d-4fa4-abc2-b45c753fc5b7)

![awsml](https://github.com/Brindha-m/AWS_Games/assets/72887609/8dc7396d-f342-44a6-a598-ca2106fe9ce3)

![awsml](https://github.com/Brindha-m/AWS_Games/assets/72887609/f558c280-031f-4748-bb3e-ad2e60d41d9a)

![awsml](https://github.com/Brindha-m/AWS_Games/assets/72887609/65b5b32c-2b00-4477-be78-a0680181feb6)

- #### Navigate to s3 and check the bucket and its contents
![awsml](https://github.com/Brindha-m/AWS_Games/assets/72887609/c2e5e415-759f-407a-bd89-c4eae8ed8466)

![awsml](https://github.com/Brindha-m/AWS_Games/assets/72887609/3c2e4146-1477-4d31-9473-1eb4fdc148cf)

- #### Now Navigate to Cloud Front

![awsml](https://github.com/Brindha-m/AWS_Games/assets/72887609/5f6888e4-769e-4340-89f2-4f3f3c4b1333)

![awsml]("https://github.com/Brindha-m/AWS_Games/assets/72887609/6c58413a-1eb6-4de0-8d95-22e68f75b46a)

![awsml](https://github.com/Brindha-m/AWS_Games/assets/72887609/fe7d2d95-40de-4504-8a29-84e9c66175ea)

![awsml](https://github.com/Brindha-m/AWS_Games/assets/72887609/c0aae734-cfbc-4a70-9e44-9b2463a9f734)

- ### ` https://dymy4w7ib93uj.cloudfront.net/ `
- #### This application requires an API Gateway URL

![awsml](https://github.com/Brindha-m/AWS_Games/assets/72887609/235c7e13-71fe-43f3-9b24-86f1986db64c)

![awsml](https://github.com/Brindha-m/AWS_Games/assets/72887609/2c63b388-e595-44df-897e-e1b65cdcfcb9)

![awsml](https://github.com/Brindha-m/AWS_Games/assets/72887609/e2054df3-5bc4-4036-b63f-7982ab2f2df4)

![awsml](https://github.com/Brindha-m/AWS_Games/assets/72887609/0254bdb3-13d2-4535-a36e-c32af8c3faa9)

![awsml](https://github.com/Brindha-m/AWS_Games/assets/72887609/5228d617-f526-4b7d-85e9-600382e10d98)
