## Scenario 4
> Connectivity issues - VPC(Virtual Private Cloud) in EC2

<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/2d12e850-eb86-4340-8389-c62de7a403c4">

<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/01baa791-2e45-4497-9774-2e10454e3426">


<img width="500" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/daabdb4f-b0be-4712-a313-973a37496696">

<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/51419600-28f8-4b14-929c-363daff14d69">



<img width="779" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/957bb86d-d399-4b12-b7fa-cbbd9e5395f2">

- Solution

<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/ec5330b6-8f17-4968-8018-e777ad6b4d4e">
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/ef4996d2-7bc0-4df7-b6b7-d363b40b3355">

- Our servers will determine if the Web Server can connect to the DB Server, on port 3306, with Custom Source subnet 10.10.0.0/24
- Update the security group rules, and then review the Java application for a visual confirmation of an established connection. The status should change to Connected.
- The Web Server, using security group WebServerSecurityGroup, needs to connect to the DB Server, using security group DbServerSecurityGroup, over a TCP connection on port 3306
  
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/6bf16e43-4960-4cc8-aa07-8d562572ae9d">

  
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/b8a15f2c-ecbd-4b6c-8cc8-9c0dcbd50b30">
