# Learn AWS through Games

> Cloud Quest - [https://cloudquest.skillbuilder.aws/](https://cloudquest.skillbuilder.aws/)

> Road map - [https://coggle.it/diagram/ZULSKicP9Medu2Xc/t/aws](https://coggle.it/diagram/ZULSKicP9Medu2Xc/t/aws)

## Agent Brindha to continue...

![Agent Brindha](https://github.com/Brindha-m/AWS_Games/assets/72887609/1440deaa-473b-4648-946c-dc2802e7375a)

![Wave Size](https://github.com/Brindha-m/AWS_Games/assets/72887609/a94f663e-1fd4-41a7-aa68-622ca532d242)

## Scenario 1. Cloud Essentials

### Webpage to display the wave size
> #### - 👉🏻 more reliable (realtime/fast/live/more accurate) and
> #### - 👉🏻 resilient (fault tolerance - hardware failures ie. storing data across multiple nodes)

<br> 

## 🚀 Let's Start Our Cloud Journey

* 🌐 For a Static Website, migrate to Amazon Simple Storage Service (Amazon S3) bucket.
* 🛡️ As an AWS user you can have upto **100** Buckets.
* 📦 Maximum Size of the buckets is **5TB**.
* 🚀 Max size of buckets in S3 is 16GB that can be added through AWS console. But if larger size, use AWS CLI(Command Line Interface).

![Wave Size Image 1](https://github.com/Brindha-m/AWS_Games/assets/72887609/03ecaadf-45fb-44cf-a677-aec3582e2fb9)
![Wave Size Image 2](https://github.com/Brindha-m/AWS_Games/assets/72887609/cb35b1fe-d6df-415d-b2c5-8dfa674e7007)

## S3 Policies

1. Resource-based Policies - (Bucket Policies)
2. User Policies (IAM users)
3. Bucket policies file are limited to 20 KB in size [The policy.json file].

![S3 Policies](https://github.com/Brindha-m/AWS_Games/assets/72887609/29235d51-f1ae-45d3-8b27-92ee3885f0fc)

- IAM Policies (Identity and Access Management)

![IAM Policies](https://github.com/Brindha-m/AWS_Games/assets/72887609/2cbaacc4-5e0b-4b90-9c9f-05d46abc2cfb)

![Wave Size IAM Policies](https://github.com/Brindha-m/AWS_Games/assets/72887609/9f5e1eab-3323-4535-840d-dc18b8d90552)

### Let's get our Hands-on🧑🏻‍💻

- Search for S3 in AWS Console and Create a bucket in S3

![Create S3 Bucket](https://github.com/Brindha-m/AWS_Games/assets/72887609/1860e7a2-3a65-4403-85f1-efb4c54989cb)

### Name the bucket (ie. `staticwebsite-s3`) and make some setting for our bucket as follows

![Bucket Settings](https://github.com/Brindha-m/AWS_Games/assets/72887609/c7438a11-4289-4521-9d7b-41ba980661f7)
![Bucket Settings 2](https://github.com/Brindha-m/AWS_Games/assets/72887609/02651219-77ab-4249-aee6-f7e1af988db3)
![Bucket Settings 3](https://github.com/Brindha-m/AWS_Games/assets/72887609/10085ec8-752e-4f74-9fc7-beae0bf16909)
![Bucket Settings 4](https://github.com/Brindha-m/AWS_Games/assets/72887609/bbd3ec36-10ee-4b43-b0a2-dcd31352e18b)

- The contents to be uploaded in our S3 bucket can be found in the `Cloud partitioner -> Static Website utils` folder of this repo.

![Bucket Contents](https://github.com/Brindha-m/AWS_Games/assets/72887609/5abc449b-ab91-42db-abb8-67db1fb661c1)

- Click on edit bucket policy and paste the content that is in the `policy.json` file which can be found in your bucket and click save change at the bottom.

![Edit Bucket Policy](https://github.com/Brindha-m/AWS_Games/assets/72887609/5d6ff8fc-5c9f-420f-b6df-b9d99b56990c)
![Bucket Policy](https://github.com/Brindha-m/AWS_Games/assets/72887609/010589eb-ba7a-44f5-b814-3da2f1c9be3a)

- Now navigate to the properties tab, scroll down and click on Edit in Static webpage hosting

![Static Website Hosting](https://github.com/Brindha-m/AWS_Games/assets/72887609/bd7763ba-629c-4797-86d0-523ea348f774)
![Static Website Hosting 2](https://github.com/Brindha-m/AWS_Games/assets/72887609/c766920f-7f7a-4a0e-849f-2f130daf31c5)
![Static Website Hosting 3](https://github.com/Brindha-m/AWS_Games/assets/72887609/4e72a290-72da-4c96-8e6c-8d39bc63cd84)
![Static Website Hosting 4](https://github.com/Brindha-m/AWS_Games/assets/72887609/c8b072a1-8e29-419f-bc06-159efd34c82d)

- Under Bucket website endpoint, click the copy icon to copy your bucket website endpoint.

> [http://staticwebsite-s3.s3-website-us-east-1.amazonaws.com](http://staticwebsite-s3.s3-website-us-east-1.amazonaws.com)

![Static Website Endpoint](https://github.com/Brindha-m/AWS_Games/assets/72887609/33aa3d8a-97e9-476f-af3d-a109311e68cd)
