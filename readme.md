# BhaiKhata Backend

## To setup backend

1. Clone the BhaiKhata Backend repository
2. Run the command python manage.py runserver to run the backend on the server.

### [Link](https://github.com/shivam7374/BahiKhata-Frontend) to BhaiKhata Frontend

### [Link](https://docs.google.com/document/d/1iu6_CggWeDP6K82gglrFUcfRqFFB63vZptDkORlj7BE/edit?usp=sharing) to google doc

## Technologies Used

### Backend: Django

### Frontend: ReactJS

### Database: SQLite

## Features

1. This is a multiuser application where the user can maintain the transaction easily and in a meaningful manner by including one or more than one users.
2. The user could see the list of known users or friends.
3. There is a feature to create, update, and delete the transaction to split the bill.
4. The user has the facility to spilt the bill in several ways such as split equally, custom split, none, party etc.
5. The list of the transactions is displayed n the home page where the user can view the transaction history.
6. While creating the transaction the user should add a description for the transaction and categories the transaction among one of the several categories provided and then split it accordingly.
7. The user is able to see who owes you and who you owe.
8. There is also a feature to filter among transactions based on category and type of split.
9. While making the transactions there is also a feature where the person making the transaction may or may not be a part of the transaction.

## Additional Feature

The user can search for friends and send them friend request so that he can add them to transactions.

### Importance:

This feature is necessary so that a person is added to the transactions by only some known users that have been friended by the user and none can add someone who is unknown to prevent fraudulent transactions.

### Implementation

The user is able to search for friends and then send them friend requests.
The user can view all the requests that he had sent in the requests pending sent by you tab and the requests which you have received are displayed under the requests pending by you tab.
The user can accept the request so that both users become friends and now can make transactions which can include both of them.
