<!-- Title  -->
<!-- Description of Project -->
<!-- Contents List  -->
<!-- UX -->
# *User Experience* (UX)
### 1. <strong>User Stories</strong><br> 
* - a. Guest User
* - b. Registered User

## 2.<strong> Design</strong><br><hr>

<strong>Framework</strong>
* - Materialeze
* - jQuery
* - Flask
<br>

<strong>Colors used</strong>
<!-- Short Color Description -->
* - Colors
- * i.<!-- colors goes here -->

<!-- Icons Used for Project / Short Clear description -->
<strong>Icons Used</strong>
<!--Icon description  -->

<strong>Typography</strong>
<!-- Typography Description -->


<!-- Project Wireframes -->
### <strong>Wireframes</strong><br><hr>
<!-- Wireframes Goes Here -->
<!--<h5 align="center"><img width="550" height="430" src="wireframes/"></h5>-->

# Features<hr>

### ***Existing Features***
<!-- Existing features goes here -->
<!-- Accesible For All ->
<!-- Have Access Just If Registered -->
**Access Just After Registered**
<!-- What registered quest can do after registered -->

# Technologies Used<hr>
<!-- Here Goes Tech Used -->
-  ### **Languages Used**
<!-- FrameWorks/Libraries/Programs -->
- ### **Frameworks, Libraries & Programs Used**

<!-- Features Test  --->
# Features Test<hr>
<!-- Steps for Testing -->
1. LogIn
2. Register 
3. Add Recipe
4. Check Your Recipe
5. Update Recipe
6. Delete Your Recipe


## More Testing <hr>
<!-- After Registered -->
<!-- Log In  -->
<!-- Username/exist/no in db -->
<!-- Flash Mesagges -->
<!-- As non logged user access -->


### As Guest <hr>
<!-- What a Guest User will want to see / Fell / Travel -->


### As a Logged Guest <hr>
<!-- What a Logged Guest will Experience  -->


# Deployment 
<!-- Deployment Steps -->
- ## Requirements <hr>
- * 1.Python3 to run the App
- * 2.PIP for installation of what App Requirs
- * 3.GitPod as IDE (<em>You can choose your favorite IDE</em>)
- * 4.MongoDb -- MongoDb Atlas for DataBase

- ###  *Deploy To Heroku* <hr>
<h4>What will you need:</h4>

* i. For Creating requirements.txt file --> Tap in terminal  `pip3 freeze --local > requirements.txt`.
* ii. For Procfile --> Tap in terminal `echo web: python app.py > Procfile`.
* iii. You need to --> Add, commit and push these to GitHub.
* iv. Travel to Heroku Website.
* v. Create New App and Name it close to what the name of the App is on GitHub.
* vi. Choose region that is closest to you.
* vii. Go to the Deploy tab and choose Github.
* viii. Seach for current repository on what you want to work and connect.
* ix. On Heroku settings, navigate to Config Vars.
* x. You Need to set The following:<br><hr>
`IP = 0.0.0.0`<br>
`MONGO_DBNAME = [Name of MongoDB]` <br>
`MONGO_URI = mongodb+srv://:@<Your_cluster_Password>-qtxun.mongodb.net/<Your_database_name>?retryWrites=true&w=majority`<br>
`PORT = 5000`<br>
`SECRET_KEY = [Secret key]`<br>

* xii. Back to Deploy Tab --> Deploy Branch --> Choose Master Branch.

- ###  *Set up MongoDB Data Base* <hr>
- * 1. Travel to [mongoDB](https://www.mongodb.com/)
- * 2. Set Up Free account.
- * 3. Click on  Clusters and press Create new Cluster.
- * 4. Select Starter Clusters and Create a Cluster.
- * 5. Chose closest region to you.
- * 6. Select the M0 Sandbox tier.
- * 7. Add your cluster name.
- * 8. Create Cluster.
- * 9. Travel to Cluster and Click Collections.
- * 10. Create the database name and then add Collection:
- - *  a. Create Collection called: Categories:
- - *  i.1.Categories: <br>

            _id:<ObjectId>
             category_name:<string>

- - * i.2. Recipes:<br>

            id:<ObjectId>
            category_name:<string>
            recipe_name:<string>
            ingredients:<string>
            method:<string>
            created_by:<string>
            url:<string>

- - * i.3 Users:<br>

            id:<ObjectId>
            username:<string>
            password:<string>
- * 11. Click Overview
- * 12. Click Connect Your Application
- * 13. Copy full driver code example.
- * 14. Paste It in your env, on the MONGO_URI (Do not forget to put your password and database name what you currently using.)
- * 15. The following environment variables will need to be setup in your project:<br>
`app.config["MONGO_DBNAME"] = "Your database name"`<br>
`app.config["MONGO_URI"] = "The connection string, replace the password placeholder with your actual user password"`<br>
`app.secret_key = "A long random hidden string"`<br>

- ###  *Forking Project* <hr>

- * Travel To Github.
- * Chose the repository you want to fork.
- * Click the fork button, located on the right hand side.
- * Make the changes you want to the present Project.
- * If you wish to merge your changes to the original project:
     - * Press the pull request button from your forked repository.
     - * Press the button new pull request.
     - * Choose the branches you wish to merge.
     - * Press the Create pull request button.

- ###  *Clone Project* <hr>
- 1. Navigate to GitHub main page Repository.
- 2. Find Green Code button and click it.
- 3. To clone the repository using `HTTPS `you need to pic `"Clone with HTTPS"`.
- 4. Open the terminal
- 5. Change your current working directory to a location you want cloned directory.
- 6. Type <strong>`git clone`</strong> and then paste the `URL` you copied on step Nr3
- 7. Press enter to create your local clone.


<!-- Here Goes Credits -->

# Credits

<!-- Where codes come from -->
### Code

<!-- Content -->

### Content
<!-- Thank you Part -->
### Acknowledgements

#### My Mentor

#### Code Institute