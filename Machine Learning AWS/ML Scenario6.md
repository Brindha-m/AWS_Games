## ML Scenario 6
> ## Fine-Tuning LLM ON Amazon SageMaker

![image](https://github.com/Brindha-m/AWS_Games/assets/72887609/5b75cc84-3c09-4408-af80-366db8ff443c)
![image](https://github.com/Brindha-m/AWS_Games/assets/72887609/937299bb-1dc6-468e-8a4b-ec1e98b45365)
![image](https://github.com/Brindha-m/AWS_Games/assets/72887609/17903a2b-23a9-463e-b501-ea4a0187003a)
![image](https://github.com/Brindha-m/AWS_Games/assets/72887609/9ffb7b40-2834-47aa-902f-6c0d6ab6bc25)


## Let's Get Started

![image](https://github.com/Brindha-m/AWS_Games/assets/72887609/86d0a832-802c-4b6a-9902-a0813c9ca2e3)


### Create the 2 buckets, One with the .html file and other with .zip file. Files can be found here 👉🏻[Scenario 6 Util]()

![image](https://github.com/Brindha-m/AWS_Games/assets/72887609/2dc90dcf-c143-4ea9-a5e0-9059fddedb2f)

![image](https://github.com/Brindha-m/AWS_Games/assets/72887609/e656174e-c04d-4beb-b071-3086c5f2acf7)

![image](https://github.com/Brindha-m/AWS_Games/assets/72887609/d7515297-6255-451e-a7d9-322aa958d6b2)

![image](https://github.com/Brindha-m/AWS_Games/assets/72887609/4af8e67e-8cc8-45c2-9b9c-f5c50cf17b09)

![](https://github.com/Brindha-m/AWS_Games/assets/72887609/1dda32a1-8138-4e89-ab98-7a221b0ecb12)

![](https://github.com/Brindha-m/AWS_Games/assets/72887609/9b4870dd-463b-4054-ab26-02cc851873d8)

- #### In the terminal window
   
   - #### `cd SageMaker` - To change directory
   - #### ` aws s3 cp <Replace with lab-code bucket URI> . ` To download the lab code
   - #### Be sure to include the space and period  " . " at the end of the command.
   - #### `unzip lab-codes.zip` - To unzip the file, run:
   - #### click the refresh icon.
   - #### Open (double-click) the lab-notebook.ipynp file.

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/18e42363-40bb-4c57-9547-2ac5ef115520">
<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/c5f8f04f-448f-416a-b94f-03e02b36c593">

### Run Every cells in the Notebook

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/070e6eef-17bc-4faa-b7b1-fa8f492b6e3b">

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/b82775d9-69ac-40ab-be1b-4de1427d8357">

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/ef59f8a5-1606-49b8-80fe-3968969e2e35">

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/06a18c3c-a31b-4666-90c0-081954c95e5a">

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/d6bf7ae4-7e2a-4f95-825b-cda03ff92107">

### To finetune the LLM, you need to define a trainer. First, define a training arguments.

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/f4902fa9-cc0d-420e-920c-81992bbb48c5">

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/02f613ce-6ab3-4bfd-8d40-16f3916b9800">

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/886d7d4f-8e6a-452f-b06a-a2883d025cd7">

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/e649439e-b669-48f4-a85c-b5557f4134e9">

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/06643e4c-b9c3-43ff-8fb9-fa1f5bd6cd67">


<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/2fea2229-dcfc-4aa2-8312-5a2034912aaf">

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/ed0ae05b-f6a8-4390-a4f5-7ab7c0a66aa2">

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/06821415-029e-407a-b19d-cb39af84f10b">

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/19270a53-5836-4054-a737-5f85a4ec7ec9">

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/48ced8b5-e925-4902-8e17-936feddbf7cd">

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/12b19c97-ab91-4ce9-9d7a-598d1ca5ff2a">

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/881a01e8-9b1d-4fb1-97e3-c62b2b9f5dc9">

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/64b26005-5c4f-462a-81ed-1c3dbdb00f5c">

<img alt="image" src="https://github.com/Brindha-m/AWS_Games/assets/72887609/a0779394-f593-4567-91cc-e2312e06f900">

