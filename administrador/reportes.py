from .basejasperreport import BaseJasperReport

class ReporteListaTuristas(BaseJasperReport):
    report_name = 'lista_turistas'
    fecha_inicial = ''
    fecha_final = ''
    id_hotel=''

    def __init__(self, classroom, xfecha_inicio, xfecha_final, xid_hotel):
        self.classroom = classroom
        self.filename = 'reporte_lista_turistas_{}'.format('-')        
        self.fecha_inicio = xfecha_inicio
        self.fecha_final = xfecha_final
        self.id_hotel=xid_hotel    
        super(ReporteListaTuristas, self).__init__()
    def get_params(self):
        return {
            'fecha_inicio'  : self.fecha_inicio,
            'fecha_final'    : self.fecha_final, 
            'id_hotel'       : self.id_hotel            
        }
class ReportePartesHoteleras(BaseJasperReport):
    report_name = 'reportparteshoteleras'
    fecha = ''
    xid_hotel = ''

    def __init__(self, classroom, fecha, xid_hotel):
        self.classroom = classroom
        self.filename = 'reporte_partes_hoteleras_{}'.format('-')        
        self.fecha = fecha
        self.xid_hotel=xid_hotel    
        super(ReportePartesHoteleras, self).__init__()
    def get_params(self):
        return {
            'fecha'  : self.fecha,
            'xid_hotel'       : self.xid_hotel            
        }