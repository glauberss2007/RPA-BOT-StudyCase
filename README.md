# automation-anywhere
![image](https://user-images.githubusercontent.com/22028539/120869764-8ea1af00-c56d-11eb-8848-8a74fa44dacf.png)

Automation Anywhere allows organizations to automate the processes which are performed by the humans. It is a Web-Based Management System which uses a Control Room to run the Automated Tasks. Automation Anywhere tool can automate ends to end business operations for companies.

## Robot Process Automation
![image](https://user-images.githubusercontent.com/22028539/121689760-65b47900-ca9b-11eb-8daf-073d79aeee60.png)

RPA can be used to automate repetitive tasks both in the back office and front office that require human intervention. Some common RPA examples and use cases we encounter are automation of data entry, data extraction, and invoice processing. There are additional examples of RPA use cases automating tasks in different business departments (Sales, HR, operations, etc.) and industries (banking, retail, manufacturing, etc.).

Some examples [Examples](https://research.aimultiple.com/robotic-process-automation-use-cases/#customer-service):
1. ommon business processes and activities
2. cvities in commercial functions
    - Sales
    - Customer Relationship Management
3. Activities in support functions
    - Tech Support
    - Technology
    - Finance
    - HR
    - Operations
    - Procurement
4. Industry specific activities
    - Banking
    - Insurance
    - Telecom
    - Retail
    - Manufacturing
    - Healthcare
    - Government
5. RPA applications for personal use such as digital assistants

## Requiremnt
1. Create an account to use community version: [Link to create account](https://apeople.automationanywhere.com/sso/s/login/?inst=2t)
2. Get training: [Link to official training](https://apeople.automationanywhere.com/s/group/0F96F000000l2H1SAI/training-and-certification)

## HandsOn 2
1. Cadastrar no site https://www.automationanywhere.com/
2. Realizar o acesso na ferramenta online pelo link: https://community2.cloud-2.automationanywhere.digital/#/login?next=/index
3. Crie um novo bot a partir de um script python:
    - Clique em novo:
        ![image](https://user-images.githubusercontent.com/22028539/120868055-86e00b80-c569-11eb-8ea2-f075be272549.png)
    
    - Access Regex site https://regex101.com/ and type: José da Silva, Rua Era só mais um silva, 177, Centro Esquerda da Direita, Vitória, ES, CEP 29.999-545, Brasileiro, Solteiro.

    - Search for CEP in text and get position (first and last element):
    ![image](https://user-images.githubusercontent.com/22028539/120869416-d247e900-c56c-11eb-918e-aef153fef868.png)
            
             import re 
             def findCEP(address):
                cep_express = re.search('\d{2}\.\d{3}\-\d{3}', address)
                cep = address[cep_express.span()[0]
                :
                cep_express.span()[1]]
                return cep
                
                
    - Setupo your bot:
           ![image](https://user-images.githubusercontent.com/22028539/120871896-6ddc5800-c573-11eb-9611-a74d1dcf2de4.png)

