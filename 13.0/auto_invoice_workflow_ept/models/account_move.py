from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def prepare_payment_dict(self, work_flow_process_record):
        """
        Added By Udit
        This method will prepare payment dictionary.
        :param work_flow_process_record: It is work flow object.
        """
        return {
            'journal_id': work_flow_process_record.journal_id.id,
            'invoice_ids': [(6, 0, [self.id])],
            'communication': self.invoice_payment_ref,
            'currency_id': self.currency_id.id,
            'payment_type': 'inbound',
            'partner_id': self.commercial_partner_id.id,
            'amount': self.amount_residual,
            'payment_method_id': work_flow_process_record.inbound_payment_method_id.id,
            'partner_type': 'customer'
        }
