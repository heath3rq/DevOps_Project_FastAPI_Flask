# hq-individual_project4

[![GitHub Action for Continuous Integration](https://github.com/nogibjj/hq-individual_project4/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/hq-individual_project4/actions/workflows/main.yml) [![AWS CD](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZzhJYWszcEZKYTJ0aEIwZEh0UU1uSmprdXZrWnNYQ3pLcE5QeEtxcWRZSmQ4ZDRWWFRJTWdTczVYOWxzQ0IvTTRHU2RSQkhjWVBXQTA2d2ZSTXZnTld3PSIsIml2UGFyYW1ldGVyU3BlYyI6IjlMVXI1Z3pTNENLZlN2cVEiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

## Project Description

The project is done for IDS 706 Data Engineering class at Duke University. The goal is to create a Microservice that returns a JSON payload and performs a Data Engineering related task. We are expected to perform Continuous Integration with Github Actions and configure build server to deploy changes on build for Continuous Delivery. Therefore, I built a menu generator app for one of my favorite restuarant. Both Flask and FastAPI were leveraged to display the randomly generated menus. I then enabled Continuous Integration with Github Actions and Continuous Delivery with AWS CodeBuild.


## Data Flow Diagram
![menu_generator](https://user-images.githubusercontent.com/105904149/203690233-099d68b3-f7fb-4c75-9218-1ae4210aa89b.png)


## Demo Video
[Project 4 - Heather Qiu - Menu Generator - Watch Video](https://youtu.be/UCVKkLASg94)


## Instructions To Replicate the Process Yourself
To run the python scripts after cloning the repository, type in your terminal: python <filename>.py. An example is `python menu_fastapi_app.py`. There will be a window pop-up on the bottom right corner of your Codespace instance to assess the temprorary web app. A sample output looks like:
```
{
Your meal includes: 
😋 Confit Mushrooms and Chicory Caesar as appetizers; 
🍕 Whole Fish as the main course; 
🍨 Church Basement Cookie & Bar Plate as dessert; 
🍸 Bottineau and Cobbler as your drink choices. 
💵 The total cost after gratuity and tax is $149.71.
}
```
