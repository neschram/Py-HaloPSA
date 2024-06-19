"""halo_psa.params.query_params

Parameters used as query information for a request.
"""
from dataclasses import dataclass
from .utils import Param


# A
@dataclass
class ActionID(Param):
    name: str = "action_id"
    param_type: str = "query"
    data_type: type = int
    description: str = "Returns Records associated with supplied action ID"


@dataclass
class Agents(Param):
    name: str = "agents"
    param_type: str = "query"
    data_type: type = str
    param_type: str = "query"
    description: str = "Comma separated list of agent IDs."


@dataclass
class AgentOnly(Param):
    name: str = "agentonly"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Only get Records done by Agents"


@dataclass
class AppointmentsOnly(Param):
    name: str = "appointmentsonly"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Only return appointments in the response"


@dataclass
class AssetGroupID(Param):
    name: str = "assetgroup_id"
    param_type: str = "query"
    data_type: type = int
    param_type: str = "query"
    description: str = "Filter by Assets belonging to a particular Asset group"


@dataclass
class AssetTypeID(Param):
    name: str = "assettype_id"
    param_type: str = "query"
    data_type: type = int
    param_type: str = "query"
    description: str = "Filter by Assets belonging to a particular Asset Type"


@dataclass
class AttachmentType(Param):
    name: str = "type"
    param_type: str = "query"
    data_type: type = int
    param_type: str = "query"
    description: str = "Returns attachements of the specified types"


# C
@dataclass
class ClientID(Param):
    name: str = "client_id"
    param_type: str = "query"
    data_type: type = int
    param_type: str = "query"
    description: str = "Filter by Records belonging to a particular client"


@dataclass
class ContractID(Param):
    name: str = "contract_id"
    param_type: str = "query"
    data_type: type = int
    param_type: str = "query"
    description: str = "Filter by Assets assigned to a particular contract"


@dataclass
class ConversationOnly(Param):
    name: str = "conversationonly"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "'Agent to End User' conversations only"


@dataclass
class Count(Param):
    name: str = "count"
    param_type: str = "query"
    data_type: type = int
    param_type: str = "query"
    description: str = "max results to return when not using pagination"


# E
@dataclass
class EndDate(Param):
    name: str = "end_date"
    description: str = "Return Records with an end date greater than this"
    param_type: str = "query"
    data_type: type = str
    param_type: str = "query"


@dataclass
class ExcludePrivate(Param):
    name: str = "excludeprivate"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Only get public actions"


@dataclass
class ExcludeSys(Param):
    name: str = "excludesys"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "exclude system actions"


# H
@dataclass
class HideCompleted(Param):
    name: str = "hidecompleted"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Excludde completed Records from the response"


# I
@dataclass
class IncludeActive(Param):
    name: str = "includeactive"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Include active Records in the response"


@dataclass
class IncludeAttachments(Param):
    name: str = "includeattachments"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Include attachment details in the response"


@dataclass
class IncludeChilren(Param):
    name: str = "includechildren"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Include child Assets in the response"


@dataclass
class IncludeHtmlNote(Param):
    name: str = "includehtmlnote"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Include the Record note HTML as part of the response"


@dataclass
class IncludeHtmlEmail(Param):
    name: str = "includehtmlemail"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Include the Record email HTML as part of the response"


@dataclass
class IncludeInactive(Param):
    name: str = "includeinactive"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Include inactive Records in the response"


@dataclass
class ImportantOnly(Param):
    name: str = "importantonly"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Only get important Records"


@dataclass
class IsChildNotes(Param):
    name: str = "ischildnotes"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Only get actions from child Records"


# L
@dataclass
class LinkedToID(Param):
    name: str = "linkedto_id"
    param_type: str = "query"
    data_type: type = int
    param_type: str = "query"
    description: str = "Filter by Assets linked to a particular Asset"


# O
@dataclass
class Order(Param):
    name: str = "order"
    param_type: str = "query"
    data_type: type = str
    param_type: str = "query"
    description: str = "The name of the field to order by"


@dataclass
class OrderDesc(Param):
    name: str = "orderdesc"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Whether to order ascending or descending"


# P
@dataclass
class Pageinate(Param):
    name: str = "pageinate"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Whether to use Pagination in the response"


@dataclass
class PageSize(Param):
    name: str = "page_size"
    param_type: str = "query"
    data_type: type = int
    param_type: str = "query"
    description: str = "When using Pagination, the size of the page"


@dataclass
class PageNo(Param):
    name: str = "page_no"
    param_type: str = "query"
    data_type: type = int
    param_type: str = "query"
    description: str = "When using Pagination, the page number to return"


# S
@dataclass
class Search(Param):
    name: str = "search"
    param_type: str = "query"
    data_type: type = str
    param_type: str = "query"
    description: str = "Filter by Records like your search string"


@dataclass
class ShowAll(Param):
    name: str = "showall"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Admin override to return all Records"


@dataclass
class ShowAppointments(Param):
    name: str = "showappointments"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Include appointments in the response"


@dataclass
class ShowChanges(Param):
    name: str = "showchanges"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Include change requests in the response"


@dataclass
class ShowHolidays(Param):
    name: str = "showholidays"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "include the appointment type 'Holiday'"


@dataclass
class ShowProjects(Param):
    name: str = "showprojects"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Include projects in the response"


@dataclass
class ShowShifts(Param):
    name: str = "showshifts"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Include shifts in the response"


@dataclass
class SiteID(Param):
    name: str = "site_id"
    param_type: str = "query"
    data_type: type = int
    param_type: str = "query"
    description: str = "Filter Records belonging to a particular site."


@dataclass
class SlaOnly(Param):
    name: str = "slaonly"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Only get SLA hold and release actions"


@dataclass
class StartDate(Param):
    name: str = "start_date"
    param_type: str = "query"
    data_type: type = str
    param_type: str = "query"
    description: str = "filter Records by start date"


@dataclass
class SupplierOnly(Param):
    name: str = "supplieronly"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Only get actions relating to Suppliers"


# T
@dataclass
class TaskOnly(Param):
    name: str = "taskonly"
    param_type: str = "query"
    data_type: type = bool
    param_type: str = "query"
    description: str = "Only return tasks in the response"


@dataclass
class TicketID(Param):
    name: str = "ticket_id"
    param_type: str = "query"
    data_type: type = int
    param_type: str = "query"
    description: str = "Get Records for a single ticket"


@dataclass
class ToplevelID(Param):
    name: str = "toplevel_id"
    param_type: str = "query"
    data_type: type = int
    param_type: str = "query"
    description: str = "Filter Records belonging to a particular top level"


# U
@dataclass
class UniqueID(Param):
    name: str = "unique_id"
    param_type: str = "query"
    data_type: type = int
    param_type: str = "query"
    description: str = "Return Records with the specified unique ID"


@dataclass
class Username(Param):
    name: str = "username"
    param_type: str = "query"
    data_type: type = str
    description: str = "Filter Records belonging to a particular user"
