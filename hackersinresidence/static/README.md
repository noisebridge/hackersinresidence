## Static Assets

WARNING: DO NOT EDIT THE STATIC ASSETS IN /hackersinresidence/static. EDIT THE FILE AT /hackersinresidence/webapp/static and use django collectstatic to move them to the static files folder.

The purpose of this static assets folder is to be hackable by a variety of contributors over a long period.

Since we are not anticipating massive usership, we can afford to load multiple CSS files directly.

Additionally, CSS is not minified.  

Bootstrap 4 minified is included in `vendor` along with an unminified version and a map for each.


### `images/`

Please web optimize images before putting them here. 

1. Guidelines:
    - `PNG` is best for things with sharp edges. 
    - `JPG` is best for things like photo of a forest. 
    - `SVG` for scaleability (computer generated images like logos).


### `vendor/css`

Assets in the vendor folder should not be manually changed. Override them instead. If you need to fork a vendor asset, move it from vendor.


### Task Runners & Automation

There are many task runners and build automation tools, from make to gulp to webpack.  

If we don't use one, more people can contribute.


### CSS

Firefox and Chrome are the two primary targets for our CSS. Using CSS for animations and other features is a great idea.


### No Javascript

Avoid javascript, this web application caters to people who do prefer to use anonymity tools.

