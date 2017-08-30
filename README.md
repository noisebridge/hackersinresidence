## Hackers In Residence: https://www.hackersinresidence.org


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


### Structure

1. The [structure of a new django project](https://docs.djangoproject.com/en/1.11/intro/tutorial01/#creating-a-project)
    - This guide also recommends not storing python code in the document root. Since Python is rendering this stuff anyways, it makes sense (nothing in the project directory is used by apache). What about static assets???  Those are served by Python too right? Unless we use a CDN or other static asset server.
    - Explore if static assets are impacted by removing this python code from the web root. A symlink to the static assets folder may be one route to simply managing this.
