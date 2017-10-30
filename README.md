## Hackers In Residence: https://www.hackersinresidence.org



### Next Actions

- set up the user system following the template from previous django projects
- write the relationship from opportunity to user and write the filtered opportunity_list view so a user can see their opportunities
- write the opportunity edit view
- write an organization info submit form and an approval form for this
- write an organization 'view organization' template
  - this will actually go in the 'view opportunity page right? but same concept so we could have both...


### not in scope, the organizations are all just available by clicking into the opportunity

- write a thing to display all the 'organizations' - the users
    - could be a 'panel view' with a photo taking the top half, a title, and a short description.  
    - then people could go to /organizations and browse the panel view


### Deployment

1. Templates
    - Update `robots.txt` on the deployed instance.
    - Fix the browserconfig.xml or whatever, I think it's for microsoft mobile stuff. It needs some tile static assets.
1. Static Files
    - django.contrib.staticfiles deploys static files on dev only
    - look at trestl to see how static files are deployed there (apache config?)
    - [django staticfiles deploy howto](https://docs.djangoproject.com/en/1.11/howto/static-files/deployment/)
1. `site-packages`
    - in trestl-django this is symlinked from the project root to `venv/lib/python2.7/site-packages/`
1. Database - sqlite
    - initial deployment will be using sqlite to reduce management overhead
    - migration to postgres could be done manually in the future if the site has highly concurrent database transactions, under the current submission model we will likely have < 10 transactions per DAY. 
    - there are utilities for converting between sqlite->postgres and models might need updated


### Guidelines

This first iteration of the project is supposed to be cheap, extendable, and serviceable. I have a lot of latitude in order to ensure the cost is low and the project is hackable. Ideally volunteers will take over when I finish.

1. Avoid Javascript (tor friendly)
1. NO emphasis on design (bootstrap css for the most part)
1. Mobile is derived from bootstrap friendly stuff almost exclusively


### Simple iteration of hackers in residence that allows:

1. organizations to: 
    - create accounts
    - post opportunities
    - update opportunities
    - view opportunities (of any state)
        - this is recycled from the opportunity search template
    - see and update opportunity state:
        - pending approval
        - active
        - rejected
        - cancelled (by the user)
        - expired
1. admins to: 
    - update opportunity state
    - view a `pending review` queue of opportunities
        - this is recycled from the opportunity search template
            

1. individual users/applications
    - How to apply: NOT through hackers in residence, could be email, link, etc.
    - VERY slim, conceptual only - no infrastructure for users to track their applications or for applications to even exist
    - Applicants do not have their own account
    - Applicants reach our directly to the organization by email or other means.
    - Organizations must have certain contact info in their opportunity.


### Templates & Data Models

1. Opportunity
    - Produced by an organization submitting a form
    - Updated by an organization submitting a pre-filled form.
        - Updates require approval, make a special note by the submit button
        - This note can be on the submission form too
    - Cannot be deleted, but state can be changed to cancelled.
    - Allow the organization to un-cancel opportuntities too.
    - Data model consumed by the opportunity


#### Deploying a mail in a view on form submission

- [more info](https://docs.djangoproject.com/en/1.11/topics/forms/#field-data)


#### Flash Messages

- [more info](https://docs.djangoproject.com/en/1.11/ref/contrib/messages/)

### Structure

1. [structure of a new django project](https://docs.djangoproject.com/en/1.11/intro/tutorial01/#creating-a-project)
    - This guide also recommends not storing python code in the document root. Since Python is rendering this stuff anyways, it makes sense (nothing in the project directory is used by apache). What about static assets???  Those are served by Python too right? Unless we use a CDN or other static asset server.
    - Explore if static assets are impacted by removing this python code from the web root. A symlink to the static assets folder may be one route to simply managing this.
