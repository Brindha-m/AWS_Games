## ML Scenario 3 - Extract Text from Docs with Amazon Textract
> ## Amazon Textract

![Image 1](https://github.com/Brindha-m/AWS_Games/assets/72887609/18052209-aeba-496f-89c3-cd9f860ed83b)
![Image 2](https://github.com/Brindha-m/AWS_Games/assets/72887609/3cd5f1f1-3619-48b2-a9f6-26f56a1488ce)
![Image 3](https://github.com/Brindha-m/AWS_Games/assets/72887609/0afa41bf-0925-4b4a-87b4-3dd0a9070d74)

### Let's Get Started

- #### Upload any image and note the extracted text.

![Image 4](https://github.com/Brindha-m/AWS_Games/assets/72887609/5087a2fb-bd90-4d64-ba4d-c25f5724d770)

#### In the Data output section:

- Choose data outputs: Forms, Tables, and Queries.
- In the Queries section text box, type: Full Name.
- Click + Add query.

![Image 5](https://github.com/Brindha-m/AWS_Games/assets/72887609/18e56bf5-6911-4a87-944a-0a1149504ad4)
![Image 6](https://github.com/Brindha-m/AWS_Games/assets/72887609/8affe79c-7cfc-4091-b3de-6daf81dcef7d)
![Image 7](https://github.com/Brindha-m/AWS_Games/assets/72887609/7f0ef6af-5521-423c-ac73-5f6939263c93)
![Image 8](https://github.com/Brindha-m/AWS_Games/assets/72887609/fc9fa607-9976-4792-b8ed-667770dcfb72)

- #### Go to Lambda:

- #### In the Layers section, click Create layer.

![Image 9](https://github.com/Brindha-m/AWS_Games/assets/72887609/f4f136ab-c00d-44c0-9d3a-437bbd3b497f)
![Image 10](https://github.com/Brindha-m/AWS_Games/assets/72887609/0359ea11-ffce-4bb0-bd82-1cd78f957e98)

- #### Name the layer as `textract-trp-layer` (trp is Third Party).
- ####  This zip contains the Textract libraries (what we get when we do pip install textract).
- ####  Zip File can be found 👉🏻 [Scenario3 - textract utils](https://github.com/Brindha-m/AWS_Games/tree/main/Machine%20Learning%20AWS/Python%20Snippets%20For%20the%20ML%20Scenarios/Scenario%203%20-%20Textract)


![Image 11](https://github.com/Brindha-m/AWS_Games/assets/72887609/dcdfdd9b-5f14-40bd-a04d-c56ed8d96ecb)
![Image 12](https://github.com/Brindha-m/AWS_Games/assets/72887609/89d2c7aa-48e0-4778-a35f-5592cfc960d6)

- #### Time to create a lambda function

![Image 13](https://github.com/Brindha-m/AWS_Games/assets/72887609/2c98477c-e983-42ab-a564-f771d04dbbc1)
![Image 14](https://github.com/Brindha-m/AWS_Games/assets/72887609/91d207a5-abb4-48c6-81ca-5d47e78c66bf)

![Image 15](https://github.com/Brindha-m/AWS_Games/assets/72887609/c860975c-5e87-482b-822b-bf4d1955c121)
![Image 16](https://github.com/Brindha-m/AWS_Games/assets/72887609/98be0e7a-8945-477c-8285-de6cc5a13387)
![Image 17](https://github.com/Brindha-m/AWS_Games/assets/72887609/130e5ccd-31aa-4fb8-98f2-29014a16e4f0)

- #### Review the code on lines 49–58. The code uses Amazon Textract AnalyzeDocument API calls. 

- #### On line 58, to replace `<Enter_Your_Feature_Type>`, type: FORMS.
- ####  Click `DEPLOY`.

![Image 18](https://github.com/Brindha-m/AWS_Games/assets/72887609/c1e9bca4-21b5-4658-bd6a-f42247c856c6)
![Image 19](https://github.com/Brindha-m/AWS_Games/assets/72887609/ca84e132-5f71-48ab-933d-8d04fdf4f024)
![Image 20](https://github.com/Brindha-m/AWS_Games/assets/72887609/77ec1b6b-e6b0-47b6-9a8a-c12dce55dd97)

- #### Click the Code tab. Scroll down to Layers.

![Image 21](https://github.com/Brindha-m/AWS_Games/assets/72887609/d864fc90-8787-4b1a-b26c-52a40a33b9ff)
![Image 22](https://github.com/Brindha-m/AWS_Games/assets/72887609/e8f1726d-d198-4ee0-a5c5-5688922cfb8c)

![Image 23](https://github.com/Brindha-m/AWS_Games/assets/72887609/c6386197-b05e-4b13-b451-d6cfa83aaefb)

- #### Add a Trigger

![Image 24](https://github.com/Brindha-m/AWS_Games/assets/72887609/4e96a2cd-f50b-4b26-bd4f-f37d09eecd42)
![Image 25](https://github.com/Brindha-m/AWS_Games/assets/72887609/825d602e-3491-4bba-b095-55976b141234)
![Image 26](https://github.com/Brindha-m/AWS_Games/assets/72887609/d6b5e7a1-9d7d-43e8-a205-c534f81ae942)
![Image 27](https://github.com/Brindha-m/AWS_Games/assets/72887609/2037a75f-1aaa-41ae-ae58-ec97f5034dcf)

![Image 28](https://github.com/Brindha-m/AWS_Games/assets/72887609/b61e7e13-aaf9-4833-8caf-6744a0c6bb50)

![Image 29](https://github.com/Brindha-m/AWS_Games/assets/72887609/20f447b0-3397-4f30-8eb2-f030b802bedd)

- #### Click Add files, and then choose the employment_form.png file that you downloaded at the beginning of the lab

![Image 30](https://github.com/Brindha-m/AWS_Games/assets/72887609/d843d14d-db73-4d54-8778-8c48814fcfd3)
![Image 31](https://github.com/Brindha-m/AWS_Games/assets/72887609/12468887-954b-4141-acec-ac2bd1ca3d84)
![Image 32](https://github.com/Brindha-m/AWS_Games/assets/72887609/3579f929-0573-415e-a094-b696b346f334)
![Image 33](https://github.com/Brindha-m/AWS_Games/assets/72887609/d9d166b9-aad1-4d74-b065-d67ac32586e2)

- #### Search for Cloudwatch, under Logs -> click Log groups.

![Image 34](https://github.com/Brindha-m/AWS_Games/assets/72887609/b913b992-f8aa-4c1c-a7d3-9884b11404d4)
![Image 35](https://github.com/Brindha-m/AWS_Games/assets/72887609/0bf64ca7-c18c-4180-8201-dd99f30e55b2)
![Image 36](https://github.com/Brindha-m/AWS_Games/assets/72887609/f4295a83-4cd7-4625-aad7-669dd978ed56)
![Image 37](https://github.com/Brindha-m/AWS_Games/assets/72887609/b45e4035-eb5c-4214-af38-2ded12eeabf5)

- #### Navigate back to the labFunction code editor window on the AWS Lambda console:

- #### Starting at line 76, type the following code:

```python
print("\nSearch Fields:")
key = "address"
fields = page.form.searchFieldsByKey(key)
for field in fields:
    print("Key: {}, Value: {}".format(field.key, field.value))
```

![Image 38](https://github.com/Brindha-m/AWS_Games/assets/72887609/0fcc285c-ba5d-4cda-82c8-2a7194699b04)
![Image 39](https://github.com/Brindha-m/AWS_Games/assets/72887609/ea1e853f-e4fd-4459-b98a-7fb7a3217fa6)
![Image 40](https://github.com/Brindha-m/AWS_Games/assets/72887609/44288348-4b84-477d-832e-b14837cf60f8)

![Image 41](https://github.com/Brindha-m/AWS_Games/assets/72887609/0d41708b-f60a-4b91-ab01-3475fa55ad53)
![Image 42](https://github.com/Brindha-m/AWS_Games/assets/72887609/12cff98b-82c4-4b35-9206-8bd05284f5fa)

- #### Reupload the image in the S3 bucket in the input folder

![Image 43](https://github.com/Brindha-m/AWS_Games/assets/72887609/88db2448-9a74-4e76-ad14-603791cd13ac)
![Image 44](https://github.com/Brindha-m/AWS_Games/assets/72887609/35e7ba0e-7872-4614-b48a-63b60e279a10)

- #### You used Address as your search field. You will see the contents matching your search field.

![Image 45](https://github.com/Brindha-m/AWS_Games/assets/72887609/508c86d9-b4d6-4b15-a9e4-1e98e38aa495)

---
## LAMBDA CODE TO EXTRACT TABLE
![Image 46](https://github.com/Brindha-m/AWS_Games/assets/72887609/1fb55805-9d4c-48e8-b216-a904627bcf39)
![Image 47](https://github.com/Brindha-m/AWS_Games/assets/72887609/ee0f0350-2c5f-4d97-a32c-4839871b95b8)



