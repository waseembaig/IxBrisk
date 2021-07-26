import json
import re
from brisk_ixload.timer import Timer


class chassis(object):
    """Transforms OpenAPI objects into IxLoad objects
    - chassis
    Args
    ----
    - ixloadapi (Api): instance of the Api class
    """
    
    def __init__(self, ixloadapi):
        self._api = ixloadapi
    
    def config(self):
        """Transform config.network into IxLoad.network
        1) create a network for every config.scenarios.networks that is not present in IxLoad
        2) set config.networks[].name to /network -name using rest call
        """
        self._chassis = self._api.brisk_config.chassis
        with Timer(self._api, "chassis Configuration"):
            for chassis in self._chassis:
                self._create_chassis(chassis)
    
    def _create_chassis(self, chassisChain):
        """Add any network to the api server that do not already exist
        """
        chassisChain.url  = self._api._ixload + chassisChain.url
        payload = self._api._set_payload(chassisChain)
        if payload:
            response= self._api._request('POST', chassisChain.url, payload)
            chassisChain.url = chassisChain.url + response + "/"
            url = chassisChain.url + "operations/refreshConnection"
            payload1 = {}
            reply = self._api._request('POST', url, payload1, option=1)
            self._api._wait_for_action_to_finish(reply, url)

        
