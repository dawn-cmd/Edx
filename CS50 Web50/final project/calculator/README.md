# Calculator

## 1. About distinctiveness and complexity requirements

+ My project is a web application which servers as a calculator. It is totally not related to a website like social network or a e-commerce platform. So Im confident that it is distinctive.

+ My project is a single-paged Javascript web application. It contains only a index page. All the commands on front-end is achieved by Javascript. Moreover, it is a calculator, so I use a model to record the history of ans, which called "ans" and can be find in models.py

+ This project has made modification on mobile devices

## 2. About the content

In the "board" application I created, there exist admin.py, models.py, urls.py, views.py and an index html file.

+ models.py: I create a model named "ans" in models.py. The ans models contains two attributes, which are timestamp and num. This model is used to record the history answer of the calculator.

+ admin.py: I register the "ans" model in admin.py to supervise the infomation about the model.

+ urls.py: The urls.py has three paths: a blank link represents the index page, and two api links for calculate and check history.

+ views.py: This file contains three display functions: index(), calculate(), get_ans(). 

    + index(): The function to show the main page. Display when the application open and server as a default page

    + calculate(): The core function of this application, which is an api function in this project. It works by receiving the fomula from the front-end, calculating in the back-end and returning the answer to the front-end.

    + get_ans(): This function can be used to check the history. When this api was used, it will return the last ans the calculator get.

+ index.html: index.html contains two main parts: the body part and script part.

    + body: I depict a calculator board in the body part and named them with id.

    + script: I set onclick for the buttons and control the screen to display formula or answer.

## How to run my application
Just like the other normal django web applications, it is only need to input "python manage.py runserver" in the command board and visit the specific link. 

After the browser enter the link, it will display the calculator's board and you need to press the button to input formula. After you input the formula, press "=" button and the application will get the answer and print it in the screen. All the answers will be recorded in the application. 

Moreover, you can press "del" button to delete the content you input or press "clear" button to clear the screen. If you press "ans" button, it will add the last answer you get into the input board.

The calculator suppports calculations on integer and floats. 
