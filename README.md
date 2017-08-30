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


