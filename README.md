----------


# GeekHaven - Personal Blog

![geekhaven-blog-cosplay-and-gaming-community](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/bea14448-a0f5-4993-ac9a-f0a5c75fdfdf)
)


Visit the deployed site: https://geekhaven-ab6b47c83d52.herokuapp.com/

I plan to create a simple yet rewarding personal blog of my cosplay and gaming adventures. The blog also sports a section for community members to upload their cosplays for people to see.

## CONTENTS

* [User Stories](#user-stories)

* [Design](#design)
	* [Accessibility](#accessibility)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)

* [Features](#features)

* [Technologies Used](#technologies-used)
	* [Languages Used](#languages-used)
	* [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Iteration over starting code](#iteration-over-starting-code)

* [Deployment & Local Development](#deployment--local-development)
	* [Deployment](#deployment)
	* [Local Development](#local-development)
	* [How to Fork](#how-to-fork)
	* [How to Clone](#how-to-clone)

* [Testing](#testing)

* [Bug Fixes](#bug-fixes)

* [Credits](#credits)

* [Code Used](#code-used)

* [Content](#content)

* [Acknowledgments](#acknowledgments)

- - - 

## User Stories

| Epic | User Story  |
|--------------|---|
| Unauthenticated User | As an Unauthenticated User, I want to view the homepage so I can browse the content  |  
|              | As an Unauthenticated User, I want to click on a nav bar so I can navigate to the selected content   |
|              | As an Unauthenticated User, I want to register an account by clicking Login/Register so I can join the community |
|              | As an Unauthenticated User on the Login/Register page, I want to sign in once I have created an account so I can start engaging with the content 
|              | As an Unauthenticated User, I want to click on a blog so I can view the content  | 
|              | (Addon) As an Unauthenticated User on the cosplay hall of fame, I want to log in or register an account via the buttons provided | 
| Authenticated User             | As an Authenticated User I want to have confirmation when I perform an action so that I know they have happened | 
|              | As an Authenticated User I wish to submit a cosplay to the Hall of Fame so that I may share my hobby with the community   |
|              | As an Authenticated User I want to edit/delete my cosplay submission so I can have control over my content  |  
|   Site Admin           | As a Site Admin I want to create, update, upload images and delete my posts so I can control the content of my blog  | 
|              | As a Site Admin I want to approve or disapprove cosplay submissions so I can ensure a good tone is kept in the cosplay Hall of Fame section   | 
|              | As a Site Admin I want to delete comments that I've previously approved to ensure full control of my blog content(covered in the same User Story as above)  |
|              | (addon) As a Site Admin I want user comments to go through a validation against a set of banned words so that they can be automatically rejected |
|              | As a Site Admin I want both Authenticated/Unauthenticated users to search the site via a search bar so that they can find relevant blog content |
  

- - -

## Design

* Colour palette - My first idea is a palette I found on Coolor, it appeals to me as it's my personal blog, whilst also giving Cyberpunk vibes which adds to its gamification. The very vibrant pink will only be used for a few outlines so as not to give anyone a headache!

![preliminary colour palette](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/0902544c-cf91-473e-ac5f-304ea954586d)

After choosing this colour palette I was introduced to Tailwind CSS Color Generator and took one of the hexcodes from it, adjusted the hue to a more pastel shade, and exported the hexcodes to my Tailwind config.

![updated colour palette](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/ad83f848-9bd3-4429-97f9-eed7d5db3e1e)


I spent some time researching gaming and cosplay blogs and found that I preferred the more minimalist style. Too much information made it more like a news site (such as [Kotaku.com](https://kotaku.com/) ) but sites like [The Gaming Blog](https://thegamingblog.co.uk/) were more clear and concise, and more blog-like to me.

I liked the enlarged header and footer design of The Gaming Blog, as well as the very centred content with a lot of space on the sides, even on my small laptop the content wasn't spread out too much, so I will try to implement something similar:

![the-gaming-blog-header-nav](https://github.com/emmy-codes/Star-Trek-Museum/assets/70635859/13cd4718-c66b-41a5-9311-706ee310e135)

The blog content heading suited my style much more from Kotaku, so I will use that as a base for my blog posts:

![kotaku_blog_header_preview](https://github.com/emmy-codes/Star-Trek-Museum/assets/70635859/ac560aa9-d221-4833-89ad-76593b464dfb)

For the login pages, I had a quick Google of login/signup pages and really liked the design of [this envatoelements design](https://elements.envato.com/login-page-screen-02-DQUHPP?irgwc=1&clickid=3BdW0o0pXxyPRuQxyZSGN09uUkH1ljy9Xwq5UQ0&iradid=298927&utm_campaign=elements_af_78798&iradtype=ONLINE_TRACKING_LINK&irmptype=mediapartner&utm_medium=affiliate&utm_source=impact_radius&mp=Speckyboy%20Design%20Magazine) both in colour scheme and cleanliness of the layout. 

### Accessibility

Accessibility plans:

* Semantic HTML
* Descriptive alt text for images (this turned out to be difficult due to the dynamic nature of the webpage).
* Ensure good colour contrast for visually impaired users with [Colour Contrast Analyzer](https://www.tpgi.com/color-contrast-checker/)
* Colour blindness: I did some research on the most common types of colour blindness and other than the vibrant pink (which will make up a small, small portion of the site) the rest of the colours still looked OK together.

### Imagery

The imagery for the blog will either be photographs from my projects, free images on the internet or perhaps AI generated if I need something specific.

### Wireframes
  
![login page](https://github.com/emmy-codes/windows-95/assets/70635859/582402ed-25e7-4796-aae5-b5f9e3dfef06)
![blog page](https://github.com/emmy-codes/windows-95/assets/70635859/dee114d6-ff61-4642-937b-4621b567025b)
![chat page not signed in](https://github.com/emmy-codes/windows-95/assets/70635859/67c6db23-e558-4806-8166-aa457a7406ec)
![chat page](https://github.com/emmy-codes/windows-95/assets/70635859/6ac17dce-e906-4620-8782-6410f31a1ec4)
![sign up page](https://github.com/emmy-codes/windows-95/assets/70635859/cee5ffd1-2713-426a-84b3-f2671627de18)
![homepage](https://github.com/emmy-codes/windows-95/assets/70635859/d02a8b57-8332-4cca-8aaa-c474c48c22fb)

Here are the pages to match against the wireframes (as cosplay submissions was a last minute panic to ensure I had an adequate unique model, I didn't get time to create a wireframe for it):

[Live site screenshots compliation to not flood ReadMe](https://github.com/emmy-codes/geekhaven-blog/blob/main/live-site-screenshots.md)

## Features
 The website consists of several key pages:

* Homepage - this is where all users can see the list of blog posts written by the admin
![geekhaven-blog-cosplay-and-gaming-community](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/a554a19d-65ff-471e-9664-3a5f9bb322dc)
* Blog post view - when the user clicks on a blog post they're redirected to that specific blog to read about the content.
* User registration - anyone can create an account to engage in different ways with the content. There are measures in place to ensure no two users can have the same email or username, and that the password is of sufficient strength.
* User login/out - the user can choose to log in or out of the website. Logged-in users have access to submit cosplays to the community!....
![login_screen](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/c0dc610c-c7d4-4c09-af1a-a5110eefdcd5)
* .... which leads on to this feature, cosplay submissions. Authenticated users can upload an image with a description and character name. Submissions will be pending until an admin has approved them.
* Cosplay Hall of Fame: Published submissions  (and the user's own pending submissions) can be viewed on this page.
* Editing submissions - Authenticated users can also edit their submissions at any time by going to the Hall of Fame. This will redirect them to the cosplay submissions page but with the prepopulated form data from their original submission.


- - - 

## Technologies Used

### Languages Used
 
HTML
CSS
JavaScript
Python
Tailwind CSS and components

### Frameworks, Libraries & Programs Used

[Github](https://github.com/) - For online storage of code and deployment.

[Picresize](https://picresize.com/) - Used to resize images for Readme/Testing docs.

[VS Code](https://code.visualstudio.com/) - For writing my code.

[Heroku](https://dashboard.heroku.com/apps) - For deploying my program.

[Grammarly](https://app.grammarly.com/) - For grammatical adjustments.

[Materialize](https://materializecss.com/) - Framework to make responsive front-end solutions.

[Django](https://www.djangoproject.com/) - To build my CRUD functionality.

[PostgreSQL](https://www.postgresql.org/) - For my Database.

[Cloudinary](https://cloudinary.com/) - For hosting blog images.

[Coolors](https://coolors.co/) - To create colour palettes.

[Tailwind CSS color generator](https://uicolors.app/) - To generate a CSS palette for Tailwind.

- - -
  

## Iteration over starting code

Here I will take you through some of my thought processes and first iterations of code to help see my learning and problem-solving process.

I did a mix of utilizing the information from Code Institute's "I think therefore I blog" material, and trying to do it myself to see how much I'd learned. 

One of the first issues I encountered was setting up my blog post class. After a few hiccups, everything migrated correctly and I could access the admin panel and see the button to add a blog post. I went in, only to realise that I had no field for the bulk of my blog content.

![bug_1_no_blog_content](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/ce42cb49-2526-4a9b-8940-d26f8df47ba2)

I checked my class on models.py - there was my blog_content attribute! But it wasn't showing up on the admin panel... so I checked my migration 0001_initial.py and checked what had been migrated.
No blog_post.
This led me to do a quick check and yes, it was meant to have brackets on the end of my TextField type. A small error that wasn't picked up in any code compiling but still caused an undesired result. All it took was a () (and a default parameter) and a new migration to fix!

![bug1 textfield issue](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/c83d2c81-8ba1-41cd-b070-1a35f1f42c7f)



- - -

## Deployment & Local Development

### Deployment

This project was deployed at [Heroku](https://heroku.com/)

The numbers on the screenshots represent the numbers on the steps of my deployment process.

To deploy this project after creating my account, I:

1. Went to my dashboard and clicked on the New App dropdown menu

2. Clicked Create new app from the options
  

![heroku_deployment_step_1-2](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/f5810840-3399-48aa-8944-384850e2f6d9)


3. Named my app in the App name box

4. Chose a region from the dropdown menu (and accidentally chose the United States for this one)

5. Clicked Create app


![heroku_deployment_step_2-5](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/be20a348-416c-446c-8876-2a33ccb883bb)

Once the app was made I went to my dashboard where I can see my apps.

6. Clicked on the relevant app

![heroku_deployment_step_6](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/e6648e64-446c-4832-929f-3f7477c236b6)


7-8. From here, I went to settings, then to the Config Vars. I added the key of DISABLE_COLLECTSTATIC and gave it a value of 1.

![deployment_step_7-8](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/5e1a7d4f-3a96-42b5-bda3-464fbf8cd907)


9. I then had to prepare my code for deployment. Back in VSCode I installed the following gunicorn version and added it to my requirements.txt file:

![deployment step 9](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/55bf05d5-8451-4d27-95ef-f97b50d5b65b)

10. After that, I created a Procfile in the root directory and added my blogpage file directory to the Gunicorn WSGI:

![deployment_step_10](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/05cd3c9a-f252-4d98-a6c5-9400a6338c4b)

11. To keep my files safe when deployed, in my settings I changed DEBUG to False to prevent excessive information from being shown when errors occurred which could potentially give people unwanted access. I then updated my ALLOWED_HOSTS list to include my Heroku deployment links.
12. Back on Heroku I switched to the Deployment tab and connected Github as the Deployment method. I searched my repository name and connected it.

![deployment_step_12](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/aba54a9b-9436-4ad9-9e1c-6985be01cdce)

13. Scrolling down the page, I chose to manually deploy my project as needed, but it's possible to set up automatic deployments if preferred.
  
![heroku_deployment_step_13](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/fed29cb2-9af8-4d0d-a827-ef493390b716)

  

### Local Development


#### How to Fork


Should you wish to fork this repo, here is a guide on how to do that:


Firstly, go to https://github.com/emmy-codes/geekhaven-blog/


1. On the main repo page, click the Fork button near the top right corner
![fork_step_1](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/2ac24fa9-0403-49f5-92b1-f4e5160f5109)


2. On the create a fork page, check the Owner of the repo is set to the GitHub org you wish to use, and change the name of the repo if you wish.

	2a: Add a description if you want to.

3. Check the box here if you want to make a copy of the main branch or multiple branches (main is selected by default).

4. Create the fork. The screenshot is from an old project as I cannot fork my Python project due to not having any organizations connected to my account, and presumably because this repo is already a fork of the CI template.
 
 ![rsz_fork__steps](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/aa4dae7c-807d-4108-bb5b-f24c7010514b)


#### How to Clone
  

For cloning the repo you will need:

* The [repo](https://github.com/emmy-codes/geekhaven-blog) open
 

* Your IDE of choice

1. On the repo page, click on the green "Code" button

2. On the dropdown from the Code button, click on your chosen key (pictured here is SSH)

3. Click the copy button (shown as two squares on top of one another) 

![ssh_code_copy_gh](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/ea6bcd4d-40d1-4250-b3ea-eb3e6b804efd)


4. Open your IDE of choice and open the Terminal, or in my case, open the Terminal on your computer (I run Linux on Windows so may be slightly different for Mac/Windows users)

5. Check that you're in the right folder (shown here by checking my current folder by using the input: ls

6. Change as needed to reach your desired folder.

7. Type (without quotation marks): "git clone" followed by your copied link from GitHub.
  
  ![git_clone_on_ubuntu](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/bfa89623-5fc5-4c04-a526-f3dffabdd964)

8. You can now access the repo in your IDE if cloned directly there, or by typing (without quotation marks) "code ." in your Terminal.

9. Enjoy! 

- - -
  

## Testing

Please refer to the [Testing MD file](https://github.com/emmy-codes/geekhaven-blog/blob/main/TESTING.md) for manual testing

## Bug Fixes

As I am making a blog I am very mindful of trying to keep my project as far separated as I can from the walkthrough from CI, whilst still using it as an assist tool.

I am ensuring that I change any naming conventions, both to help me understand what the code does and to force me to have a more in-depth understanding of the codebase rather than copying the same names as CI.

This comes with its own set of problems when I don't fully understand something, as was proved when I attempted to append my blog posts to the HTML page I had created. I thought I had labelled everything correctly but received an error when attempting to run my server:

![appending_posts_to_dom](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/8b4abf41-64ef-4a03-95bd-1a4bb8bb2d0e)

It was telling me that blogpost_list.html didn't exist, which was entirely true. It was looking in geekhaven_blog/blogpost_list.html because ListView was looking for a file of the same name, aka my BlogPost class. After some research, I discovered it also expected geekhaven_blog to be a folder inside of my templates, which I was missing.

After making the above changes my server was once again loading!

Sometime after I had successfully appended the Cloudinary images to my homepage blog post views, I noticed that the first blog post was loading a <p> tag at the start of the excerpt, despite there not being one in the TextField of the admin panel.

![p_tag_showing_on_first_blog_post](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/ddc16ebc-83bf-41fe-bf08-e8fbaab2aa20)

I took a look at my blogpost_list.html to try and figure out what was happening, but there are no mentions of p tags in the rendering of the blog content. I thought the truncate attribute might have impacted it in some way since it was the only tag to use it, but since that only limits the amount of text content visible, it turned out not to have any impact.

I then took a look at my admin panel, and sure enough, no p tags showing. BUT when clicking on the Code View button I could see these p tags sure enough!


![p_tag_showing_on_first_blog_post_2](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/b1b83163-c5b2-4d9e-89fc-85fc3b44ba27)

It was the only one showing and I thought perhaps there was some bug/issue with it being the first post available. Then I realised it was the first post I had made after installing Summernote.... sure enough, when I looked into the error I found out the tags were being auto-inserted because of the WYSIWYG of Summernote.

Thankfully there was a quick fix since it's not possible to remove the tags manually from the admin post as they get reapplied. Simply putting "|striptags" on my excerpt stopped the tags being appended to the page. Result!

Bug 3: The next problem was when I realised that I needed to remove the block of code that was rendering the thumbnails of the blogs to my homepage since Django wants every template to only serve one purpose. I remember a bit of trouble getting the initial render and having to rename my HTML file to match somewhere else to make it render... but where?

![bug_3_template_not_exist (1)](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/4e0379f1-7ed2-4006-b78c-5256e173f27b)

Reading the error I could tell 2 things: Which part of the code that was firing the error, and the error name. I went to my BlogGrid class on views.py and looked at my recently added attribute: template_name which was pointing to geekhaven/templates/index.html as the HTML files are in a folder, it seemed logical. Yet changing it to just index.html allowed some of the content to render..... some.

![bug_3_progress](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/8ce3684b-0cef-4700-9978-9e6455c035b7)

On to bug 4... this was clearly not rendering any CSS, nor my blogpost_list.html content.

I had a quick Google around to try and find a starting point and came across a post that mentioned starting my TailwindCSS with the command python3 manage.py start. When I did that I got a massive list of errors but one stuck out "Cannot find module 'postcss-simple-vars'". It mentioned the build failing in a folder I had, that didn't contain the file it was looking for. Strange when it worked when everything was in one HTML file.

Aha! In my tailwind.config.js file, I was referencing a folder, geekhaven_blog which I recently removed as it seemed redundant inside my templates folder.  ~~This didn't help a bit, but I'm sure it will prevent another error down the line.~~ Ahaaaa! False alarm, my computer bugged out with the port open so the localhost server wasn't working properly, after a reboot I'm back to what I expected to see after moving my bloglist out of the homepage. Success!


![bug4_success](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/7c42e778-a08f-44aa-b24d-4435a5da34d5)

Hello bug5, my old friend...

I was going to consider bug 4 my final explanation to show my thought process on problem-solving, but this bug required me to make a lot of commits so it felt like something I shouldn't glaze over when it comes to looking at my commit history. All was looking well on my deployment, but as soon as I deployed the logo on my header threw a 404 error.

I dug into my code and the Heroku logs. The logs showed that Heroku couldn't find the logo on the path I had specified. I tried running the collectstatic command but that checked 209 files and adjusted none due to finding another file with the destination path. It was referencing a load of admin css files that came from Tailwind which was equally confusing and not necessarily related to my issue.

I thought back to when I had first created the project and installed Tailwind CSS and then Django Tailwind on top of that, got caught up and carried on. I thought "I'll try uninstalling django-tailwind to see if that helps" it definitely didn't! It took a lot of my regular Tailwind files so I ran a pip install just for Tailwind.

I redeployed and received the following error:

![bug_5_-_tailwind](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/4f5f575c-1e77-4e44-aa1f-7911ff705fb3)

I checked the requirements.txt file and saw that tailwindcss was marked with version 0.0.1 which seemed off. I tried updating it to the latest version on the Tailwind site. No luck. Next, I tried updating Tailwind with an npm install from the site. Nothing. So I reverted to the version that was automatically assigned.

![bug_5_-_tailwind_commits](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/abe09b9f-e883-41fa-a32d-54b26eb85a84)

I also updated the source on the image element to include Django's {% static %} parenthesis to see if it could help. After running a reinstall of tailwind css I ran the collectstatic command again and received a new error (that's what programmers call progress!) it said it couldn't find django_tailwindcloudinary_storage. A missing dependency? No, a missing comma on my INSTALLED_APPS list. Trying again I received a similar error for 'django_tailwind' uninstalling didn't remove it from my installed apps so removing it allowed the page to load correctly, logo and all! ...... ON LOCAL HOST

I also made 2 small changes on my settings.py, namely removing the leading slash on the STATIC_URL, and returning my STATICFILES_DIRS to having square brackets rather than regular which was a small change I made whilst trying to solve it since it didn't give a direct error, I thought it didn't matter which.

Dejected, I returned to https://django-tailwind.readthedocs.io/en/latest/installation.html and https://tailwindcss.com/docs/installation to reinstall django tailwind and check everything on regular tailwind was up to date. Installing it didn't break anything at least!

This project is challenging, and I've stumbled onto more errors than I've seen in all 3 projects together x4 or more. So I couldn't possibly talk about all of them, but this next one felt like a good one to tackle.

Account creation. I went blindly into this, seemingly having forgotten everything about creating an account using Django. I tried winging a class-based model with a similar layout to the blog post list and blog posts, then tried creating a function to store the data. I simply can't try to wrangle Django without support, so I had a look on multiple different websites, trying to Frankenstein a working product together.

- - -

## Credits
  
[DaisyUI walkthrough for Django and Tailwind](https://django.wtf/blog/django-alerts-with-tailwind-and-daisyui/) and [Django documentation](https://docs.djangoproject.com/en/4.2/ref/contrib/messages/) for my alert messages

My amazing partner and his error interpretation skills, and extra help putting together the form after I broke it implementing submission edit functionality! Who also gave me a crash course in Tailwind CSS and helped to speed up my use of this new tool.

[This forum post](https://stackoverflow.com/questions/65730017/using-widgets-to-change-the-css-of-label-in-django-forms/65730427#65730427) and [More Django documentation](https://docs.djangoproject.com/en/5.0/ref/forms/widgets/) for researching widgets to be able to customise the submission forms' CSS.

A whole lot of Django documentation for forms!

[Django form validation using form.clean](https://docs.djangoproject.com/en/5.0/ref/forms/api/#using-forms-to-validate-data)
[Django cleaning and validating forms](https://docs.djangoproject.com/en/5.0/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other)
[Django Form Validation](https://docs.djangoproject.com/en/5.0/ref/forms/validation/)
[Django URL usage for the HTML](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#url)

### Code Used

### Content

I have used [OpenAI](https://chat.openai.com/) to create most of the blog text content for me so I can focus my time on practising with the code.
  

### Acknowledgments

I would like to acknowledge the following people:
  

* My partner who, despite having no idea about Python, has done his best to support me in my learning 🥰

* community-sweden on Slack for becoming an amazing community space, leading to online and IRL study sessions! Many of us were doing P4 at the same time and it was great to talk with fellow students about project woes.

