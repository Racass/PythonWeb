from MySQL.MySQLDB import mySQL

class Clientes:
    id = 0
    nome = ""
    email = ""
    fone = ""
    db = mySQL(True)
    
    def getClientes(self):
        sqlGet = f"SELECT id, nome, email, fone FROM Clientes WHERE id = {self.id}"
        oRS = self.db.execReadQuery(sqlGet)
        for result in oRS:
            self.id = result[0]
            self.nome = result[1]
            self.email = result[2]
            self.fone = result[3]
    
    def __init__(self, id = 0, nome = "", email = "", fone = ""):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone

    def delete(self):
        sqlDelete = f"DELETE FROM Clientes WHERE id = {self.id}"
        return self.db.execModQuery(sqlDelete)
    def Sync(self):
        sqlGet = f"SELECT COUNT(id) FROM Clientes WHERE id = {self.id}"
        oResultSet = self.db.execReadQuery(sqlGet)
        for x in oResultSet:
            if(x[0] > 0):
                update = f"UPDATE Clientes SET nome = '{self.nome}', email = '{self.email}', fone = '{self.fone}' WHERE id = {self.id}"
                self.db.execModQuery(update)
            else:
                insert = f"INSERT INTO Clientes (nome, email, fone) VALUES ('{self.nome}', '{self.email}', '{self.fone}')"
                self.db.execModQuery(insert)
        self.getClientes()
    def getNext(self):
        sqlGet = "SELECT COALESCE(Max(id), 0) + 1 FROM Clientes"
        oRS = self.db.execReadQuery(sqlGet)
        self.id = oRS[0][0]
        self.nome = ""
        self.fone = ""
        self.email = ""
        return oRS[0][0]