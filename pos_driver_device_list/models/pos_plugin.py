# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class PosPlugin(models.Model):
    _name = "pos.plugin"
    _description = "Point of Sale Plugins"
    _order = "last_connexion_date desc, name"

    device_type = fields.Selection(
        selection=[
            ("display", "Customer Display"),
            ("payment", "Payment Terminal"),
            ("scale", "Scale"),
            ("printer", "Printer"),
        ]
    )

    name = fields.Char(readonly=True)

    config_id = fields.Many2one(comodel_name="pos.config")

    company_id = fields.Many2one(related="config_id.company_id")

    plugin_version = fields.Char(readonly=True)

    plugin_hash = fields.Char(readonly=True)

    last_connexion_date = fields.Datetime(readonly=True)
