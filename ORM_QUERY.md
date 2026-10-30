## DJANGO models 

### Createing django model 

*Employee [id,name,department,salary,email,location,phone]*

```
our_app>models.py

from django.db import models

class Employee(models.Model):

    name = models.CharField(max_length=200) # similar to mysql name varchar(200)

    department = models.CharField(max_length=200)

    salary = models.DecimalField(max_digts=10,decimal_places=2)

    email = models.EmailField(unique=True)#email varchar(200) unique

    location = models.CharField(max_length=200)

    phone = models.CharField(max_length=15,unique=True)

```

#### make sure to run

```

> python manage.py makemigrations  

```

#### make sure to run

```
>python manage.py migrate

```


## ORM (Object Relational Mapping)

### Listing All Records

```
mysql> select * from table_name;

EG:

mysql>select * from employee;

```

*orm*

```

ModelName.objects.all()

EG

qs = Employee.objects.all()


```

### Creating | inserting Record

```

mysql> insert into table_name(col1,col2,col3) values(val1,val2,)

EG:

mysql>insert into employee(name,department,salary,email,location,phone) values
        ('hari','hr','hari@gmail.com','kakkanad',"456789")
```


```
orm  

Modelname.objects.create(col=value,col=value,col=value)

EG:

form_data={"name":"hari","department":"hr","email":"hari@gmail.com","location":"ekm","phone":"4567890"}

Employee.objects.create(
    name=form_data.get("name"),
    department=form_data.get("department"),
    email=form_data.get("email"),
    location = form_data.get("location"),
    phone=form_data.get("phone")
)


```

### Creating | inserting Record

```

mysql > select * from table_name where condition;

EG:

mysql> select * from emoployee where id = 1;

```

```

qs = Modelname.objects.get(condition)

or

qs = ModelName.objects.filter(condition)

EG:

pk = 2

qs = Employee.objects.get(id=pk)

qs= Employee.objects.filter(id=pk)

```

### Updating Record

```

mysql>update table_name set col=value,col=value where condtion

EG:

mysql>update employee set salary = 55000, department="hr" where id = 2; 

```

```
    orm :

    Modelname.objects.filter(condition).update(col=value,col=value)

    EG:
    
    pk=2

    form_data={"salary":55000,"department":"hr"}

    Emplloyee.objects.filter(id=pk).update(
                                                salary=form_data.get("salary"),
                                                department=form_data.get("department")
                                                
                                            )






```

### Delete Record

```
myql:

    mysql>delete from table_name where condition

    Eg:

    mysql>delete from employee where id = 2;

```

```
ORM:
    ModelName.objects.filter(condition).delete()

    Eg:

    pk=2

    Employee.objects.filter(id=pk).delete()
```