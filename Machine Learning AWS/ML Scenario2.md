# Scenario 2 - Image and Video Analysis with Amazon Rekognition

> ## Amazon Rekognition

Explore the capabilities of Amazon Rekognition for image and video analysis.

### Image Analysis

![Image 1](https://github.com/Brindha-m/AWS_Games/assets/72887609/d6c602d4-3c9e-43b7-965e-63fb1b24a9e9)
![Image 2](https://github.com/Brindha-m/AWS_Games/assets/72887609/7960d505-5ffd-4098-8440-867a1dcb0abd)
![Image 3](https://github.com/Brindha-m/AWS_Games/assets/72887609/35642c87-d32f-4e09-a082-c7bc5687607f)

### Video Analysis

![Image 4](https://github.com/Brindha-m/AWS_Games/assets/72887609/3c3d785e-0afa-47fc-b38e-6eb90b720cdd)
![Image 5](https://github.com/Brindha-m/AWS_Games/assets/72887609/a92302f1-6603-4580-bef5-92a2a9e17a56)
![Image 6](https://github.com/Brindha-m/AWS_Games/assets/72887609/9e1b8ecc-0710-46ad-a5af-81f7f097ec44)
![Image 7](https://github.com/Brindha-m/AWS_Games/assets/72887609/5d317c85-84ad-4d06-9b78-efbb56642a1c)
![Image 8](https://github.com/Brindha-m/AWS_Games/assets/72887609/d4a11176-06be-4eeb-8457-342063bfb1d9)
![Image 9](https://github.com/Brindha-m/AWS_Games/assets/72887609/72e3a055-6aa9-43e8-bbea-db9eb6129b07)

## Let's Start

### Label Detection with Amazon Rekognition

![Image 10](https://github.com/Brindha-m/AWS_Games/assets/72887609/14a99b1a-7c8d-4b2b-901f-bf5e6b0e056f)
![Image 11](https://github.com/Brindha-m/AWS_Games/assets/72887609/cdc4a987-7b51-41db-b146-7fd2f1c044f6)

1. Click on Label Detection and upload any image to check the response.

![Image 12](https://github.com/Brindha-m/AWS_Games/assets/72887609/081caff5-bca7-44b3-b055-136ba5023a3e)
![Image 13](https://github.com/Brindha-m/AWS_Games/assets/72887609/8491bdba-b5d5-4a53-a07b-29cf4a654fcf)

2. Now, create a `Lambda Function` for further processing.

![Image 14](https://github.com/Brindha-m/AWS_Games/assets/72887609/cd1aa4bb-4ee0-4a0d-b265-d8a22fba58cf)
![Image 15](https://github.com/Brindha-m/AWS_Games/assets/72887609/0e421cd5-5024-4fcb-b9b3-a88b3a84756d)

![Image 16](https://github.com/Brindha-m/AWS_Games/assets/72887609/e886099c-e0ee-4323-99f3-29f89f50f0c8)

3. Edit the labels accordingly and click on deploy.

![Image 17](https://github.com/Brindha-m/AWS_Games/assets/72887609/219d0ddd-a2dd-418d-8de6-70f5478513ab)
![Image 18](https://github.com/Brindha-m/AWS_Games/assets/72887609/896fddf9-5779-42b0-a9cb-e36af80b4410)
![Image 19](https://github.com/Brindha-m/AWS_Games/assets/72887609/b80a5651-33b1-4da0-a915-cae83f19bade)

4. Navigate back to the code section and click Edit runtime settings.

![Image 20](https://github.com/Brindha-m/AWS_Games/assets/72887609/1d56ba3b-0cda-452b-b4d0-e7697c5d7ade)
![Image 21](https://github.com/Brindha-m/AWS_Games/assets/72887609/369391e3-f85c-4c3a-9cc4-daddd74335d9)

5. Create an S3 Bucket for storage.

![Image 22](https://github.com/Brindha-m/AWS_Games/assets/72887609/7c09e45d-1112-4910-b87a-a12dc9ced130)
![Image 23](https://github.com/Brindha-m/AWS_Games/assets/72887609/5247a791-1429-4d4b-9c17-7aaf5919fb20)
![Image 24](https://github.com/Brindha-m/AWS_Games/assets/72887609/5b421817-bfe8-4090-8313-c0c9edfe003b)
![Image 25](https://github.com/Brindha-m/AWS_Games/assets/72887609/16ef8476-0220-4bc8-ab3b-19ba5a917408)
![Image 26](https://github.com/Brindha-m/AWS_Games/assets/72887609/b43a52f5-6716-4fe4-99a5-774e7f7df819)

6. Create input and output folders.

![Image 27](https://github.com/Brindha-m/AWS_Games/assets/72887609/59134934-df42-49e3-9962-ed67855408d7)

7. Navigate to the input folder and upload new images of type .png / .jpg.

![Image 28](https://github.com/Brindha-m/AWS_Games/assets/72887609/d0099849-4b98-454c-90e9-af639bab7efd)
![Image 29](https://github.com/Brindha-m/AWS_Games/assets/72887609/ec9bf39d-adf8-4564-a0e6-ed6af48db7c3)

8. Navigate to the output folder to download the response.

![Image 30](https://github.com/Brindha-m/AWS_Games/assets/72887609/56b4c895-5e67-4664-9c9b-2c431eb48be0)
![Image 31](https://github.com/Brindha-m/AWS_Games/assets/72887609/64b1b7a2-a390-46a7-8b26-12f3ba79a110)
![Image 32](https://github.com/Brindha-m/AWS_Games/assets/72887609/79aa110a-bf78-4c13-bb12-a47a07bc7c9b)
