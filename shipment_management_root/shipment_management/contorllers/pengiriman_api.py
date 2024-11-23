from odoo import http
from odoo.http import request

class PengirimanAPI(http.Controller):

    @http.route('/api/update_status',type='json',auth='public',methods=['POST'], csrf=False)
    def update_status(self,**kwargs):
        #validasi
        request_id = kwargs.get('id')
        new_status = kwargs.get('status')


        if not request_id or not new_status:
            return {'status':'error','message':'Parameter Id dan status diperlukan'}
        
        if new_status not in ['pending','approved','rejected']:
            return {'status':'error','message':'Status tidak ada'}
        
        #cari data/record berdasarkan id

        pengiriman = request.env['pengiriman'].sudo().search([('id','=', int(request_id))], limit=1)
        if not pengiriman:
            return {'status':'error','message':'Id tidak ditemukan'}
        
        #perbarui status
        pengiriman.sudo().write({'status':new_status})
        return {'status':'success','message':f'Status berhasil diperbarui menjadi {new_status}'}
    def get_pengiriman(self, id=None):
        try:
            Pengiriman = request.env['pengiriman'].sudo()

            if id:
                #mendapatkan data pengiriman berdasarkan id
                pengiriman = Pengiriman.browse(int(id))
                if not pengiriman.exist():
                    return {'status':'error','message':f'Pengiriman id {id} tidak ditemukan'}
                
                #format pengiriman data

                data = {
                    'id': pengiriman.id,
                    'name': pengiriman.name,
                    'deskripsi': pengiriman.keterangan,
                    'tanggal_pengiriman':pengiriman.tanggal_pengiriman,
                    'status':pengiriman.stats
                }
                return {'status':'success','data':data}
            else:
                #mengambil semua data pengiriman
                pengiriman_records = Pengiriman.search([])
                data = [
                    {
                        'id': record.id,
                        'name': record.name,
                        'deskripsi': record.keterangan,
                        'tanggal_pengiriman': record.tanggal_pengiriman,
                        'status': record.status
                    }
                    for record in pengiriman_records
                ]
                return {'status':'success','data':data}
        except Exception as e:
            return {
                'status':'error',
                'message':f'terjadi kesalahan: {str(e)}'
            }