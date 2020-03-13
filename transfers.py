# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, _



class Transfers(models.Model):
     _name ="transfers.name"
     _description ="Transfer Record"

     transfers_Name = fields.Char(string="Name", required = True)
     transfers_ISO = fields.Char(string="ISO") 
     transfers_amount = fields.Integer("Amount")
     notes = fields.Text(string ="Notes")
     image = fields.Binary(string ="Image")
