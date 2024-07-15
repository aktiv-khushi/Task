from odoo import models, fields


class SqlQuery(models.Model):
    _name = "sql.query"
    _description = "Sql query"

    name = fields.Char("Name")
    number = fields.Integer("Number")
    address = fields.Char("Address")
    email = fields.Char("Email")
    expected_salary = fields.Float("Expected Salary")
    order_id_no = fields.Integer("CustomerID")
    emp_id = fields.Integer("EmployeeID")
    city = fields.Char('City')
    order_id = fields.Many2one('order.order',"Order Id")
    order_ids = fields.Many2many('order.order', 'sql_order_rel', string='order')
















