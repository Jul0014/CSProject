from backend.models.post_connection_pool import PostgreSQLPool

class SalonModel:
    def __init__(self):        
        self.post_pool = PostgreSQLPool()

    def get_salon(self, salon_codigo):    
        params = {'codigo' : salon_codigo}      
        rv = self.post_pool.execute("SELECT * from salones where codigo=%(codigo)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'codigo': result[0], 'pabellon': result[1], 'numero': result[2]}
            data.append(content)
            content = {}
        return data

    def get_salones(self):  
        rv = self.post_pool.execute("SELECT * from salones")  
        data = []
        content = {}
        for result in rv:
            content = {'codigo': result[0], 'pabellon': result[1], 'numero': result[2]}
            data.append(content)
            content = {}
        return data

    def create_salon(self, pabellon, numero):    
        data = {
            'pabellon' : pabellon,
            'numero': numero
        }  
        query = """insert into salones (pabellon, numero) 
            values ( %(pabellon)s, %(numero)s)"""    
        cursor = self.post_pool.execute(query, data, commit=True)   
        return data

    def update_salon(self, codigo, pabellon, numero):    
        data = {
            'codigo' : codigo,
            'pabellon' : pabellon,
            'numero': numero
        }  
        query = """update salones set pabellon = %(pabellon)s, numero = %(numero)s where codigo = %(codigo)s"""    
        cursor = self.post_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_salon(self, codigo):    
        params = {'codigo' : codigo}      
        query = """delete from salones where codigo = %(codigo)s"""    
        self.post_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 

"""if __name__ == "__main__":    
    pm = SalonModel()     
    print(pm.create_salon('A', '101')) """

