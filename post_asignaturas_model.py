from backend.models.post_connection_pool import PostgreSQLPool

class AsignaturaModel:
    def __init__(self):        
        self.post_pool = PostgreSQLPool()

    def get_asignatura(self, asignatura_codigo):    
        params = {'codigo' : asignatura_codigo}      
        rv = self.post_pool.execute("SELECT * from asignaturas where codigo=%(codigo)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'codigo': result[0], 'nombre': result[1], 'semestre': result[2], 'carrera': result[3]}
            data.append(content)
            content = {}
        return data

    def get_asignaturas(self):  
        rv = self.post_pool.execute("SELECT * from asignaturas")  
        data = []
        content = {}
        for result in rv:
            content = {'codigo': result[0], 'nombre': result[1], 'semestre': result[2], 'carrera': result[3]}
            data.append(content)
            content = {}
        return data

    def create_asignatura(self, nombre, semestre, carrera):    
        data = {
            'nombre' : nombre,
            'semestre': semestre,
            'carrera': carrera
        }  
        query = """insert into asignaturas (nombre, semestre, carrera) 
            values (%(nombre)s, %(semestre)s, %(carrera)s)"""    
        cursor = self.post_pool.execute(query, data, commit=True)   
        return data

    def update_asignatura(self, codigo, nombre, semestre, carrera):    
        data = {
            'codigo' : codigo,
            'nombre' : nombre,
            'semestre': semestre,
            'carrera': carrera
        }  
        query = """update asignaturas set nombre = %(nombre)s, semestre = %(semestre)s,
                    carrera = %(carrera)s where codigo = %(codigo)s"""    
        cursor = self.post_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_asignatura(self, codigo):    
        params = {'codigo' : codigo}      
        query = """delete from asignaturas where codigo = %(codigo)s"""    
        self.post_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 

"""if __name__ == "__main__":    
    pm = AsignaturaModel()     
    print(pm.create_asignatura('Construccion de Software', '5', 'Ingenieria de Software')) """

