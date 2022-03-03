# LQN
It is a project created to execute the proposed technical test    
    
 
 You must run the following command to build all the project containers:    
    
 $ make build    
you should generate the initial Django migrations, for them execute the following command    
    
 $ make migrate    
## Run project    
 To run the project you must execute the following command    
    
 $ make up    
> If you have problems connecting Django with Postgres, you should run the command: make restart CONTAINER=django    
 ## Other commands    
    
 1. **Create a new app:** make startapp NAME=example    
 2. **Generate migrations:** make migrate    
 3. **Create a superuser:** make superuser  
  
## Test Environment  
  
In the following url you will be able to carry out tests in a secure environment, with the following superuser:  
[Inventory - Test Environment URL](http://159.223.105.137:8000/admin/)  
  
 - **User:** root  
 - **Password:** Hogar2020

If you want to check it out, access the graphi explorer here: (http://159.223.105.137:8000/explore)

The service should be available in the URL: (http://159.223.105.137:8000/graphql)
## Sort packages in the requirements.txt file

First you need to add the package to the requirements.txt file, then you run the **make build** command.
Finally, so that the packages are ordered and with their version established in the requirements.txt file, you must execute the following command.

    $ make get-requirements
