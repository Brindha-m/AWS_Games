# Scenario 6
> Connecting VPCs - VPC Peering
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/0cd718c5-4196-488c-a241-6fe52d13e79b">
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/d3b0f690-314f-47ab-b767-3d9e0efe4c65">
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/fe227e07-6db0-4c5f-98fc-34ae80302fc8">


- todos: Developer Server -> `Finance Server` <- Marketing Server

<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/361afb1e-740c-4a78-8ecc-75aa5109a60a">

- Now navigate to EC2
  
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/0d15502f-c34d-4289-b49c-8698a03a65d3">
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/be637697-678b-4ca9-b2dd-e74df893b0a5">
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/7cb73060-e929-4273-8610-82bd352a9acf">

-  This private IPv4 address is for the FinanceServer instance. This command checks the connection to the FinanceServer instance.
-  ip address 172.31.x.xx various on your server
-  in my case 172.31.1.197

-  <img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/b34a6eaa-38b6-4d79-a524-8a468497560f">

-  <img width="500" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/ced5e97a-5261-495a-82a8-28e082e543db">


- Click on VPC peering
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/fceeab88-592d-4da4-946c-8a4101cd75fb">
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/b78b2796-bca6-43d7-adbb-58f918cf3f39">
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/f936fe4f-0ae9-4af9-9395-da8c620a1394">
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/ab61a942-e9f2-44ed-956c-9ff8a0d86f51">

- Click on Marketing EC2 Instance id and subnet then to route table and click edit the route table and add a route.
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/660f9262-9a9f-4447-af48-514ad21892b7">

- Similarly do this for finance server
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/8e528c37-ae1c-4b30-bfd0-6ea3fb26150d">

- Click on ec2 Finance server -> security

<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/967f3bd3-7bb5-4b43-a301-bd1a5ec53d35">

<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/e71a0246-ec5f-4d58-8f16-b9e803434641">

<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/7adc2b73-b354-41f8-a4fc-ae8cf6b51c02">

- Finally,
<img width="700" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/2593616a-3cef-4570-88da-35a326f7ec05">


















