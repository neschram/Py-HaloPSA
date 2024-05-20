Clients
#######

Endpoint for Halo Client records.

.. toctree::
   :caption: Clients:

HaloPSA Client API:
*******************

GET /Client
===========

Permissions Required: ``Agent`` ``Customers Read``

Query Params:
^^^^^^^^^^^^^

`pageinate` (`bool`): Whether to use Pagination in the response

`page_size` (`int`): When using Pagination, the size of the page

`page_no` (`int`): When using Pagination, the page number to return

`order` (`str`): The name of the field to order by

`orderdesc` (`bool`): Whether to order ascending or descending

`search` (`str`): Filter by Customers like your search string

`toplevel_id` (`int`): Filter by Customers belonging to a particular top level

`includeinactive` (`bool`): Include inactive Customers in the response

`includeactive` (`bool`): Include active Customers in the response

`count` (`int`): When not using pagination, the number of results to return



ClientResource
**************

.. automodule:: halo_api.resources.clients


.. autoclass:: halo_api.resources.clients.ClientResource
   :members:
   :undoc-members:
