# CAR SALES SHOWROOM:
    Car sales showroom is designed for two different types of users. Client user who wants to buy a car and an admin user who is dealing with client’s requests. User interface for both users is different from each other. Client user can be any number of users who are visiting car sales showroom website. They are allowed to view website, cars and book a test drive for any available car. Admin user is required ID and password to access the application. 
    Admin side of car sales showroom is designed to work like a web software. Admin is required to learn it in order to use it. Learning it is simple and easy, user interface for admin is self-explanatory simple to understand and follow along. It keeps you on the track and provides all useful information that you need on the same page where you are a performing task.
    At the moment I have left Admin login button present on client site just for evaluation purposes in actual requirement client user is not intended to see admin login button.  

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
    Car sales showroom is simple and easy to use. It is designed and developed to satisfy following user needs. 
###### •	Person who is interested in a particular brand and wants to see only those cars.
###### •	Person with a budget to buy a car and wants to know running cost of a car.
###### •	Person who wants to see all car features before he buys it.

## Admin user UX:
    Admin site UX is designed to be user friendly, easy to learn, interactive and dynamic. To keep admin on top of his daily jobs with client and car management.
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
