from dataclasses import dataclass, field
from typing import List


@dataclass
class Record:
    pk_field: str = field(default="id", kw_only=True)
    name_field: str = field(default="name", kw_only=True)

    def __str__(self) -> str:
        pk: int = getattr(self, self.pk_field)
        name: str = getattr(self, self.name_field)
        return f"Record #{pk}: {name}"


@dataclass
class ClientRecord(Record):
    id: int
    name: str
    toplevel_id: int
    toplevel_name: str
    inactive: bool
    colour: str
    confirmemail: int
    actionemail: int
    clearemail: int
    messagegroup_id: int
    from_address_override: str
    override_org_logo: bool
    override_org_name: str
    override_org_address: dict
    override_org_phone: str
    override_org_email: str
    override_org_portalurl: str
    mailbox_override: int
    default_mailbox_id: int
    item_tax_code: int
    service_tax_code: int
    prepay_tax_code: int
    contract_tax_code: int
    customfields: list
    custombuttons: list
    pritech: int
    sectech: int
    accountmanagertech: int
    notes: str
    datecreated: str
    createdfrom_id: int
    prinotify: bool
    secnotify: bool
    priassign: bool
    secassign: bool
    invoiceyes: bool
    floverride: bool
    fluserdef1hide: bool
    fluserdef2hide: bool
    fluserdef3hide: bool
    fluserdef4hide: bool
    fluserdef5hide: bool
    fluserdef1mand: bool
    fluserdef2mand: bool
    fluserdef3mand: bool
    fluserdef4mand: bool
    fluserdef5mand: bool
    includeactions: bool
    needsinvoice: bool
    dontinvoice: bool
    showslaonweb: bool
    imageindex: int
    fcemail: int
    emailinvoice: bool
    dont_auto_send_invoices: bool
    defcat1: str
    defcat2: str
    monthlyreportinclude: bool
    monthlyreportemaildirect: bool
    monthlyreportemailmanager: bool
    monthlyreportshowonweb: bool
    unmatchedcombinations: int
    billforrecurringprepayamount: bool
    prepayrecurringcharge: float
    prepayrecurringhours: float
    prepayrecurringchargebp: int
    autotopupthreshhold: float
    autotopuptoamount: float
    autotopupcostperhour: float
    autotopupbyamount: float
    surchargeid: int
    billingtemplate_id: int
    isopportunity: int
    main_site_id: int
    main_site_name: str
    all_organisations_allowed: bool
    contractaccountsdesc: str
    prepayaccountsdesc: str
    popup_notes: list
    allowall_tickettypes: bool
    allowed_tickettypes: list
    allowall_category1: bool
    allowall_category2: bool
    allowall_category3: bool
    allowall_category4: bool
    alocked: bool
    allowallchargerates: bool
    excludefrominvoicesync: bool
    portal_logo: str
    override_portalcolour: bool
    portalcolour: str
    portalbackgroundimageurl: str
    ninjarmmid: int
    accountsfirstname: str
    purchase_tax_code: int
    prepayrecurringminimumdeduction: float
    prepayrecurringminimumdeductiononlyactive: bool
    prepayrecurringautomaticdeduction: float
    qbodefaulttax: int
    default_contract: int
    device42id: int
    servicenowid: str
    isnhserveremaildefault: bool
    datto_id: str
    datto_alternate_id: int
    datto_url: str
    dattocommerce_tenantid: int
    qbodefaulttaxcode: int
    qbodefaulttaxcodename: str
    connectwiseid: int
    autotaskid: int
    ateraid: int
    kashflowid: int
    website: str
    alastupdate: str
    snelstart_id: str
    syncroid: int
    hubspot_id: str
    hubspot_url: str
    hubspot_dont_sync: bool
    hubspot_archived: bool
    domain: str
    passportal_id: int
    prepayasamount: bool
    tax_number: str
    hubspot_lifecycle: str
    prepayrecurringexpirymonths: int
    defaultcontractoverride: int
    external_links: list
    liongardid: int
    default_team_to_salesrep_override: bool
    portalchatprofile: str
    trading_name: str
    salesforce_dontsync: bool
    stripe_payment_method_id: str
    servicenow_url: str
    servicenow_locale: str
    servicenow_username: str
    servicenow_assignment_group: str
    servicenow_assignment_group_name: str
    servicenow_defaultuser_id: str
    servicenow_defaultuser_name: str
    sage_business_cloud_details_id: int
    exact_division: int
    ncentral_details_id: int
    jira_url: str
    jira_username: str
    jira_servicedesk_id: str
    jira_servicedesk_name: str
    jira_user_id: str
    jira_user_name: str
    servicenow_enable_webhook: bool
    servicenow_webhook_user: int
    servicenow_webhook_tickettype: int
    sync_servicenow_attachments: int
    twilio_subaccount_name: str
    twilio_subaccount_created: bool
    override_layout_id: int
    servicenow_ticket_sync: str
    use: str
    logo: str
    xero_tenant_id: str
    accountsid: str
    overridepdftemplateinvoice: int
    client_to_invoice: int
    client_to_invoice_name: str
    itglue_id: str
    sentinel_subscription_id: str
    sentinel_workspace_name: str
    sentinel_resource_group_name: str
    default_currency_code: int
    client_to_invoice_recurring: int
    client_to_invoice_recurring_name: str
    qbo_company_id: str
    dbc_company_id: str
    stopped: int
    customertype: int
    servicenow_validated: bool
    jira_validated: bool
    ref: str
    ticket_invoices_for_each_site: bool
    is_vip: bool
    taxable: bool
    percentage_to_survey: int
    billing_plan_text: str
    overridepdftemplatequote: int


@dataclass
class ClientData:
    records: List[ClientRecord] = field(default=list())

    def add_record(self, record: ClientRecord) -> None:
        self.records.append(record)
