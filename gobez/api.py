from datetime import timedelta
from xml.dom.minidom import parseString

import frappe
from frappe import _
from frappe.integrations.frappe_providers.frappecloud_billing import (
	current_site_info,
	is_fc_site,
)
from frappe.query_builder import DocType
from frappe.translate import get_all_translations
from frappe.utils import (
	add_days,
	cint,
	date_diff,
	flt,
	format_date,
	get_datetime,
	getdate,
	now,
)
from frappe.utils.response import Response

@frappe.whitelist(allow_guest=True)
def payment_callback():
    data = frappe.form_dict
    status = data.get('status')
    ref_id = data.get('ref_id')
    tx_ref = data.get('trx_ref')

    # Verify the transaction (e.g., call gateway API)
    if status == 'success':
        # Update your document
        frappe.db.set_value('Call Back Payment', tx_ref, {
            'status': 'Paid',
            'ref_id': ref_id
        })

    frappe.respond_as_web_page('Payment Status', f'Payment {status}')
