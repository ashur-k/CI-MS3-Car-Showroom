
# CAR SALES SHOWROOM http://car-sales-showroom.herokuapp.com/index:
    Car sales showroom is designed for two different types of users. Client user who wants to buy a car and an admin user who is dealing with client’s requests. 
    User interface for both users is different from each other. Client user can be any number of users who are visiting car sales showroom website.
     They are allowed to view website, cars and book a test drive for any available car. Admin user is required ID and password to access the application. 
    Admin side of car sales showroom is designed to work like a web software. Admin is required to learn it in order to use it. Learning it is simple and easy, user 
    interface for admin is self-explanatory simple to understand and follow along. It keeps you on the track and provides all useful information that you
     need on the same page where you are a performing task. At the moment I have left Admin login button present on client site just for evaluation purposes in 
     actual requirement client user is not intended to see admin login button.  

## Client services:
###### •	Slide showing hero section.
###### •	Dynamic buttons to select car, provided with tooltips.
###### •	Special car offers.
###### •	User friendly photo gallery.
###### •	Responsive web which user can view on different types of modern smart device.
###### •	Responsive navigation bar that stays fixed on large screen sizes and becomes side navigation menu on small and medium screen size devices.
###### •	Procedure of booking test drive.
###### •	User can view full car specifications.

## Admin services:
###### •	Fully device responsive and completely dynamic in nature web application. 
###### •	Admin login and sign out interface and ability to create a new admin user.
###### •	Interactive and dynamic in design admin dashboard works as admin control centre. 
###### •	Fixed side navigation bar, it hides on small and medium size screens and get operational with help of menu button provided at top. 
###### •	Service to create, read, update, delete and search car records.
###### •	Client management service where admin can book test drive appointments and search clients.

## Client user UX:
    Car sales showroom is simple and easy to use. It is designed and
    developed to satisfy following user needs. 
###### •	Person who is interested in a particular brand and wants to see only those cars.
###### •	Person with a budget to buy a car and wants to know running cost of a car.
###### •	Person who wants to see all car features before he buys it.

## Admin user UX:
    Admin site UX is designed to be user friendly, easy to learn, interactive and dynamic. 
    To keep admin on top of his daily jobs with client and car management.
###### •	Admin can have secure login system to keep admin side separated and only accessible to amin user.
###### •	Admin can view client requests, and book car test drive appointments.
###### •	Admin can create, read, update and delete cars data that clients can view on their end.
###### •	Admin can create new user if he needs to grant access to his/her assistant.
###### •	Admin can search cars and clients to speed up his job.

## Working of application:
## Client site:
    Car sales showroom website is responsive to small, medium and large screen sizes. 
    Its top is a slide show where client is presented with 3 car slides. Next is car 
    selections area which I have separately explained in detail at the end of paragraph 
    with heading, how selections area works. After selection area client website has special 
    offers to advertise different cars. Special offer cars can lead client straight to book 
    test drive for car or view its specifications. After special car offers there are social 
    media links to keep clients connected to social activities of car sales showroom, then car 
    photo gallery where client can view photographs, on click these photos are opened as full-size 
    image centred on screen. End section that contain about us information and contact form. At the 
    moment contact us form is not operational; Its functionoing will be implemented in 
    later version of car sales shoroom.

### How selections area works?
    On homepage under slides show user is presented with number of cars make in a selection dropdown 
    button, user is required to select a car make. Once user selects a car make, it enables user to 
    view cars in that make by clicking find cars button provided there. Similarly, user can select 
    car models which shows models available in the make that user has selected. 
    
    Selection buttons are dynamic, on selection they change interactively, to inform user about 
    choices user has made. Tooltips are added if some users required additional help.

    On either car make or car model selection, if cars are available, user can view cars 
    by clicking find car button. Car view page is going to present user with images and car 
    summaries of car make/model user has requested to view. All cars display three dotted 
    button which gives more information about that car. In end of each car section, user is
    provided with two buttons, to view full specifications of car or if user wishes to book 
    a car test drive.    

    If user book’s a test drive, then booking request will be submitted to 
    admin dash board. Admin will see user requests on first come first serve basis and from there
    admin can contact user to make arrangements for a test drive. 

## Admin site
    Admin homepage is divided in two sections fixed side navigation menu and admin dashboard. 
    Side menu is responsive to different screen sizes, it disappears if application is viewed on 
    medium or smaller screens. Appearance can be controlled with button provided at fixed top. 
    Admin dashboard is designed with an idea that when user book for test drive it will end up on 
    admin dashboard and from there the admin is able to book a test drive appointment with the 
    potential buyer. If buyer is happy with the test drive then he/she can proceed to buy the car.

## Admin dashboard
###### 1.	Admin dashboard is divided in two section information about cars and information about client information.

### Information about cars:
###### •	In car information section admin is provided with the car image and its basic details. Then admin is provided with two buttons, first is to see full car details which shows all information about the car and second is sell car button which gives amin a form to add buyer information. If admin enters and submits the information in buyer form, it will remove car data from available cars to sold cars. Users on client side won’t be able to see any sold cars.
###### •	Admin dashboard is dynamic it keeps track of sold cars which other clients already have requested to book a test drive. To keep admin updated sold cars are displayed with red label at top informing that ‘car is sold’. Admin can view full details which are included with buyer information. Sold cars are presented with different button that gives an option to admin to book a different car for client. 

### Information about clients:
###### •	Information about clients provides admin with details about client including what is best date and time to contact, and if client gives any instructions message.
###### •	At the top of client section, admin is provided with an appointment booking form inside a collapsible, to book an appointment. Admin is not going to be allowed to book an appointment on same date and time. If admin is doing, it will be informed with a flash message ‘that there is already an appointment on this date and time’. Admin can update appointment date and time simply by re-booking appointment with help of same collapsible form. 
###### •	Admin is provided with two buttons in client section, first to delete clients in case if client has requested to delete his/her information or admin not want to keep client records. There is safety modal message implemented for admin when deleting clients in case if it is an accidental click. 
###### •	Second button will remove client from dashboard but in this case, admin can see the removed client again on view all client and can also re-add the client back to admin dashboard from there. Admin is provided with this option to only keep potential buyer to view on admin dashboard. 
###### •	Admin is provided with blinking message that keeps reminding admin that client is still needed to contact. 
###### •	In an update version, admin dashboard will be implemented with feature where admin can see other test drive bookings for the car in car section. It will help admin to organise bookings in better way.

## FIXED SIDE NAVIGATION MENU FEATURES:
###### 1.	Admin Login menu.
###### 2.	Add new car to database.
###### 3.	Manage cars menu, option available in the menu are add car make/model, edit existing car information and view sold cars. 
###### 4.	Manage client’s menu, option available in this menu are book test drive for client and view all clients.
###### 5.	Search bar where admin can search car make, model or registration number.

### Admin Login menu:
###### •	Admin login menu has two options logout and add new user in case if admin wishes to add another admin user.

### Add new car: 
###### •	Add new car will provide interactive and dynamic experience to admin. It creates page headings with selections admin is making. For example, if admin choses to add car to Audi make, then page title and heading are going to show adding car to Audi. In case if there is no model available in car make that admin is trying to add car, then admin will be redirected to add model page with flash message about the error. 
###### •	Once Admin adds car registration and selects car model in next step server is going to check if there is no entry of that registration number in database. Registration numbers in car database collections are planned to be unique and if admin registration number is already in database then admin will be informed about the error.
###### •	If there is no error then admin is required to add car specifications, including car image URL. There is no facility provided of adding these details automatically. In an upgrade version of car sales showroom, I am planning to add feature that admin is able to fetch all that information from an external API.
###### •	In end of process when admin submits all car specifications to database, admin will be redirected to admin dashboard with message that all information is added successfully.  
###### •	If for some reason admins stop that process in middle, then admin will be requested to finish or end that session. 

### Manage Cars:
###### •	In first option “Add Car Make / Model” admin can add car make or car model to database. Admin is not allowed to duplicate these entries. There are collections in database of each car makes and car models. Purpose of these collections is to fill in dropdown and selection menu. There uniqueness is required to make dropdown and selection boxes working properly. At the moment Admin cannot delete or update car make/model. This feature will be added in next version of car sales showroom. 
###### •	Second option, edit existing car info gives admin ability to update car information if there is any mistake made while adding car information. Admin is able to change car registration number and If admin changes car registration number then it will first check for its uniqueness. Second it will check if there are any clients interested in the car for which admin is updating registration number. If there are then correspondingly registration number will be change in client database collections. 
###### •	Third option, view all cars admin can see all cars in database on this template. Information is displayed in alphabetical order of car make name. Admin can delete the car record and view full information about car. In update version I am going to plan how an effective pagination option can be implemented on this page. Idea of seeing all cars in order to find one specific car is not considered user friendly. Admin is provided with feature of car search that is explained under search input box heading.

### Manage Cleints:
###### •	Admin can book car test drive from his end. Admin is required to give car registration number. After this admin is going to be provided back with car image, information about other test drive appointments for the car, if there are any, and car test drive booking form to add test drive booking in database.
###### •	Admin can View all clients it works similar to admin dashboard but here admin can search clients with their name, phone number or email address. And information on client administration page is provided in alphabetic order using clients name.
###### •	Third option, sold cars admin can see information about sold car and its buyer. Admin can also delete the record of sold cars. At the moment admin cannot update sold cars record. I am implementing this feature in update version of cars sale showroom. 

### Search input box: 
###### •	If there are 100s of car then looking for a one particular difficult job to do. Admin can search car registration number; car make or car model with help of search input provided in side navigation. If result is searched, admin will see a web page with all numbers of result. Each result will have car image its summary and four operation buttons. Update, view, sell and delete car to perform that particular operation with car registration number. All of these buttons are functional.
###### •	If admin is entering registration number of sold car in search input, then returning page is going to be all information about that sold car..  
###### •	At the moment search is required to follow same pattern of small and capital letters as values are saved in database. In update version of cars sales showroom, admin won’t be required follow this rule.
###### •	Client is not given feature for updating and setting special up car offers for client site home page. It is left to implement for later application version. Temporarily three cars are randomly selected to display on client site special car offers section.

## Testing:
    I have performed wide measures of testing on application before and after hosting to 
    make sure that user data is not breaking. I did find errors and I have corrected them. 
    Following are the errors that I would like to mention:

###### •	Car updating and add car was using same name for session variable reg_num. This was crashing application if adding car is in process and the same time admin chooses to update a car from navigations.
###### •	In the process of updating registration number my session variables were conflicting with each other. Both session variables were named ‘reg_num’ resulting the application to crash. In order to prevent this issue, update function session variable was named differently. This fix caused a corresponding error where updating form fields in car update-delete page were not filling up with data. This was due to not updating all entries of ‘reg_num’, although once all entries were updated, application started to work properly without any further crashes. 
###### •	To make car sales showroom behaves interactive and dynamic, multiple URLS routes are used which serves different values to their URL function. These URLS hold variables and the values of these variables comes from different HTML templates or are redirected from other associated routing functions. Thorough testing is performed, during and after the implementation of the logic. To check functions and operations of application are not breaking or crashing, web templates are served with correct data values and links or buttons in application are directing correctly.
###### •	In testing, an unexpected logical error was caught at admin end of application. If admin deletes any sold car data, and there is another client who is interested in that same car, then admin won’t be able to view car information that the other client is interested in. The reason for this problem is car registration number which is present in client database collections but deleted from admin car collections. Consequently, if admin wants to view information about that car registration number server will generate empty HTML template. To resolve this issue car sales showroom was implemented with logic that in that particular case admin get reminded with the help of flash message about the deletion he performed earlier. “Admin has removed car information from all client and car databases.” 
###### •	Car sales showroom is tested on different browsers and on different screen sizes to make sure if user readability or designed stability is not compromised.
###### •	In testing phase, it was discovered that navigation bar on client side is going out of its position. This problem was coming from admin css file. The link of admin.style.css file was provided in head tag of client side to provide styling to admin login file. To fix this problem classes in styling of admin login file were included to css styling of client side css file. Link of admin_style.css file was removed from client-side head tag.
###### •	After implementing fully functional side navigation some of flash messages were disappearing behind the side navigation. To fix problem these flash messages were give new html tags and css styling.
###### •	There are minor form validation issues which at the moment are left to deal with in upgrade version. Although materializecss validations classes are applied to form fields and they are working.
###### •	Feature of view all car is a last-minute update to car sales showroom. In testing phase, it occurred that admin need to view all cars. In case if admin is trying to find a car and he has no way to recall it then there is one option left for admin to view all cars.
###### •	In testing it occurred that if admin is updating car make, application will not detect if there is no model available in car make that admin is trying to update. This will lead to add car details without car model. This can cause faults in functioning and behaviour of application especially client side. This error is removed, now If admin selects car make which has no model admin is going to displayed with error message and instructions to follow to first add car model to make admin is selecting.
###### •	Admin car updating was only performing updating registration number of car client is requesting. Details about car image, make, model etc if were updated there were not update on client collections. This error is corrected now if admin made any update on car collections then same updating will be performed on client data.
###### •	There were spellings errors which are corrected and on some web pages there was no application of materialize css grid classes. For this reason, design of those pages was losing its structure on small and medium screen sizes. Errors are corrected.
###### •	At the moment if car is deleted admin can still make or update appointment for the car only from admin dashboard. This is going to stay like this for now but in future release of car sales showroom if car that client has requested is deleted, then, admin will be required to add new car details for client before booking an appointment.  For now, admin is given clear indications that data for the car, that admin is dealing with is deleted. If admin clicks sell car button or car information button, admin will be given error message, this is explained above in detail.    

## Deployment:
All requirements to run and execute project are included in requirements.txt. Following command is required to install all requirements to workspace:
###### • - pip3 install -r requirements.tx.t 
Database name, password, PORT address, IP address and secret key for sessions are hidden in env.py and added to config vars in heroku settings. These details are not provided for public view.
To view implemented and running version of site please visit, http://car-sales-showroom.herokuapp.com/index. User name and password for admin login are not provided for GitHub public view though they can be provided on request. For assesment these details are provided to code institute student care team.
Site is hosted using Heroku platform services. GitHub repository is linked to Heroku app, commits to GitHub are automatically committed to deployed site on heroku platform. Following steps were taken to deploy application and link both platforms:
###### 1.	Create a Heroku app, go on Heroku.com. Give app name which should be unique and choose a region which should be closest one to you for quicker delivery.
###### 2.	Run following commands before deployment:
###### a.	pip3 freeze –local > requirements.txt, this command will create requirements file, this file is required by heroku to install requirements before deploying project. 
###### b.	echo web: python app.py > Procfile this file will create Procfile on workspace. Procfile is required by Heroku to know entry point for project.
###### c.	Commit workspace to git hub repository. Following commands are required to make a commit to git hub:
###### i.	Git add .
###### ii.	Git commit -m “final commit”
###### iii.	Git push.
###### 3.	Automatic deployment method was used to deploy project on heroku and following steps were taken for deployment.
###### a.	From deploy tab on heroku web page, in deployment method section, option GitHub connect to GitHub was selected.
###### b.	Then search repository to connect to details were provided which includes ac-count details and repository name.
###### c.	When repo was fount button below connect to this app was clicked.
###### d.	Next from settings following config vars and their values were provided to heroku
###### i.	Database name, password, 
###### ii.	PORT address, 
###### iii.	IP address 
###### iv.	secret key for sessions
###### 4.	In last on GitHub deploy page in automatic deploys click enable automatic deploys from master was selected.
###### 5.	At deployment time everything was successful in first attempt there was no error. Video provided by Tim, tutor at code institute was used to follow these steps.
### Deployments during development for testing:
#### To test site during developmentdebug setting were set to true, to debug errors during development.
All codes are written using gitpod, workspace were included template provided by code institute. Python3 web hosting service was used for testing site during development process. During the process most of the time site is tested on google chrome browser and occasionally on Firefox, opera and edge browser. After deployment application is tested on different browsers including all major browsers. On mobile site is tested on Samsung internet browser.  Site is also tested on apple phones, laptop screen size 17’’, desktop monitors, 32’’, 27’’ Samsung tablet. On iPhone it is recommended not to use phone’s default browser.   
Database is created using mongodb ATLAS service. Mongodb is document based database which use collections instead of tables. Mongodb provides unique ids, for its collection. In comparison to sequel databases mongodb works faster. Though it’s always recommended choose database which serves development requirements in best way. Car registration numbers are used as unique ids to perform CRUD operations on cars data. Logic to keep uniqueness of registration number is developed using python flask server-side codes. 

## Technologies Used:
###### •	HTMI5 to implement website project.
###### •	CSS3 to implement website project.
###### •	JavaScript codes provided by materializecss.
###### •	Python3, flask framework and its libraries.
###### •	Mongodb database  
###### •	GIT POD online web workspace for HTML & CSS coding.
###### •	Git Hub hosting services and data storage services.
###### •	Heroku to host project online
###### •	Google Chrome to run GIT POD workspace for development process.
###### •	Google chrome Git extension button to log into Git Pod workspace.
###### •	Google Chrome Developer tools.
###### •	Firefox browser latest version for testing purposes.
###### •	Opera latest version for testing purposes.
###### •	EDGE latest version for testing purposes.
###### •	Internet explorer latest version for testing purposes.
###### •	Materializecss to implement website.
###### •	Font awesome free version.
###### •	Google icons.
###### •	Balsamiq Mock-ups 3 for designing wireframes
## Credits
## Content:
    Content on client application is taken from Cazoo website (https://www.cazoo.co.uk/). The content about car specifications is only a representation of information to explain functioning of application. I am advised by friends not update actual data on hosted project in case if I am not sure about legal obligations.   
    Although in a future update version of car sales showroom car specifications are going to be directly taken from an API and once I have permission to use that API then my legal obligation barriers are going to be taken away by API providers.
    Media:
###### •	Pictures are downloaded from Unsplash.com and then they are saved on my flicker account and from there I was adding images URL address to database which then I have displayed on my templates. There are few images that were taken from google searched websites.
###### •	Logo and some other images are used taken from undraw (https://undraw.co/search).
## Acknowledgements:
    I want to say thanks to following youtubers how have shared and explained using flask and mongodb in development.
###### •	Hitesh Choudhary for explaining Mongodb and flask concepts.
###### •	Anthony from pretty printed who explains concepts of flask and particularly how to implement blue prints.
###### •	Tech with Tim for blue prints in flask.
###### •	Luke Peters for building login system particular hashing password.
###### •	Travesy Media for materializecss.
###### •	Special thanks to code institute tutors for helping troubleshooting problems.
###### •	My mentor Dick Vlaanderen who particularly has advised me and emotionally encouraged me.
###### •	Special thanks to code institute tutor Tim, helped me to crack errors and provided me with his vidoe toutorials for project deployments. 
