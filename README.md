# automation-anywhere

1. Cadastrar no site https://www.automationanywhere.com/
2. Realizar o acesso na ferramenta online pelo link: https://community2.cloud-2.automationanywhere.digital/#/login?next=/index
3. Crie um novo bot a partir de um script python:
    - Clique em novo:
        ![image](https://user-images.githubusercontent.com/22028539/120868055-86e00b80-c569-11eb-8ea2-f075be272549.png)
    
    - Access Regex site https://regex101.com/ and type: José da Silva, Rua Era só mais um silva, 177, Centro Esquerda da Direita, Vitória, ES, CEP 29.999-545, Brasileiro, Solteiro.

    - Import def regex to python:
    ![image](https://user-images.githubusercontent.com/22028539/120869416-d247e900-c56c-11eb-918e-aef153fef868.png)
            
             import re 
             def findCEP(address):
                cep_express = re.search('\d{2}\.\d{3}\-\d{3}', address)
                cep = address[cep_express.span()[0]
                :
                cep_express.span()[1]]
                return cep
                
                

