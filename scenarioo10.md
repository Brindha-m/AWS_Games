# Scenario 10
> EFS - Elastic File Storage system
> Serverless, Fully elastic file storage

<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/9fd3d3ed-2a31-4bab-ba08-bf007cc85ed6">

<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/e588a1fe-83aa-471b-ade7-a291633077c3">

<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/43ec6c63-9f07-43c4-a278-0e5507f9b40c">

<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/d4143662-26b5-437c-a54b-bf2d90f24a1d">

<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/fbbfba13-5d0e-436b-a40b-5a9852556265">

<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/fd46e9a0-5ea7-49c7-bb66-874824cb55e8">

- ## Lets get started, Note you have 3 servers running on 3 different AZ's.

<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/8136b02b-538b-4e95-8d34-de13310de952">
 
- ## Create a Security Group
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/5b2f5139-4a1b-4634-96de-d349aed3a25e">
 
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/75869eae-9294-4dc7-8d51-dcff7f33efd4">

<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/143a2e01-e876-426b-a71a-0e9b73e1bfcc">

<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/03ae776b-4f64-4c08-9249-f291e9776b6a">

<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/73c4b3cf-3b8a-4ded-b60d-7b7653abdd64">

<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/0a38aa27-43c2-4b71-902f-4db4d324ebe3">
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/13a9f930-2d7c-4aeb-8c26-efadafb5505b">

<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/811a27ce-e3be-48aa-b68e-c1ab2c0a83db">

- ## For now remove these 2 AZ's
  
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/37f8bda6-0af0-429a-9824-c7e8af79ca34">
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/a5def598-8e78-4c3c-a89f-bb59f8d6d529">

- ## Do nothing and skip to next steps
  
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/ee5f121e-7a69-443f-ad9c-5d213898cc3b">
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/90d10c1a-a952-42d2-81b6-8e82929b6271">

<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/c0f28a9b-37cb-45d0-b3e7-a132f9b25249">
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/5796e962-ca55-4bf2-8df4-ba517529a0fc">

- ## NOW Navigate to EC2 instance
  

<img width="596" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/97553094-5957-40ed-8ab9-0c9f38555570">


- ## Terminal of Cat Server 1
  
  1. sudo -i
 
  2. sudo yum install -y amazon-efs-utils
 
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/f8bacc1e-870a-4ce7-bad3-277be97e6f22">

 3. mkdir data
 
 4. ls
 5. sudo mount -t efs -o tls fs-0bff6359d94cd7562:/ data
 6. cd data
 7. sudo bash -c "cat >> efs-1-setup.log"
 8. then type, efs-1 mounted in site A
 9. cat efs-1-setup.log
     
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/1a3badbd-147c-4766-bc86-ac102e7e6a2d">

- ## Now navigate to networks tab in the EFS
  
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/19c7eda8-3c4d-426a-becf-f3bd80295642">
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/cd6b2e2d-7d76-4079-ba61-196bccd81550">


- ## And when you run the server 3 from the EC2
  
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/916cee9b-ce75-4538-a726-6e7b57317356">

- ## FINALLY, THE FILES ARE ACCESSIBLE FROM EC2 INSTANCE THROUGH EFS
