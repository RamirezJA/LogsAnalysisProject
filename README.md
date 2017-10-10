# Logs Analysis Project

This project will allow you to practice your SQL database skills. The project allows you to interact with a live database both from the command line and from the code. In the project you can explore a database with over a million rows. The project uses complex queries that are used to draw business conclusions from the data. The project works with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

The program runs three reports for answers to the following questions:

What are the most popular three articles of all time?

Who are the most popular article authors of all time?

On which days did more than 1% of requests lead to errors?


## Getting Started

1.Install Vagrant and VirtualBox.

2.Download or Clone fullstack-nanodegree-vm repository.

3.Download the data here: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

4.Unzip file and move the newsdata.sql into the vagrant directory, which is shared with your virtual machine.

5.Using the terminal from the vagrant directory run the VM using vagrant up command

6.Then run the vagrant ssh command to log into your VM

7.To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.

8.Create the following two database views within psql -d news:

CREATE VIEW http_cuatros AS SELECT date(time) as date, count(status) AS numbers FROM log WHERE status LIKE '%404%' GROUP by date;

CREATE view add_all as SELECT date(time) as date, count(status) as numbers FROM log GROUP by date;

9.Return to the vagrant directory with \q 

10.From the vagrant directory run python logsanalysisproject.py

12.Shutdown the VM with CTRL + D.

### Prerequisites

-Python 2.7

-Vagrant

-VirtualBox

-PostgreSQL

### Files

LogsAnalysisProject.py This is the program for the internal reporting tool

report.txt This file contains the output of the program

ReadME
