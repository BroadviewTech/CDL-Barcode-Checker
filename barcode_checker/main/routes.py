from flask import render_template, request, Blueprint
from barcode_checker.models import (
    OrderPackageItems,
    Orders,
    ClientMaster
)
from barcode_checker import db

import os

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')


@main.route("/lookup", methods=["POST"])
def lookup_rte():
    barcode = request.form.get("barcode")
   
    dbquery = db.session.query(
        ClientMaster.AccountNo,
        ClientMaster.CompanyName,
        Orders.OrderTrackingID,
        Orders.ClientRefNo,
        OrderPackageItems.RefNo, 
        Orders.DSortCode)
    dbquery = dbquery.join(Orders, OrderPackageItems.OrderTrackingID == Orders.OrderTrackingID)
    dbquery = dbquery.join(ClientMaster, Orders.ClientID == ClientMaster.ClientID)
    dbquery = dbquery.filter(OrderPackageItems.RefNo == barcode)
    dbquery = dbquery.filter(Orders.Status == 'N')
    records = [r._asdict() for r in dbquery.all()]
    if len(records) > 0: 
        res = records[0]
        return render_template('record.html', account_no = res['AccountNo'], company_name=res['CompanyName'], order_tracking_id=res['OrderTrackingID'], client_ref_no=res['ClientRefNo'], refNo=res['RefNo'], sort_code=res['DSortCode'])
    return render_template('no_record.html')
    
