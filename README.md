# DB_project

## Description
This project is the backend of an application that manages disaster relief supplies for those that need it. 

## Entity Relationship Diagram
Link to diagram: https://drive.google.com/file/d/1-UbNseLd5zJ4iH2_MvqiEngKwrQ9kIPz/view?usp=sharing

### Entities
* User

  A user represents an account that will interact with the application. The user has identifying details and contact information such as name, email, password, and phone number. 
   
* Role

  This represents the type of account the user has. The current three roles are client, supplier, admin. If a user is a client, the account is authorized to make purchases and requests for supplies. If the user is a supplier, the account can submit resources for sale on the application. Finally, is a user is an admin, they can look at the statistics of the application as a whole, as well as making different changes to the system, such as adding new categories or creating more roles if the need arises.
  
* Address

  An address hold the location details for other entities. The information is composed of the physical address as well as the GPS location in terms of latitud and longitud, and the Senate Region.
  
* Resource

  
* Category
* Restock Entry

### Relationships
