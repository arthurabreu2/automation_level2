from robocorp.tasks import task
from robocorp import browser
from RPA.HTTP import HTTP
from RPA.Tables import Tables

@task
def order_robots_from_RobotSpareBin():
    """
    Orders robots from RobotSpareBin Industries Inc.
    Saves the order HTML receipt as a PDF file.
    Saves the screenshot of the ordered robot.
    Embeds the screenshot of the robot to the PDF receipt.
    Creates ZIP archive of the receipts and the images.
    """
    browser.configure(
        slowmo=1000,
    )
    open_available_order_website()
    download_csv_file()
    get_orders()
    
def open_available_order_website():
    """Navigate to the given url"""
    browser.goto("https://robotsparebinindustries.com/order#/robot-order")
    
def download_csv_file():
    """Function to download the orders file"""
    http = HTTP()
    http.download("https://robotsparebinindustries.com/orders.csv")
    
def get_orders():
    """Function to read the csv file as a table and return the result"""
    tables = Tables()
    orders_table = tables.read_table_from_csv("orders.csv", header=True)
    for row in orders_table:
        print(row)
    return orders_table