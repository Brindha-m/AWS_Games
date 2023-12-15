## Let's understand the Subnet Concepts.

> ### Subnet - Dividing a Large network into **Smaller Networks** is called **Subnetting.**

> ### CIDR -  Classless Inter-Domain Routing --> Total No of Network Bits

> ### Bits -> 1. Network Bits, 2. Host Bits

 ## Example 1 - Class A
  Given

 ```
  CIDR = (/8)
  IP ADDRESS = 1-126
  DEFAULT SUBNET = 255.0.0.0

 ```
![image](https://github.com/Brindha-m/AWS_Games/assets/72887609/449611b1-e541-4b56-8488-6a2f4d40e336)

<br>

 ## Example 2 - Class B
  Given

 ```
  CIDR = (/16)
  IP ADDRESS =  128-191 
  DEFAULT SUBNET = 255.255.0.0

 ```
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/d40d7673-1482-4c49-8438-6dff34dc18a6">


<br>

## Example 3
## Given IP -> **192.168.10.0/26**

#### Find 
1. `Default Subnet`
2. `Find No of Networks`
3. `Find No of IP Address on each network`
4. `Find No of Hosts in each network`

Lets Start..

### 1. Finding Subnet given that cidr - 26
   
   ![image](https://github.com/Brindha-m/AWS_Games/assets/72887609/f3ad372c-4168-4249-a6c3-449073dceea7)

   This the default subnet.. in last 8 bits --> **128 + 64 = 192**

   <img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/f06858d2-731e-410b-b0ec-a2f38784975c">

<br>

### 2. Find No of Networks -  `2^n` Here n is No of bits borrowed from Host bits.

NOTE: The formula to calculate the number of networks is given by `2^n`, where `n` represents the number of bits borrowed from host bits.

So, the 2^n => 2^2 = 4
<img width="613" alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/ffe4c06f-92ac-4c65-8081-c9610f672227">

Therefore, you can form **4 networks** using this configuration.

<br>

### 3. Find No of IP Address on each network -  `2^n` Here n is No of Host Bits.

So, Here n = 6. 
2^n => 2^6 = 64

 Resulting in **64 IP addresses** on each network.


<br>

### 3. Find No of Host on each network -  `2^n - 2` Here n is No of Host Bits.

So, Here n = 6.
2^n -2 => 2^6 - 2 => 64 - 2 = 62

 Resulting in **62 hosts** on each network.

<br>

## Put together,

### Note:

**Network ID:** Start Address
**Broadcast ID:** End Address



### IP Addressing Table

| No of Network | Network ID    |     Host Address                | Broadcast ID       |
|---------------|---------------|---------------------------------|--------------------|
| 1             | 192.168.10.0  | 192.168.10.1 to 192.168.10.62   | 192.168.10.63      |
| 2             | 192.168.10.64 | 192.168.10.65 to 192.168.10.126 | 192.168.10.127     |
| 3             | 192.168.10.128| 192.168.10.129 to 192.168.10.190| 192.168.10.191     |
| 4             | 192.168.10.192| 192.168.10.193 to 192.168.10.254| 192.168.10.255     |

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/29afd9f8-d537-4f50-bcc2-0e05513b1fc6">

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/8faf82fb-0829-42a1-9e50-5b8b5bb1e824">

#### Website CIDR visualizer - https://cidr.xyz/
