# Colin's Venmo Tools
This is app is designed to be a GUI equipped toolbox for efficient usage of Venmo functionalities

## Usage
- main.py is the GUI version of the app.

## Inspiration
Inspired by a need to request 6 roommates for rent, utilities, and internet every month. I wanted to automate this process so I wouldn't need to manually make all 18 identical requests each month.

Eventually built a GUI on top, so users can be selected from a list and automation/scheduling settings can be adjusted.

## Libraries Used:
- venmo_api: https://pypi.org/project/venmo-api/
- pandas: https://pandas.pydata.org/docs/
- tkinter
- json


## Future Features:
### Default Request Groups
- Default mass request shortcuts
- Interface with scheduling menus
### Scheduling
- Scheduled payments to landlord on first of month.
- Scheduled requests to roommates a couple days before first of month.
### Data Collection and Statistics
- Tracking of fulfillment of requests, with fulfillment dates stored in a database.
- Relevant statistics of payments.