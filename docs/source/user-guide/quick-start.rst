Quick Start
###########

Clone the module
****************

1. Clone the repository from `Git Hub <https://github.com/neschram/Py-HaloPSA>`_ into your
   project.
2. with your environment enabled, import the requirements from `./requirements.txt`.
3. Import the module into your project: ``from Py-HaloPSA.halo_api import halo``
4. Authenticate the API: ``halo.connect()``
5. Instantiate a Resource: ``halo.Client._get_all()``
6. Interact with Resource data: ``halo.Clients.INSTANCES``