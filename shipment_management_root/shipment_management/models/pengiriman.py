from odoo import models, fields

class Pengiriman(models.Model):
    _name = 'pengiriman'
    _description = 'Pengelolaan Pengiriman'

    name = fields.Char(String='Kode pengiriman', required=True)
    tanggal_pengiriman = fields.Date(string='Tanggal Pengiriman', required=True)
    status = fields.Selection(
        selection=[
            ('pending','Pending'),
            ('approved','Approved'),
            ('rejected','Rejected')
        ],
        string='Status',
        default='pending',
        required=True,
    )
    keterangan = fields.Text(string='Keterangan')