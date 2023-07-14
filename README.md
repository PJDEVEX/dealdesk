# **DealDesk-CRM**

![Responsive screenshot showing site on different screen sizes](https://res.cloudinary.com/pjdevex/image/upload/v1689275971/static/dealdesk-crm/readme/deal_desk_crm_lui0pw.webp)

The DealDesk-CRM is CRM platform for SMEs who wants thrive in thier business through successful Customer Relationship Management.

# **Executive Summary**
In today's competitive business landscape, customer relationship management (CRM) is essential for success. According to Salesforce, CRM not only enhances customer experience but also boosts personalized marketing efforts, leading to remarkable increases in customer satisfaction and retention rates of up to 25% and 30% respectively. Furthermore, Aberdeen Group highlights that CRM drives efficiency by automating repetitive tasks, resulting in a remarkable 41% revenue increase. It also empowers businesses with better data management, leading to informed decision-making, a 65% improvement in sales quota attainment, and a 36% increase in win rates.

Despite these immense benefits, many small and medium-sized enterprises (SMEs) face barriers to CRM adoption. Cost, lack of expertise, and resistance to change are among the challenges highlighted by surveys conducted by Capterra and Software Advice.

Introducing DealDesk-CRM, an affordable, easy-to-use CRM solution tailored specifically to address the needs of SMEs. Our cloud-based platform eliminates cost concerns, ensuring that businesses of all sizes can benefit from CRM's transformative power. With DealDesk|CRM, you can effortlessly manage customer data, automate repetitive tasks, and enjoy the rewards of improved customer satisfaction, revenue growth, and informed decision-making.

Built on the Django Python framework, DealDesk|CRM boasts a modular design, scalability, and easy maintenance. Our cutting-edge technology ensures seamless integration and exceptional performance, empowering your business to thrive in today's digital landscape.


visit [DealDesk|CRM](https://dealdesk-crm.herokuapp.com/)

# **Planning Phase**
## **Strategy** 

**Vision:**
DealDesk|CRM empowers SMEs'

**Buyer Persona:**
Name: Samantha

**Job Title:** Owner of a Small Business

**Background:** Samantha started her business a few years ago and has been successful in growing it, but she struggles to manage customer relationships and keep track of her sales team's progress. She is aware of the benefits of a CRM system, but the cost and implementation process has deterred her from pursuing it.

**Pain Points:** Samantha is frustrated with the inefficiency of her current sales and marketing processes. Further, Samantha faces barriers to CRM adoption such as cost, lack of expertise, and resistance to change. She needs a system that can be tailored to her specific business requirements without breaking the bank.

**Goals:** Samantha's main goal is to improve her customer experience and increase sales efficiency. She wants to personalize her marketing efforts and retain her customers, but also automate repetitive tasks to free up her sales team's time to focus on more valuable tasks.

How DealDesk|CRM Can Help: DealDesk|CRM is a cloud-based CRM solution that addresses the challenges of implementing CRM in small businesses like Samantha's. It is a cost-effective solution that is tailor-made to meet the specific requirements of her business. With DealDesk|CRM, Samantha can manage her data effectively, leading to personalized marketing efforts, increased customer satisfaction, and retention. It also automates repetitive tasks, resulting in a 41% revenue increase and better data management, enabling informed decision-making. DealDesk|CRM can help Samantha improve her sales team's performance, resulting in a 65% improvement in sales quota attainment and a 36% increase in win rates.


**Brand Identity**
Brand Essence: Empowerment

**Brand Promise:** Empowering SMEs to achieve more with a cost-effective, tailored CRM solution.

**Brand Personality:** Innovative, helpful, trustworthy, approachable.

**Tagline:** "Empowering SME Sales"

**Visual Identity:**
Logo: The logo should reflect the brand essence of empowerment and convey a sense of innovation, approachability, and trustworthiness. The logo could feature an abstract icon that represents the idea of "empowerment" and a modern, clean font for the brand name.

Color Palette: The color palette should be modern and vibrant, reflecting the innovative and approachable nature of the brand. Colors like blue & pink could work well.

Typography: The typography should be modern and clean, with a font that is easy to read and conveys a sense of approachability and trustworthiness.

**Messaging:**
Elevator Pitch: "At DealDesk|CRM, we understand the challenges that small and medium businesses face when it comes to implementing a CRM system. That's why we've created a cost-effective, tailored solution that empowers SMEs to manage their customer data effectively and automate repetitive tasks. With DealDesk|CRM, you can improve your customer experience, increase efficiency, and make more informed decisions based on reliable data."

Website: The website should feature clear and concise messaging that highlights the benefits of using DealDesk|CRM. The messaging should be tailored to small business owners like Samantha, addressing their pain points and highlighting how DealDesk|CRM can help them achieve their goals.

Social Media: Social media messaging should focus on thought leadership and helpful tips for small business owners. The messaging should showcase the innovative and approachable nature of the brand, with a focus on empowering SMEs to achieve more.

Advertising: Advertising messaging should focus on the brand promise of empowering SMEs to achieve more with a cost-effective, tailored CRM solution. The messaging should be tailored to small business owners like Samantha, addressing their pain points and highlighting how DealDesk|CRM can help them achieve their goals.

Overall, the brand identity should be consistent across all touchpoints, conveying the brand promise of empowering SMEs to achieve more and showcasing the innovative, trustworthy, and approachable nature of the brand.


### **Platform's Aims:**
**User Goals**
- Streamline sales and marketing processes.
- Increase customer satisfaction and retention.
- Improve sales team performance and efficiency.
- To have an easy-to-use CRM solution.

**Business Owner Goals**
- Introduce a Cost-effective CRM solution
- Tailored to specific business requirements
- Easy-to-use and user adoption
- Improved customer experience and sales efficiency
- Well-informed Decision Making


### Opportunities:
The was an extended range of features during the brainstorming session for platform. A feasibility table has been used to narrow it down and prioritize the scope of the intended strategy. 

Opportunity | Importance | Viability/Feasibility
---|---|---
Dashboard | 5 |5
Dashboard - KPIs |5 | 5
Client database | 5 | 5
Project database | 5 | 5
Lead management |5 | 5
Sales Pipeline | 5 | 5
Task Management | 5 | 5
Mobile CRM | 5 | 5
Team management | 5 | 3
Sales Training protal| 4 | 3
Customer service supprt | 4 | 1 
Integrate a chatbot | 2 | 1
Internal messaging systme |2 | 1
Email integration | 4 | 3
Notification system |3 | 2
User log in | 5 | 5
API for news updates | 2 | 1
Integrate marketing actvities | 4 | 2
KAM analysis | 5 | 1
Totals | 89 | 70 

Based on The above Viability/Feasibility scores, where features with higher scores are considered more viable and feasible to implement. 

## **Scope**

Given the uneven scores provided above, there will inevitably be some compromises and trade-offs to be made. However, I anticipate that additional trade-offs will be necessary in the future due to the project's time constraints.

I have further divided this table into three categories to help prioritize the order of importance and clarify the MVP required to launch as a basic proof of concept while meeting the above objective. 

These three categories are:-
* UX efforts **must** address these:
    * Dashboard
    * Dashboard - KPIs
    * Client database
    * Project database
    * Lead management
    * Sales Pipeline
    * Task Management
    * Restricted User log in
  
* UX efforts **should** accommodate these:
    * Team management
    * Sales Training portal
    * Email integration
    * Integrate marketing activities
  
* **Unwise** use of time to address there:
    * Customer service support
    * Integrate a chatbot
    * Internal messaging system
    * Notification system
    * API for news updates
    * KAM analysis
  
## **Structure**   
- User Authentication: The system requires users to authenticate using a username and password to access restricted areas of the site.
- Dashboard: Upon login, users are presented with a dashboard view, providing an overview of key metrics and important information.
- Client Management: Authorized users can perform Create, Read, Update, and Delete (CRUD) operations on client records, enabling effective management and communication.
- Project/Lead Management: Users have the ability to manage projects and leads, including tracking progress.
- Task Manager: The system includes a task management module that allows users to create, assign, and track tasks, ensuring efficient project execution.
- Logout: When a user decides to leave the site, they can log out to ensure secure access and protect sensitive information.

### **User Stories:**  
  
Based on 10 epics, the user storeis were created for the proejct. Pls visit the the [Kanbam Board](https://github.com/PJDEVEX/dealdesk/blob/c64ffb02cc7f26afd2ee0918f45f83d8cc4152e1/README.md#L239) for details.


## **Skeleton**
### **Wireframes:**
* [DealDesk|CRM](https://res.cloudinary.com/pjdevex/image/upload/v1689275971/static/dealdesk-crm/readme/deal_desk_crm_lui0pw.webp)  

The provided image represents the initial user interface (UI) design of the intended web platform. However, as the project progresses and undergoes iterations, there may be deviations in the final look and feel of the application. These changes are expected as part of the natural evolution and refinement process to ensure the best user experience and alignment with project goals. The wireframe serves as a starting point and visual representation of the intended layout and functionality, but it should be understood that the final product may differ in certain aspects based on user feedback, design considerations, and technical implementation.

### **Database Schema**
I have designed an initial database schema for the project, which can be visualized through the Entity-Relationship Model (ERD) accessible [here](https://drive.google.com/file/d/1wSQkzBoeSgtjjhWu1O8MICGSJ3kA3AvN/view?usp=sharing).

The database schema comprises four models, with a total of seven tables. The models are as follows:

1. **Client Model:** This model represents the clients and includes the "Client" table, which stores information about the clients.

2. **Project Model:** The project model consists of three tables: "Project," "Brand," and "Category." The "Project" table stores details about the projects, while the "Brand" table stores information related to different brands associated with the projects. The "Category" table categorizes the projects based on specific categories.

3. **Team Model:** The team model includes two tables: "Manager" and "SAR" (Sales Account Responsible). The "Manager" table contains data about the managers, and the "SAR" table stores information about the Sales Account Responsibles.

4. **Task Model:** The task model represents the tasks and includes the "Task" table, which stores details of the tasks associated with the projects.

This database schema provides a structured approach for organizing and managing data related to clients, projects, brands, categories, team members, and tasks. It forms the foundation for efficient data storage and retrieval within the project.

## **Surface**
### **Color scheme:**
Considering the purpose and target audience of the platform, I have opted for a simple and professional color scheme to align with the official nature of the application. The primary colors chosen for the brand are #004AAD and #FF5757.

By utilizing these colors consistently throughout the platform's interface, we aim to create a visually cohesive and aesthetically pleasing experience for users. The selected colors reflect the intended tone and convey a sense of professionalism and reliability.

### **Typography**:
In the context of DealDesk|CRM, the "Public Sans" font family was chosen for its diverse range of font weights and styles. This font family provides various options, including:

- Font Weight 300 (Italic)
- Font Weight 400 (Regular)
- Font Weight 500 (Regular)
- Font Weight 600 (Regular)
- Font Weight 700 (Regular)
- Font Weight 300 (Italic)
- Font Weight 400 (Italic)
- Font Weight 500 (Italic)
- Font Weight 600 (Italic)
- Font Weight 700 (Italic)

By utilizing these different font weights and styles, I could achieve a high level of flexibility and versatility in the design, enabling you to create visually appealing typography that suits the project's requirements of professional touch and enhances the overall user experience.

# **Agile Development Process**
During the development of the project, I utilized [Github Issues](https://github.com/PJDEVEX/dealdesk/issues) to effectively manage and track epics, issues/user stories, and bugs. However, I must acknowledge that due to the complexity and novel nature of the project, as well as my evolving skills as a developer, I inadvertently overlooked some aspects of the agile development process.

While I strived to adhere to industry best practices, the challenges encountered and the learning curve I experienced contributed to certain deviations from a strictly agile approach. Nonetheless, it is important to highlight the dedication and effort I put into delivering a high-quality software product.

Recognizing the significance of the agile development methodology, I acknowledge the value it brings in terms of iterative development, collaboration, and adaptability. Moving forward, I am committed to further enhancing my understanding and implementation of agile principles to ensure more comprehensive project management and efficient development cycles.

By addressing the identified gaps in my agile development process, I aim to continually improve my skills and deliver even more successful projects in the future.
  
# **Features**
## **Site Navigation**
### **Navbar**
The platform incorporates two types of navigation bars to enhance user experience and facilitate efficient navigation:

 - **Side navbar:** This navigation bar is designed to provide easy access to different sections and features of the platform. It is typically located on the side of the screen and offers a comprehensive menu of options. The content displayed in the side navbar is dynamic and varies based on the user's authorization level and permissions. Users with appropriate authorization can view and access relevant sections and functionalities through this sidebar.

 ![Sidenav](https://res.cloudinary.com/pjdevex/image/upload/v1689296044/static/dealdesk-crm/readme/Dashboard/nav-side_authorised_fmyahq.png)
 ![Sidenav](https://res.cloudinary.com/pjdevex/image/upload/v1689296044/static/dealdesk-crm/readme/Dashboard/landing_page_nktmyv.png)

- **Toggle navbar for small screens:** To optimize the user experience on smaller screens, such as mobile devices or tablets, a toggle navbar is implemented. This navigation bar is specifically tailored to accommodate limited screen space and offers a condensed menu. Similar to the side navbar, the content displayed in the toggle navbar is also determined based on the user's authorization. It provides a simplified and accessible menu for users to navigate through the platform seamlessly.

![Togglenav](https://res.cloudinary.com/pjdevex/image/upload/v1689296044/static/dealdesk-crm/readme/Dashboard/nav-side_authorised_fmyahq.png)
![Togglenav](https://res.cloudinary.com/pjdevex/image/upload/v1689296044/static/dealdesk-crm/readme/Dashboard/nav_toggle_unauthorised_zxkbcb.png)
The utilization of these two types of navbars ensures that users can easily explore and interact with the platform's functionalities while adhering to their specific authorization privileges.



#### ***Logo:***
The logo of DealDesk|CRM is designed around three core pillars: managing complex sales deals, nurturing high-value customer relationships, and embracing future technologies. The logo symbolizes the specialized function of Deal Desk teams, who play a crucial role in facilitating and optimizing sales negotiations. The concept of CRM is represented, highlighting the strategic importance of effectively managing customer interactions to drive business growth. The block icon in the logo signifies the empowerment of SME sales in the modern business landscape, emphasizing the platform's ability to support small and medium-sized enterprises in navigating the evolving sales environment. Overall, the logo reflects the essence of DealDesk|CRM as a solution that combines deal management, customer relationship management, and technological innovation to enable business success.

**Logo Square**
  
  ![Site Logo Square](https://res.cloudinary.com/pjdevex/image/upload/v1689184170/static/dealdesk_crm_logo/dd_sq_dark_vt0sqk.webp)

**Logo rectangular**
  
  ![Site Logo rectangular](https://res.cloudinary.com/pjdevex/image/upload/v1689184170/static/dealdesk_crm_logo/dd_hr_light_qo3739.webp)

**Logo favicon**
  
  ![Site Logo favicon](https://res.cloudinary.com/pjdevex/image/upload/v1687544628/static/dealdesk_crm_logo/dd-fav_cqmbp3.webp)
  
#### ***Signup:***
Since it is a secured, private platform user shall be proved with the user name and password to login to the site
![Siginup](https://res.cloudinary.com/pjdevex/image/upload/v1689296044/static/dealdesk-crm/readme/Dashboard/signup_u2dytf.png).

**NOTE** 
For evaluation purposes, I will provide the necessary user credentials along with my submission form. These credentials will grant access to the platform and allow the examiner to review the functionality and user experience.
  
#### ***Signin:***
As stated earlier user shall be proved with login details as signup is dissabled:     
![login](https://res.cloudinary.com/pjdevex/image/upload/v1689296045/static/dealdesk-crm/readme/Dashboard/singin_dmb5va.png)  
  
#### ***Signout:***
* blow is the signout.
    ![signout](https://res.cloudinary.com/pjdevex/image/upload/v1689296978/static/dealdesk-crm/readme/Dashboard/signout_igw3d8.png)  
  

  
### **Home Page:**
Below is the hompage/ index page for the site,
![Homepage](https://res.cloudinary.com/pjdevex/image/upload/v1689296044/static/dealdesk-crm/readme/Dashboard/landing_page_nktmyv.png) 

#### ***Dashboard:***
Upon successful user authentication, the platform directs the user to the dashboard, strategically designed with the busy business professional in mind. The dashboard serves as a centralized hub, offering a concise and intuitive overview of key business metrics and performance indicators. This thoughtful design approach enables users to swiftly grasp critical insights and make informed decisions, optimizing their efficiency and productivity. By presenting relevant information in a visually appealing and easily digestible manner, the dashboard empowers users to quickly assess the state of their business, enhancing their ability to navigate and prioritize tasks effectively. 
![dashboard](https://res.cloudinary.com/pjdevex/image/upload/v1689296044/static/dealdesk-crm/readme/Dashboard/dashboard_wyfhtv.png)  

#### ***Taks Manger:***
Continuing with the user-centric approach and considering the needs of busy professionals, the next vital component is the Task Manager. This feature takes into account the importance of prioritization and efficient task management in the daily workflow. With its comprehensive CRUD (Create, Read, Update, Delete) functionality, the Task Manager enables users to seamlessly create, view, modify, and remove tasks as needed. By providing a centralized platform to organize and monitor their daily priorities, professionals can effectively plan, allocate resources, and stay on top of their tasks. The Task Manager module enhances productivity and streamlines workflow management, ensuring that users can efficiently handle their responsibilities and achieve their objectives in a timely manner.
  
![Taskmanager-list](https://res.cloudinary.com/pjdevex/image/upload/v1689296043/static/dealdesk-crm/readme/Task%20Manager/task_list_view_zv0vs6.png)
![Taskmanager-filter](https://res.cloudinary.com/pjdevex/image/upload/v1689296043/static/dealdesk-crm/readme/Task%20Manager/task_filter_t7w8rn.png)
![Taskmanager-new](https://res.cloudinary.com/pjdevex/image/upload/v1689296043/static/dealdesk-crm/readme/Task%20Manager/task_new_wezrjg.png)
![Taskmanager-edit](https://res.cloudinary.com/pjdevex/image/upload/v1689296043/static/dealdesk-crm/readme/Task%20Manager/task_edit_uipdvz.png)
![Taskmanager-delete](https://res.cloudinary.com/pjdevex/image/upload/v1689296043/static/dealdesk-crm/readme/Task%20Manager/task_delete_ei4qej.png)
![Taskmanager-pagination](https://res.cloudinary.com/pjdevex/image/upload/v1689296043/static/dealdesk-crm/readme/Task%20Manager/taks_list_pagination_uwcxpm.png)


### ***Projects:***
Moving forward, we have the Projects/Leads module, which encapsulates the core objectives that the team strives to achieve. This module serves as a central hub where users can access and manage their projects and leads. It offers a comprehensive range of functionalities, including list view with filtering and search capabilities, detailed project/lead views, the ability to create new projects/leads, make edits, and perform deletions when necessary. Additionally, the module incorporates pagination functionality to ensure efficient navigation and presentation of project/lead records. By leveraging these features, users can effectively track, organize, and manipulate project/lead data, enabling seamless collaboration and driving the team towards successful outcomes.

![Project-list](https://res.cloudinary.com/pjdevex/image/upload/v1689296045/static/dealdesk-crm/readme/Projects/projects_leadlist_details_ro2v3z.png)
![Project-filter](https://res.cloudinary.com/pjdevex/image/upload/v1689296045/static/dealdesk-crm/readme/Projects/projects_leadlist_filter_avjikx.png)
![Project-detail](https://res.cloudinary.com/pjdevex/image/upload/v1689296045/static/dealdesk-crm/readme/Projects/projects_leadlist_details_ro2v3z.png)
![Project-new](https://res.cloudinary.com/pjdevex/image/upload/v1689296045/static/dealdesk-crm/readme/Projects/projects_leadlist_new_xkergc.png)
![Project-edit](https://res.cloudinary.com/pjdevex/image/upload/v1689296045/static/dealdesk-crm/readme/Projects/projects_leadlist_edit_vatbck.png)
![Project-delete](https://res.cloudinary.com/pjdevex/image/upload/v1689296045/static/dealdesk-crm/readme/Projects/projects_leadlist_delete_ooyqso.png)
![Project-pagination](https://res.cloudinary.com/pjdevex/image/upload/v1689296045/static/dealdesk-crm/readme/Projects/projects_leadlist_pagination_xittik.png)

### ***Client:***
At the core of the entire process lies the Client module, serving as the foundational element of the business. Ensuring the availability of up-to-date and accurate client details is of utmost importance for sustainable growth and success. With a strong focus on the essential CRUD (Create, Read, Update, Delete) functionalities, the Client model empowers users to efficiently manage client-related information.

Within the Client view, users are provided with a comprehensive list showcasing client records, complete with advanced filtering and search capabilities. This enables quick and seamless navigation, empowering users to locate specific clients based on customized criteria. Moreover, a detailed view is available to offer a holistic perspective on individual clients, presenting a comprehensive overview of their profiles.

To facilitate seamless interactions, the module supports the creation of new client entries, allowing users to capture and store essential information efficiently. Additionally, the ability to edit existing client details empowers users to keep client information up-to-date, ensuring accuracy and relevance. When necessary, the module also offers the option to remove unwanted client records through a deletion functionality, maintaining data integrity and decluttering the system.

By leveraging these comprehensive features, users can harness the power of the Client module to build and nurture strong, long-lasting client relationships, thereby driving business growth and success.

![Client-list](https://res.cloudinary.com/pjdevex/image/upload/v1689296045/static/dealdesk-crm/readme/Clients/clients_list_view_p0lzoe.png)
![Client-filter](https://res.cloudinary.com/pjdevex/image/upload/v1689296046/static/dealdesk-crm/readme/Clients/client_list_filter_up6vtz.png)
![Client-detail](https://res.cloudinary.com/pjdevex/image/upload/v1689296046/static/dealdesk-crm/readme/Clients/client_list_details_whk85u.png)
![Client-new](https://res.cloudinary.com/pjdevex/image/upload/v1689296046/static/dealdesk-crm/readme/Clients/client_list_new_pomlvy.png)
![Client-edit](https://res.cloudinary.com/pjdevex/image/upload/v1689296046/static/dealdesk-crm/readme/Clients/client_list_edit_h1vwd2.png)
![Client-delete](https://res.cloudinary.com/pjdevex/image/upload/v1689296046/static/dealdesk-crm/readme/Clients/client_list_delete_hlnul6.png)
![Client-pagination](https://res.cloudinary.com/pjdevex/image/upload/v1689296046/static/dealdesk-crm/readme/Clients/client_list_pagination_a3hxxx.png)
  


# **Future development**
I have identified future developments in two primary areas: strategic and tactical/functional.

**Tactical/Functional Developments:**
* Error Pages - Implementing error pages such as 404 and 500 to provide informative and user-friendly error messages when encountering page or server errors.

* Task List Enhancements:
- Adding a date range selection option to filter tasks based on their status within a specific timeframe.
- Enhancing task visibility by displaying the completion date of projects at a glance.
- Introducing filtering options under the headings bar for improved task organization and navigation.
- Implementing an undo button functionality to allow users to revert accidental task deletions.
- Enabling the ability to recall mistakenly deleted tasks, providing an additional layer of data recovery.
- Allowing users to add new individuals to the "Assigned to" tab when creating a new task, facilitating efficient task assignment.
- Automating the task numbering system to automatically assign the next available task number when creating new tasks.
- Delete authorisation
- Differentiate the views and CRUD based on the user groups
- clear button to filters in all list views
- Possiblity of using filter & search as option (let user to decide in the view)

*  Clients:
- Enhancing the client form to include auto-fill functionality or a dropdown menu for country code selection, ensuring accurate telephone number entry.
- Resolving any existing bugs related to field validation in the Clients' details navigation page.
- Exploring the possibility of retrieving deleted client items for data recovery purposes.

**Strategic Future Developments:** 

*  Mail Integration - Integrating email functionality within the DealDesk | CRM platform to facilitate seamless communication and collaboration.
*  KAM (Key Account Management) Analysis Module - Implementing a dedicated module to analyze and manage key accounts, enabling strategic decision-making and relationship development.
*  Product Module - Introducing a product module to effectively manage and track product information, inventory, and sales-related data.
* Quotations and Proposal Module - Developing a module to streamline the quotation and proposal creation process, enhancing efficiency and accuracy.
* Integration of AI/ML - Leveraging the power of Artificial Intelligence (AI) and Machine Learning (ML) technologies to enhance the capabilities and intelligence of the DealDesk | CRM platform.

These future developments will drive continuous improvement, address user needs, and propel the platform towards enhanced functionality, efficiency, and strategic alignment with business objectives.


# **Testing Phase**
I have included testing details during and post-development in a separate document called [TESTING](https://drive.google.com/file/d/1KoXrVdEqYAWf58OLwIiqa_TuJPrzzXzA/view?usp=sharing).

# **Deployment**
The final Deployed site can be found [here](https://jobs-a-gooden.herokuapp.com/)
I have included details of my initial deployment in a separate document called [DEPLOYMENT.md](DEPLOYMENT.md).

# **Technologies used**
* Python
  * The packages installed for the is project can be found in [the requirements.txt](requirements.txt)
* Django
  * Django was used as the python framework in the project.
  * Django all auth was used to handle user authentication and related tasks i.e. sign in, sign up, sign out.
* Heroku
  * Used to deploy the page and make it publicly available.
* Heroku PostgreSQL
  * Used for the database during development and in deployment.
* HTML
  * HTML was the base language used to layout the skeleton of all templates.
* CSS
  * Custom CSS used to style the page and make the appearance look a little more unique.
* Javascript
  * I have used Javascript throughout to manipulate the DOM and communicate to the backend to create, read, update, and delete data from the database.
* Jinja
  * Jinja was the templating language used in order to implement the views.py logic and models.py data into a template so it could be displayed to the user.
* Bootstrap 5.1.3
  * Used to style HTML, CSS, minor javascript.
* Font awesome
  * All icons throughout the page.
* Canva
  * Creating the logo
* Googl Font
  * For font types and styling
* cdnjs.com 
  * content delivery network for Bootstrap css and js 
* Chart.js
  * js based chart creation. It is worth noting that unless the js code placed in the same html, charts were not functioning. pls ref the [documentation](https://www.chartjs.org/docs/latest/getting-started/)
* Cloudinary
  *  cloud-based image- and video-management solution for websites and mobile apps. 

# Honorable mentions  
I would like to express my gratitude and recognition to the following individuals and organizations who have played a significant role in my journey:

* Daisy McGirr - My mentor from Code Institute, whose guidance, support, and expertise have been invaluable throughout the development process. Daisy has been a true inspiration, constantly pushing me to strive for excellence.
* David Bowers - I would like to extend my appreciation to David for his willingness to assist and support me in the absence of my mentor. His humility and willingness to help have made a positive impact on my progress.
* Code Institute - I am grateful to the entire team at Code Institute for providing an exceptional learning experience and resources. Special thanks to the tutor team, especially Alen McGee and Jason, for their prompt assistance and guidance whenever I encountered challenges.
* My Wife and Child - I owe a heartfelt thank you to my wife and child for their unwavering support and understanding throughout this journey. Their presence has been a constant source of motivation and inspiration. 

These individuals and organizations have made a significant impact on my development journey, and I am grateful for their contributions to my success.
  
# Credits
* Balsamiq was used to create the wireframes.
* The site was developed using VScode.
* GitHub was used to store my repository.
* Responsive screenshot made using [techsini.com](https://techsini.com/multi-mockup/index.php)
* Guidance on file structure for templates folder from [learndjango.com article](https://learndjango.com/tutorials/template-structure)
* [W3cschool](https://www.w3schools.com/howto/howto_css_timeline.asp) was used to source the majority of the code used to create a timeline in CSS for the insights page. Minor styling adjustments were made and the HTML was adapted to include a Jinja for loop to display the relevant data without code repetition.
* How to handle exceptions [studygyann.com](https://studygyaan.com/django/django-custom-404-error-template-page)
* Fonts were taken from [Google Fonts](https://fonts.google.com/)
* Multiple videos sourced from youtube were used to research a variety of topics:
    * [Programming with Mosh Python Django Tutorial for Beginners](https://youtu.be/rHux0gMZ3Eg)
    * [Learn Django - Class-Based Views series](https://youtu.be/ScteNE1jB4g)
* General references:
    * [Geeks for Geeks](https://www.geeksforgeeks.org/)
    * [Stack Overflow](https://stackoverflow.com/)
    * [Code Institute Learning Platform](https://codeinstitute.net/)
    * [Django Documentation](https://docs.djangoproject.com/en/3.2/)
    * [Bootstrap Documentation](https://getbootstrap.com/)
    * [Jinja Template Documentation](https://jinja.palletsprojects.com/en/3.0.x/templates/)