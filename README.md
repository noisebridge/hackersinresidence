## Hackers In Residence: https://www.hackersinresidence.org

### Little issues

- It seems to be taking css from the webapp app, not the collectstatic dist path


#### Django User 

pinax django-user-accounts app - it's basically required to keep the project slim.

##### Downside: it requires pinax-theme-bootstrap which requires some things:

- Bootstrap 3.3.5
- Font Awesome 4.4.0
- jQuery 2.1.4

##### Result:

- Modified the templates to remove most of these requirements.

##### Pinax Options

1. Install the dependencies
2. Copy the template files for account from the app and drop them in my templates folder
    - This requires some retrofitting, ugh.


##### Django User Resources

- [more info](saticfiles deploy howto](https://docs.djangoproject.com/en/1.11/how    to/static-files)
    - weak password linting not provided by default, can be form validation?
- [manage auth](https://docs.djangoproject.com/en/1.11/topics/auth/default/)
    - check logged in, permission required, etc
    - will need this to show a user their entries?


### Deployment

1. Templates
    - Update `robots.txt` on the deployed instance.
    - Fix the browserconfig.xml or whatever, I think it's for microsoft mobile stuff. It needs some tile static assets.
1. Static Files
    - django.contrib.staticfiles deploys static files on dev only
    - [django staticfiles deploy howto](https://docs.djangoproject.com/en/1.11/howto/static-files/deployment/)
1. Database - sqlite
    - initial deployment will be using sqlite to reduce management overhead. This should work indefinitely unless the number of organizations goes beyond the thousands or some other unforeseen circumstance.
1. Site URL
    - make sure your site is set
    - you can do this in the backend
    - [explanation and howto](https://stackoverflow.com/questions/11814059/site-matching-query-does-not-exist)
    - [django site docs](https://docs.djangoproject.com/en/1.11/ref/contrib/sites/)
    - to delete a Site, unregister it then delete the object
        - [unregister with django.contrib.admin](https://stackoverflow.com/questions/5742279/removing-sites-from-django-admin-page)
        - [delete the object with filter+object's delete() method](https://stackoverflow.com/questions/3805958/how-to-delete-a-record-in-django-models)
1. Email backend on dev
    - i used the smtp server shim shell script in this project root for dev (see settings.py on dev)
    - [django docs](https://docs.djangoproject.com/en/1.11/topics/email/)


### Guidelines

This first iteration of the project is supposed to be cheap, extendable, and hackable.

1. Avoid Javascript (tor friendly)
1. NO emphasis on design (bootstrap css for the most part)
1. Mobile is derived from bootstrap friendly stuff almost exclusively


### Templates & Data Models

1. Opportunity
    - Produced by an organization submitting a form
    - Updated by an organization submitting a pre-filled form.
        - Updates require approval, make a special note by the submit button
        - This note can be on the submission form too
    - Cannot be deleted, but state can be changed to cancelled.
    - Allow the organization to un-cancel opportuntities too.
    - Data model consumed by the opportunity

#### accounts templates

The accounts templates are copied from pinax-theme-bootstrap which is MIT licensed.


#### Deploying a mail in a view on form submission

- [more info](https://docs.djangoproject.com/en/1.11/topics/forms/#field-data)


#### Flash Messages

- [more info](https://docs.djangoproject.com/en/1.11/ref/contrib/messages/)


# Documentation

Documentation can go here.


## Approval

Moderators must got into `/admin/` and approve an organization or opportunity the first time it is created.


## Maintenance

Here is as much of the system maintenance as I can think up at the moment.


### Linode

1. Enable Backups on the server
2. Make a `backup` or `snapshop` now because you want to be able to rollback to a working state.

### Database

The project database is sqlite and is stored in the project directory, NOT under source control.

The project database should be backed up regularly, any changes between backups will be lost. These will also be backed up in Linode rolling backups, but would need recovered from the server snapshot.


### Ubuntu 16.04 LTS

Unattended upgrades is enabled, but that doesn't mean that manual OS maintenance should be skipped. Information about maintaining ubuntu is not included here.


### Django

Django 2.0 was released during the creation of this project. This project should eventually be updated to Django 2.0 and Python 3.


###  Namecheap: SSL Certificate, Domain Name, Private Email

The SSL Certificate will eventually expire, this date should be noted and planned for.

The domain name and email service need regularly renewed, currently via namecheap.
