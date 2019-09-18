
# Digi Shop
[![Build Status](https://travis-ci.org/LukaszPlawinski/DigiShop.svg?branch=master)](https://travis-ci.org/LukaszPlawinski/DigiShop)

![alt text](https://digi-shop-ecommerce.s3.amazonaws.com/static/images/DigiShop-Image.png)

The purpose of this application was to build Full Stack eCommerce  website based around business logic used to control a centrally-owned dataset. 
An authentication mechanism has been set up and provide paid access to the site's data and/or other activities based on the dataset, 
such as the purchase of a product, edit profile, possibilty to check orders.

### Main Goals:
1.  By authenticating on the site and paying for some of its services, users can advance their own goals. 
    Before authenticating, the site makes it clear how those goals would be furthered by the site.
2.  The site owner is able to make money by providing this set of services to the users. 
    There is no way for a regular user to bypass the site's mechanisms and derive all of the value available to paid users without paying.

## UX
Website Is Designed for users who are looking for electronic products at a bargain price. Acces to all features such as :
Category Nav, Search bar Product list, Login, Basket is easy and intuitive. New ,lower prices are big, red and bold.
Customer can easy add products to basket however to purchase them login easy needed.
    
### Design

[Mockup](https://xd.adobe.com/spec/f0abd3a4-99ac-4b76-53e4-31837fb720da-869a/grid)
 Created from scratch in Adobe XD
 
### User stories:

User will be able to browse and filter products by Category or be able to find them by name. 
In Product Detail Page there are more information such as: features, color , model, description.
From there and after choosing quantity he can  add products to the cart.
After authentication through loginn he will be able to purchase them and check his old orders.

### Acceptance Criteria:

* Product should contains:
    * Name
    * Picture
    * Price
    * Old Price
    * Features
    * Color
    * Model
    * Description
*  Each User should be able to:
    * Have possibility to find/filter products:
        *  By category
        *  By searched phrase   
    * Open page with product detail
    * Add product to the basket
* Logged person should be able to:
    * Edit Profile
    * See his orders
    * Checkout in Basket
    * Pay for Order
    * Logout

## App/Page
### All Pages
    On all pages there are:
    1. Main navbar where are links to: 
        * Basket
        * Login/Register option
        * Profile - just for logged users
        * Orders - just for logged users
        * Logout - just for logged users
    2.Category Navbar contains:
        * All
        * Computing
        * Small Appliances
        * Smarthpones
        * TV & Entertainment
    
   
### Shop/Home page
   
    1. All Products are displayed (image, name and price of the recipe)
    2. User can search recipe by phrase using searching box
    3. Under search box there are social icons  leading to:
        * Instagram
        * Github
        * Linkedin
### Shop/Product Page
    1. Product name
    2. Product price
    3. Product Picture
    4. Product Old price
    5. Product Features
    6. Product model
    7. Product color
    8. Selector to choose quantity
    9. Detail Overview
### Accounts/Login Page
    After Clicking "Login" icon user is redirected to Page where he has to type in login and password.
### Accounts/Register Page
    From Login page user can choose option to register . He has to provide informations such as:
        * email 
        * username
        * password
        * confirm password
### Accounts/Edit Profile Page
    User can edit Basic informations such as:
        * name
        * last name
        * email

### Cart/ Cart Detail Page
    In that Page User sees table which contains:
        * Picture/name of the product
        * Quantity
        * Price per unit
        * Price
        * Icon to remove Item from basket
    On the right side is total basket worth and checkout button
### Orders/Order Page
    Contains Shipping Form to fill up and Stripe Payments "Pay with Card" button
    
### Orders/My Orders Page   
    Contains table with orders and order details such as:
     * Shipping name
     * Order Id
     * Order Date
     * Price
     * Payment status

## Technologies Used

1. HTML5 - Valid HTML structure
2. CSS3 - Styling for page
3. Javascript - makes website interactive
4. Popper.js - library used to manage poppers
5. Bootstrap-  mobile responsive layout, cookie alert
6. PYTHON - logic, functions
7. Django - login, searching
8. PostgreSQL- heroku Database
9. SQLite - database for Cloud9 
10. Cloud9 - cloud-based IDE in which I coded
11. Stripe - provides credit card payments
12. [Font Awsome](https://fontawesome.com/) - some icons
13. [Autoprefixer](https://autoprefixer.github.io/)- plugin which add vendor prefixes for different browsers
14. Adobe XD - to create mockup/wireframe


## Testing
* Github repository is conected with Travis CI by .travis.yml file. Everytime when repository is updated or new commit appears, Travis runs a bunch of thest and display results in Readme file under the name of the project.
* Html files were tested by [HTML VALIDATOR](https://validator.w3.org/)
* Css files were tested by [CSS Validator](https://jigsaw.w3.org/css-validator/)<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
* Javascript files were tested by [JS Validator](https://codebeautify.org/jsvalidate)
    and [jshint](https://jshint.com/)
* Python file was tested by [Python validator](https://pythonbuddy.com/)
* All inputs, links and buttons have been tested
* Tested features:
    * Register user , user exist error
    * Login user, Wrong Login, Wrong Password
    * Logout 
    * Edit Profile
    * Check Orders
    * Search product by phrase
    * Search product by category
    * Add Product to cart
    * Remove Product from cart
    * Checkout Cart
    * Pay for Order
* Website is responsive at all screen resolutions. 
* Website works on mobiles such as:
    * Iphone 6/7/8
    * Iphone 6/7/8 plus
    * Samsung galaxy s5
    * Pixel 2
* Website was tested in 'MultiBrowser' - cross-browser testing program. App works in all browsers below:
    * Chrome (Versions 75)
    * Firefox (Version 68)
    * Opera (Version 62)
    * MS Edge (Version 42)
    * Safari (Version 11)
* Stripe payment testing
```
Please use the below information to test payments.
- Card number - 4242424242424242
- CVC - Any 3 digit number.
- Expiry date - Any date in the future.
```

## Deployment

* I was using cloud 9 IDE and git bash command line which helped me to commit ale changes on "Deployment" branch.
* I installed Django and all necessary extensions
* All frameworks/extensions which have to be installed in environment are in requirements.txt file.
* Main folder contain Procfile which declaring what commands are run by application’s dynos on the Heroku platform.
* Code was pushed to github repository and later on connected with heroku pipeline.
* In heroku environment i saved variables such us: 
* Right know fully deployed website is visible on heroku server.

### How to Run Project locally for example in  Cloud9:
It have to be installed:
* Python 3.6
* Pip
* Git

1. Clone github repository
```
git clone https://github.com/JordenCI/UnicornAttractor---Milestone-4
```
2. Install required modules
```
pip3 -r requirements.txt.
```
3. Try to run your project and copy host name which should be inserted to settings.py ALLOWED_HOST
```
python3 manage.py runserver $IP:$PORT
```
4. Create a [stripe](https://stripe.com/gb) account and security keys.
5. Add 'import env' to settings.py and create env.py file which will contains variables:
* STRIPE_PUBLISHABLE
* STRIPE_SECRET
* DATABASE_URL
* SECRET_KEY
* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
6. Run Project with command:
```
python3 manage.py runserver $IP:$PORT
```


### [Live website ](https://digi-shop.herokuapp.com)
### [Github repository](https://github.com/LukaszPlawinski/DigiShop)


## Credits
* Background picture is from: [Pexels](https://data.gov.ie/)
* Products images and descriptions come from [Powercity](https://powercity.ie/)
* [Cookie alert](https://github.com/Wruczek/Bootstrap-Cookie-Alert)
* Icons and some styles comes from: [Bootstrap theme](http://bootstrap-ecommerce.com)

## Acknowledgements
Big thanks to my mentor Guido Cecilio for guiding me and showing me path to become a better Developer.
Thank you for help Code Institute team and Slack community it was great to meet you all.