import json
import time, re
from brisk_ixload import ixrestutils as http_transport
#import ixrestutils as http_transport
from collections import namedtuple
#import sys
#sys.path.append('C:/Users/waseebai/Documents/laptop backup/work/Ixload OpenAPi/Ixload_backup_latest/Ixload backup/brisk-main')
from brisk import briskIxload as brisk
from brisk_ixload.scenarios import scenarios 
from brisk_ixload.protocols import protocols
from brisk_ixload.chassis import chassis


class Api(brisk.Api):
    """IxNetwork implementation of the abstract-open-traffic-generator package

    Args
    ----
    - address (str): The address of the IxNetwork API Server
    - port (str): The rest port of the IxNetwork API Server
    - username (str): The username for Linux IxNetwork API Server
        This is not required when connecting to single session environments
    - password (str): The password for Linux IxNetwork API Server
        This is not required when connecting to single session environments
    """
    def __init__(self,
                 host,
                 ixload_version, 
                 username='admin',
                 password='admin',
                 gateway_port = 8080,
                 log_level='info'):
        """Create a session
        - address (str): The ip address of the TestPlatform to connect to
        where test sessions will be created or connected to.
        - port (str): The rest port of the TestPlatform to connect to.
        - username (str): The username to be used for authentication
        - password (str): The password to be used for authentication
        """
        super(Api, self).__init__(
            host='https://127.0.0.1:11009' if host is None else host
        )
        self._address, self._port = self._get_addr_port(self.host)
        self._username = username
        self._password = password
        self._host = host
        self.ixload_version = ixload_version
        self._gateway_port = gateway_port
        self._config = None
        self._assistant = None
        self._config_type = self.config()
        self.scenarios = scenarios(self)
        self.protocols = protocols(self)
        self.chassis = chassis(self)
    
    def _get_addr_port(self, host):
        items = host.split('/')
        items = items[-1].split(':')

        addr = items[0]
        if len(items) == 2:
            return addr, items[-1]
        else:
            if host.startswith('https'):
                return addr, '443'
            else:
                return addr, '80'
    @property
    def brisk_config(self):
        return self._config
        
    def set_config(self, config):
        """Set or update the configuration
        """
        try:
            if isinstance(config, (type(self._config_type),
                                    str)) is False:
                raise TypeError(
                    'The content must be of type Union[Config, str]')

            if isinstance(config, str) is True:
                config = self._config_type.deserialize(config)
            self._config_objects = {}
            self._device_encap = {}
            self._ixn_objects = {}
            self._connect()
            self._config = config
            self.chassis.config()
            self.scenarios.config()
            self.protocols.config()
            self._apply_config()
        except Exception as err:
            print(err)
    
    def _apply_config(self):
        """
            Apply configs
        """
        url = "%s/ixload/test/operations/applyConfiguration" % (self._ixload)
        payload = {}
        #import pdb; pdb.set_trace()
        reply = self._request('POST', url, payload, option=1)
        self._wait_for_action_to_finish(reply, url)
    
    def run_test(self):
        """
            start test
        """
        url = "%s/ixload/test/operations/applyConfiguration" % (self._ixload)
        payload = {}
        reply = self._request('POST', url, payload, option=1)
        self._wait_for_action_to_finish(reply, url)
        url = "%s/ixload/test/operations/runTest" % (self._ixload)
        payload = {}
        reply = self._request('POST', url, payload, option=1)
        self._wait_for_action_to_finish(reply, url)
        return (self.get_current_state())
    
    def get_current_state(self):
        '''
        This method gets the test current state. (for example - running, unconfigured, ..)
        '''
        url = "%s/ixload/test/activeTest" % (self._ixload)
        reply = self._request('GET', url, option=1)
        return reply['currentState']
    
    def strip_api_and_version_from_url(self, url):
        '''
        #remove the slash (if any) at the beginning of the url
        '''
        if url[0] == '/':
            url = url[1:]
        url_elements = url.split('/')
        if 'api' in url:
            #strip the api/v0 part of the url
            url_elements = url_elements[2:]
        return '/'.join(url_elements)
            
    def sessionAssistance(self):
        '''
        '''
        try:
            self.connection = http_transport.get_connection(self._host, self._gateway_port, http_redirect=True)
            session_url = "sessions"
            data = {"ixLoadVersion": self.ixload_version}
            data = json.dumps(data)
            reply = self.connection.http_post(url=session_url, data=data)
            if not reply.ok:
                raise Exception(reply)
            try:
                new_obj_path = reply.headers['location']
            except:
                raise Exception("Location header is not present. Please check if the action was created successfully.")
            session_id = new_obj_path.split('/')[-1]
            self._ixload = "%s/%s" % (session_url, session_id)
            start_session_url = "%s/operations/start" % (self._ixload)
            reply = self.connection.http_post(url=start_session_url, data={})
            if not reply.ok:
                raise Exception(reply.text)
            action_result_url = reply.headers.get('location')
            if action_result_url:
                action_result_url = self.strip_api_and_version_from_url(action_result_url)
                action_finished = False
                while not action_finished:
                    action_status_obj = self.connection.http_get(url=action_result_url)
                    if action_status_obj.state == 'finished':
                        if action_status_obj.status == 'Successful':
                            action_finished = True
                            self._ixload = self._ixload + '/'
                        else:
                            error_msg = "Error while executing action '%s'." % start_session_url
                            if action_status_obj.status == 'Error':
                                error_msg += action_status_obj.error
                            raise Exception(error_msg)
                    else:
                        time.sleep(0.1)
        except Exception as err:
            raise Exception(err)
        
    def _connect(self):
        """Connect to an IxNetwork API Server.
        """
        self._errors = []
        if self._assistant is None:
            self.sessionAssistance()

    def _request(self, method, url, payload=None, params=None, headers=None, option=None):
        '''
        '''
        data = json.dumps(payload)
        response = self.connection._request(method=method, url= url, data=data, params=params, headers=headers, option=option)
        return response
    
    def _wait_for_action_to_finish(self, reply_obj, action_url):
        '''
            This method waits for an action to finish executing. after a POST request is sent in order to start an action,
            The HTTP reply will contain, in the header, a 'location' field, that contains an URL.
            The action URL contains the status of the action. we perform a GET on that URL every 0.5 seconds until the action finishes with a success.
            If the action fails, we will throw an error and print the action's error message.
            Args:
            - reply_obj the reply object holding the location
            - rt_handle - the url pointing to the operation
        '''
        action_result_url = reply_obj.headers.get('location')
        if action_result_url:
            action_result_url = self.strip_api_and_version_from_url(action_result_url)
            action_finished = False
            while not action_finished:
                action_status_obj = self._request('GET', action_result_url)
                #action_status_obj = rt_handle.invoke('http_get', url=action_result_url)
                if action_status_obj.state == 'finished':
                    if action_status_obj.status == 'Successful':
                        action_finished = True
                    else:
                        error_msg = "Error while executing action '%s'." % action_url
                        if action_status_obj.status == 'Error':
                            error_msg += action_status_obj.error
                        raise Exception(error_msg)
                else:
                    time.sleep(0.1)
    
    def strip_api_and_version_from_url(self, url):
        '''
        #remove the slash (if any) at the beginning of the url
        '''
        if url[0] == '/':
            url = url[1:]
        url_elements = url.split('/')
        if 'api' in url:
            #strip the api/v0 part of the url
            url_elements = url_elements[2:]
        return '/'.join(url_elements)

    def _get_url(self, parent, child):
        '''
        '''
        try:
            pattern = re.search(r'(.*)(\{id\})(.*)', child)
            if pattern:
                url1 = parent + pattern.group(1)
                url2 = pattern.group(3)
                return (url1, url2)
        except Exception:
            raise Exception('can not get url for parent %s and child %s' % (parent, child))


    def _set_payload(self, snappi_obj):
        properties = snappi_obj._properties
        payload = {}
        for prop_name in properties:
            if prop_name != 'url' and isinstance(properties[prop_name], (str, int, float, list)):
                prop_name_new = self._convert_camel(prop_name)
                payload[prop_name_new] = properties[prop_name]
        return payload

    def _convert_camel(self, argument):
        word_regex_pattern = re.compile("[^A-Za-z]+")
        words = word_regex_pattern.split(argument)
        return "".join(w.lower() if i == 0 else w.title() for i, w in enumerate(words))

    def info(self, message):
        print ("working %s" % message)
        

    def warning(self, message):
        self._ixnetwork.warn('[ixn-otg] %s' % message)
