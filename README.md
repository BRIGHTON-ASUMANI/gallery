# __Gallery__
Gallery is a simple application that allows users to click on an image of their choice and their suscription

### __prerequisites__
The app runs on django==1.11 and works with both bootstrap3 and bootstrap4
For more details and istallations please check out the requirements.txt and runtime.txt

### __installation__
1. install a virtualenv in your root folder
2. To start a django app you have to install django e.g ***python3.6 -m pip install django==1.11***
3. Then start a django project  -  django-admin startproject projectname
4. Inside the django project start a django-app -  django-admin startapp appname
5. for more info please read the django documentation

### __Running Tests__
> after passing in diferrent functions in this application, one has to write tests
> some of the functions include:

1. save_image() - Save an image to the database.
2. delete_image() - Delete image from the database.
3. update_image() - Update image in the database.
4. get_image_by_id(id) - Allows us to get an image using its ID.
5. search_image(category) - Allows us to search for an image using its category.
6. filter_by_location(location) - Allows us to filter images by the location.
***note tests have to be assigned in the tests.py module***

### __Technologies Used__
1. posgresql
2. django==1.11
3. python
4. bootstrap3 and 4
5. javascript

### __Deployment to Heroku__
> for deployment in heroku please click on this link and follow the steps very keenly [deployment](https://www.codementor.io/jamesezechukwu/how-to-deploy-django-app-on-heroku-dtsee04d4)


### __Authors__
***BRIGHTON ASUMANI***
* For anyproblem please contact at asumanibrighton@gmail.com

### __Licence__
This project is licensed under the MIT License - see the LICENSE.md file for details
