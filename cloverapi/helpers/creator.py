class Creator(object):

    @staticmethod
    def create_customer(customer_since=None, first_name=None, last_name=None, addresses=None,metadata=None,
                        email_addresses=None, cards=None, marketing_allowed=None, merchant=None, orders=None,
                        id_number=None, phone_numbers=None):
        return {
            "customerSince": customer_since,
            "firstName": first_name,
            "lastName": last_name,
            "addresses": addresses,
            "metadata": metadata,
            "emailAddresses": email_addresses,
            "cards": cards,
            "marketingAllowed": marketing_allowed,
            "merchant": merchant,
            "orders": orders,
            "id": id_number,
            "phoneNumbers": phone_numbers
        }

    @staticmethod
    def create_address(zip_code=None, country=None, address3=None, address2=None,address1=None, city=None,
                       id_number=None, state=None):
        return {
            "zip": zip_code,
            "country": country,
            "address3": address3,
            "address2": address2,
            "city": city,
            "address1": address1,
            "id": id_number,
            "state": state
        }

    @staticmethod
    def create_email_address(email, id_number=None, verified_time=None):
        return {
            "emailAddress": email,
            "id": id_number,
            "verifiedTime": verified_time
        }

    @staticmethod
    def create_payment(modified_time=None, note=None, void_reason=None,line_item_payments=None,german_info=None,
                       cash_tendered=None,card_transaction=None, transaction_settings=None, cash_back_amount=None,
                       cash_advance_extra=None,employee=None, refunds=None,result=None,offline=None,
                       service_charge=None,tax_rates=None, created_time=None, external_payment_id=None,
                       id=None,order=None,tender=None, amount=None, tip_amount=None, doc_info=None,transaction_info=None,
                       client_created_time=None, app_tracking=None, tax_amount=None, device= None):
        return {
            "modifiedTime": modified_time,
            "note": note,
            "voidReason": void_reason,
            "lineItemPayments": line_item_payments,
            "germanInfo": german_info,
            "cashTendered": cash_tendered,
            "cardTransaction": card_transaction,
            "transactionSettings": transaction_settings,
            "cashbackAmount": cash_back_amount,
            "cashAdvanceExtra": cash_advance_extra,
            "employee": employee,
            "refunds": refunds,
            "result": result,
            "offline": offline,
            "serviceCharge": service_charge,
            "taxRates": tax_rates,
            "createdTime": created_time,
            "externalPaymentId": external_payment_id,
            "id": id,
            "order": order,
            "tender": tender,
            "amount": amount,
            "tipAmount": tip_amount,
            "docInfo": doc_info,
            "transactionInfo": transaction_info,
            "clientCreatedTime": client_created_time,
            "appTracking": app_tracking,
            "taxAmount": tax_amount,
            "device": device

        }

    @staticmethod
    def create_external_merchant(modified_time=None, merchant_ref=None, usage_flag=None, audit_user_id=None,
                                 xref_type=None, client_flag=None, created_time=None, external_merchant_number=None,
                                 audit_date=None):
        return {
            "modifiedTime": modified_time,
            "merchantRef": merchant_ref,
            "usageFlag": usage_flag,
            "auditUserId": audit_user_id,
            "xrefType": xref_type,
            "clientFlag": client_flag,
            "createdTime": created_time,
            "externalMerchantNumber": external_merchant_number,
            "auditDate": audit_date
        }

    @staticmethod
    def create_merchant_ref(merchant_id=None):
        return {
            "id": merchant_id
        }

    @staticmethod
    def create_logo(logo_filename=None, logo_type=None, url=None):
        return {
            "logoFilename": logo_filename,
            "logoType": logo_type,
            "url": url
        }

    @staticmethod
    def create_merchant_program_express(merchant_ref=None, program_code=None, key_description=None, program_code_description=None, value_description=None,
                                        value=None, key=None):
        return {
            "merchantRef": merchant_ref,
            "programCode": program_code,
            "keyDescription": key_description,
            "programCodeDescription": program_code_description,
            "valueDescription": value_description,
            "key": key,
            "value": value
        }

    @staticmethod
    def create_modifier_group(max_allowed=None, min_required=None, sort_order=None, name=None, alternate_name=None, modifier_ids=None,
                              modifier_id=None,modifiers=None,items=None,show_by_default=None):
        return {
            "maxAllowed": max_allowed,
            "minRequired": min_required,
            "sortOrder": sort_order,
            "name": name,
            "alternateName": alternate_name,
            "modifiersIds": modifier_ids,
            "id": modifier_id,
            "modifiers": modifiers,
            "items": items,
            "showByDefault": show_by_default
        }

    @staticmethod
    def create_tax_rate(is_default=None, rate=None, name=None, tax_id=None, tax_amount=None, items=None):
        return {
            "isDefault": is_default,
            "rate": rate,
            "name": name,
            "id": tax_id,
            "taxAmount": tax_amount,
            "items": items
        }