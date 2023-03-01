from barcode_checker import db

class Orders(db.Model):
    __tablename__ = "Orders"
    OrderTrackingID = db.Column(db.Integer, primary_key=True)
    ClientID = db.Column(db.Integer)
    ClientRefNo = db.Column(db.String(50))
    Status = db.Column(db.String(1))
    DSortCode = db.Column(db.String(10))

class ClientMaster(db.Model):
    __tablename__ = "ClientMaster"
    ClientID = db.Column(db.Integer, primary_key=True)
    CompanyName = db.Column(db.String(75))
    AccountNo = db.Column(db.String(18))

class OrderPackageItems(db.Model):
    __tablename__ = "OrderPackageItems"
    PackageItemID = db.Column(db.Integer, primary_key=True)
    OrderTrackingID = db.Column(db.Integer)
    RefNo = db.Column(db.String(50))
    

