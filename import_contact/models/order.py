from odoo import models, fields
from datetime import date, datetime, time


class Order(models.Model):
    _name = "order.order"
    _description = "Order table"

    customer_name = fields.Char("Customer Name")
    order_id_no = fields.Integer("CustomerID")
    date = fields.Datetime("OrderDate")
    address = fields.Char("Address")
    shipping_id = fields.Float("Shipping ID")
    order_id = fields.Integer("OrderId")
    emp_id = fields.Integer("EmployeeID")
    sql_query_ids = fields.One2many('sql.query','order_id',"Sql query")