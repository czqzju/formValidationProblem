# [Form validation problem]

This small project is to solve the problem of Form validation in  (https://springload.github.io/form-validation-problem/). The Django form components have been used. A django.forms.Form class IndexForm has been defined to handle the index.html in template. It uses the local and global hook function to validate the fields with the following rules before the form is posted to the (in this case imaginary) server:

* `Email` must be a valid email address.
* `Password` must be longer than 8 characters.
* `Colour` must be selected.
* At least two `Animal`s must be chosen.
* If `Tiger` is one of the chosen `Animal`s then `Type of tiger` is required to be a non-empty string.

## Other features

If the form is submitted and an error occurs, the error element's parent will have a CSS `error` class added to it.

```html
<p class="error">
    <label for="field"></label>
    <input id="field" type="text" value="foo">
</p>
```

## Main modification

* my_forms.py store the custom Form class IndexForm to do the validation
* views.py handles the http request
* index.html has been modified to be suitable with Django Form components

## Project setup
Before running this project, you will need to perform some set of actions(steps) to make application dependencies available in the different environments.

* Python 3.7.2
* Create a virtual environment $virtualenv venv -p python3
* Activate the virtual environment
* Install the dependencies of the project $pip install -r requirements.txt
* Run the project $python manage.py runserver
* Access http://127.0.0.1:8000/index

## Some considerations

* For the password, wo could add the feature to hint what kinds of password is good
* We could execute the unittest for each field with boundary consideration