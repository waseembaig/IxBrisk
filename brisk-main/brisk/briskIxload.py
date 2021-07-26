import importlib
try:
    from typing import Union, Dict, Literal, List
except ImportError:
    pass
from .briskcommon import BriskObject
from .briskcommon import BriskIter
from .briskcommon import BriskHttpTransport


class Config(BriskObject):
    __slots__ = ('_parent', '_choice')

    _TYPES = {
        'chassis': 'ChassisIter',
        'scenarios': 'ScenarioIter',
    } # type: Dict[str, str]

    def __init__(self, parent=None, choice=None):
        super(Config, self).__init__()
        self._parent = parent
        self._choice = choice

    @property
    def chassis(self):
        # type: () -> ChassisIter
        """chassis getter

        Adding chassis configuration.

        Returns: ChassisIter
        """
        return self._get_property('chassis', ChassisIter, self._parent, self._choice)

    @property
    def scenarios(self):
        # type: () -> ScenarioIter
        """scenarios getter

        The Community will be configured on the Ixload traffic generator.

        Returns: ScenarioIter
        """
        return self._get_property('scenarios', ScenarioIter, self._parent, self._choice)


class Chassis(BriskObject):
    __slots__ = ('_parent', '_choice')

    _TYPES = {} # type: Dict[str, str]

    def __init__(self, parent=None, choice=None, url=None, location=None, name=None):
        super(Chassis, self).__init__()
        self._parent = parent
        self._choice = choice
        self._set_property('url', url)
        self._set_property('location', location)
        self._set_property('name', name)

    @property
    def url(self):
        # type: () -> str
        """url getter

        url for portList. {id} is the community object ID

        Returns: str
        """
        return self._get_property('url')

    @url.setter
    def url(self, value):
        """url setter

        url for portList. {id} is the community object ID

        value: str
        """
        self._set_property('url', value)

    @property
    def location(self):
        # type: () -> str
        """location getter

        The location of a test port. It is the endpoint where packets will emit from. Test port locations can be the following:. - physical appliance with multiple ports. - physical chassis with multiple cards and ports. - local interface. The test port location format is implementation specific. Use the /results/capabilities API to determine what formats an implementation supports for the location property. Get the configured location state by using the /results/port API.

        Returns: str
        """
        return self._get_property('location')

    @location.setter
    def location(self, value):
        """location setter

        The location of a test port. It is the endpoint where packets will emit from. Test port locations can be the following:. - physical appliance with multiple ports. - physical chassis with multiple cards and ports. - local interface. The test port location format is implementation specific. Use the /results/capabilities API to determine what formats an implementation supports for the location property. Get the configured location state by using the /results/port API.

        value: str
        """
        self._set_property('location', value)

    @property
    def name(self):
        # type: () -> str
        """name getter

        The name of port. Globally unique name of an object. It also serves as the primary key for arrays of objects.

        Returns: str
        """
        return self._get_property('name')

    @name.setter
    def name(self, value):
        """name setter

        The name of port. Globally unique name of an object. It also serves as the primary key for arrays of objects.

        value: str
        """
        self._set_property('name', value)


class ChassisIter(BriskIter):
    __slots__ = ('_parent', '_choice')

    def __init__(self, parent=None, choice=None):
        super(ChassisIter, self).__init__()
        self._parent = parent
        self._choice = choice

    def __getitem__(self, key):
        # type: (str) -> Union[Chassis]
        return self._getitem(key)

    def __iter__(self):
        # type: () -> ChassisIter
        return self._iter()

    def __next__(self):
        # type: () -> Chassis
        return self._next()

    def next(self):
        # type: () -> Chassis
        return self._next()

    def chassis(self, url='ixload/chassischain/chassisList/', location=None, name=None):
        # type: (str,str,str) -> ChassisIter
        """Factory method that creates an instance of Chassis class

        An abstract test port.

        Returns: ChassisIter
        """
        item = Chassis(parent=self._parent, choice=self._choice, url=url, location=location, name=name)
        self._add(item)
        return self


class Scenario(BriskObject):
    __slots__ = ('_parent', '_choice')

    _TYPES = {
        'name': 'DevicePattern',
        'networks': 'NetworkIter',
    } # type: Dict[str, str]

    def __init__(self, parent=None, choice=None, url=None):
        super(Scenario, self).__init__()
        self._parent = parent
        self._choice = choice
        self._set_property('url', url)

    @property
    def url(self):
        # type: () -> str
        """url getter

        url for community. {id} is the community object ID

        Returns: str
        """
        return self._get_property('url')

    @url.setter
    def url(self, value):
        """url setter

        url for community. {id} is the community object ID

        value: str
        """
        self._set_property('url', value)

    @property
    def name(self):
        # type: () -> DevicePattern
        """name getter

        A container for emulated device property patterns.Media access control address (MAC) is a 48bit identifier for use as a network address. The value can be an int or a hex string with or without spaces or colons separating each byte. The min value is 0 or '00:00:00:00:00:00'. The max value is 281474976710655 or 'FF:FF:FF:FF:FF:FF'.. Globally unique name of an object. It also serves as the primary key for arrays of objects.

        Returns: DevicePattern
        """
        return self._get_property('name', DevicePattern)

    @property
    def networks(self):
        # type: () -> NetworkIter
        """networks getter

        The container for link aggregation control protocol settings.

        Returns: NetworkIter
        """
        return self._get_property('networks', NetworkIter, self._parent, self._choice)


class DevicePattern(BriskObject):
    __slots__ = ('_parent', '_choice')

    _TYPES = {
        'increment': 'DeviceCounter',
        'decrement': 'DeviceCounter',
    } # type: Dict[str, str]

    VALUE = 'value' # type: str
    VALUES = 'values' # type: str
    INCREMENT = 'increment' # type: str
    DECREMENT = 'decrement' # type: str

    def __init__(self, parent=None, choice=None):
        super(DevicePattern, self).__init__()
        self._parent = parent
        self._choice = choice

    @property
    def increment(self):
        # type: () -> DeviceCounter
        """Factory property that returns an instance of the DeviceCounter class

        An incrementing pattern.

        Returns: DeviceCounter
        """
        return self._get_property('increment', DeviceCounter, self, 'increment')

    @property
    def decrement(self):
        # type: () -> DeviceCounter
        """Factory property that returns an instance of the DeviceCounter class

        An incrementing pattern.

        Returns: DeviceCounter
        """
        return self._get_property('decrement', DeviceCounter, self, 'decrement')

    @property
    def choice(self):
        # type: () -> Union[Literal["value"], Literal["values"], Literal["increment"], Literal["decrement"], Literal["choice"], Literal["choice"], Literal["choice"]]
        """choice getter

        TBD

        Returns: Union[Literal["value"], Literal["values"], Literal["increment"], Literal["decrement"], Literal["choice"], Literal["choice"], Literal["choice"]]
        """
        return self._get_property('choice')

    @choice.setter
    def choice(self, value):
        """choice setter

        TBD

        value: Union[Literal["value"], Literal["values"], Literal["increment"], Literal["decrement"], Literal["choice"], Literal["choice"], Literal["choice"]]
        """
        self._set_property('choice', value)

    @property
    def value(self):
        # type: () -> str
        """value getter

        TBD

        Returns: str
        """
        return self._get_property('value')

    @value.setter
    def value(self, value):
        """value setter

        TBD

        value: str
        """
        self._set_property('value', value, 'value')

    @property
    def values(self):
        # type: () -> List[str]
        """values getter

        TBD

        Returns: List[str]
        """
        return self._get_property('values')

    @values.setter
    def values(self, value):
        """values setter

        TBD

        value: List[str]
        """
        self._set_property('values', value, 'values')


class DeviceCounter(BriskObject):
    __slots__ = ('_parent', '_choice')

    _TYPES = {} # type: Dict[str, str]

    def __init__(self, parent=None, choice=None, start=None, step=None):
        super(DeviceCounter, self).__init__()
        self._parent = parent
        self._choice = choice
        self._set_property('start', start)
        self._set_property('step', step)

    @property
    def start(self):
        # type: () -> str
        """start getter

        TBD

        Returns: str
        """
        return self._get_property('start')

    @start.setter
    def start(self, value):
        """start setter

        TBD

        value: str
        """
        self._set_property('start', value)

    @property
    def step(self):
        # type: () -> str
        """step getter

        TBD

        Returns: str
        """
        return self._get_property('step')

    @step.setter
    def step(self, value):
        """step setter

        TBD

        value: str
        """
        self._set_property('step', value)


class Network(BriskObject):
    __slots__ = ('_parent', '_choice')

    _TYPES = {
        'ethernet': 'EthernetIter',
        'ipv4': 'Ipv4Iter',
        'protocols': 'ProtocolIter',
        'ports': 'PortIter',
    } # type: Dict[str, str]

    def __init__(self, parent=None, choice=None, url=None, name=None, aggregation=None, lineSpeed=None):
        super(Network, self).__init__()
        self._parent = parent
        self._choice = choice
        self._set_property('url', url)
        self._set_property('name', name)
        self._set_property('aggregation', aggregation)
        self._set_property('lineSpeed', lineSpeed)

    @property
    def url(self):
        # type: () -> str
        """url getter

        url for network. {id} is the community object ID

        Returns: str
        """
        return self._get_property('url')

    @url.setter
    def url(self, value):
        """url setter

        url for network. {id} is the community object ID

        value: str
        """
        self._set_property('url', value)

    @property
    def name(self):
        # type: () -> str
        """name getter

        Name of the network.. Globally unique name of an object. It also serves as the primary key for arrays of objects.

        Returns: str
        """
        return self._get_property('name')

    @name.setter
    def name(self, value):
        """name setter

        Name of the network.. Globally unique name of an object. It also serves as the primary key for arrays of objects.

        value: str
        """
        self._set_property('name', value)

    @property
    def aggregation(self):
        # type: () -> int
        """aggregation getter

        Aggregation assigned to the network

        Returns: int
        """
        return self._get_property('aggregation')

    @aggregation.setter
    def aggregation(self, value):
        """aggregation setter

        Aggregation assigned to the network

        value: int
        """
        self._set_property('aggregation', value)

    @property
    def lineSpeed(self):
        # type: () -> str
        """lineSpeed getter

        lineSpeed assigned to the network

        Returns: str
        """
        return self._get_property('lineSpeed')

    @lineSpeed.setter
    def lineSpeed(self, value):
        """lineSpeed setter

        lineSpeed assigned to the network

        value: str
        """
        self._set_property('lineSpeed', value)

    @property
    def ethernet(self):
        # type: () -> EthernetIter
        """ethernet getter

        The Ethernet configuration such as MAC/vlan config, autonegotiation etc.

        Returns: EthernetIter
        """
        return self._get_property('ethernet', EthernetIter, self._parent, self._choice)

    @property
    def ipv4(self):
        # type: () -> Ipv4Iter
        """ipv4 getter

        The Ipv4 configs.

        Returns: Ipv4Iter
        """
        return self._get_property('ipv4', Ipv4Iter, self._parent, self._choice)

    @property
    def protocols(self):
        # type: () -> ProtocolIter
        """protocols getter

        protocol creations.

        Returns: ProtocolIter
        """
        return self._get_property('protocols', ProtocolIter, self._parent, self._choice)

    @property
    def ports(self):
        # type: () -> PortIter
        """ports getter

        port configuration

        Returns: PortIter
        """
        return self._get_property('ports', PortIter, self._parent, self._choice)


class Ethernet(BriskObject):
    __slots__ = ('_parent', '_choice')

    _TYPES = {
        'mac': 'DevicePattern',
        'mtu': 'DevicePattern',
        'incrementBy': 'DevicePattern',
        'name': 'NamedObject',
        'vlans': 'Vlans',
    } # type: Dict[str, str]

    def __init__(self, parent=None, choice=None, url=None, count=None):
        super(Ethernet, self).__init__()
        self._parent = parent
        self._choice = choice
        self._set_property('url', url)
        self._set_property('count', count)

    @property
    def url(self):
        # type: () -> str
        """url getter

        url for ethernet -> Id is the stack ID of ethernet ->http://localhost:8080/api/v0/sessions/0/ixload/test/activeTest/communityList/0/network/stack/childrenList/2/macRangeList

        Returns: str
        """
        return self._get_property('url')

    @url.setter
    def url(self, value):
        """url setter

        url for ethernet -> Id is the stack ID of ethernet ->http://localhost:8080/api/v0/sessions/0/ixload/test/activeTest/communityList/0/network/stack/childrenList/2/macRangeList

        value: str
        """
        self._set_property('url', value)

    @property
    def mac(self):
        # type: () -> DevicePattern
        """mac getter

        A container for emulated device property patterns.Media access control address (MAC) is a 48bit identifier for use as a network address. The value can be an int or a hex string with or without spaces or colons separating each byte. The min value is 0 or '00:00:00:00:00:00'. The max value is 281474976710655 or 'FF:FF:FF:FF:FF:FF'.

        Returns: DevicePattern
        """
        return self._get_property('mac', DevicePattern)

    @property
    def mtu(self):
        # type: () -> DevicePattern
        """mtu getter

        A container for emulated device property patterns.Maximum transmission unit. default is 1500

        Returns: DevicePattern
        """
        return self._get_property('mtu', DevicePattern)

    @property
    def incrementBy(self):
        # type: () -> DevicePattern
        """incrementBy getter

        A container for emulated device property patterns.List of vlans

        Returns: DevicePattern
        """
        return self._get_property('incrementBy', DevicePattern)

    @property
    def count(self):
        # type: () -> int
        """count getter

        Count for the MAC.

        Returns: int
        """
        return self._get_property('count')

    @count.setter
    def count(self, value):
        """count setter

        Count for the MAC.

        value: int
        """
        self._set_property('count', value)

    @property
    def name(self):
        # type: () -> NamedObject
        """name getter

        Name of the Mac object.. Globally unique name of an object. It also serves as the primary key for arrays of objects.

        Returns: NamedObject
        """
        return self._get_property('name', NamedObject)

    @property
    def vlans(self):
        # type: () -> Vlans
        """vlans getter

        Emulated ethernet protocol. MAC configurationsThe Ethernet configuration such as MAC/vlan config, autonegotiation etc.

        Returns: Vlans
        """
        return self._get_property('vlans', Vlans)


class NamedObject(BriskObject):
    __slots__ = ('_parent', '_choice')

    _TYPES = {} # type: Dict[str, str]

    def __init__(self, parent=None, choice=None, name=None):
        super(NamedObject, self).__init__()
        self._parent = parent
        self._choice = choice
        self._set_property('name', name)

    @property
    def name(self):
        # type: () -> str
        """name getter

        Globally unique name of an object. It also serves as the primary key for arrays of objects.

        Returns: str
        """
        return self._get_property('name')

    @name.setter
    def name(self, value):
        """name setter

        Globally unique name of an object. It also serves as the primary key for arrays of objects.

        value: str
        """
        self._set_property('name', value)


class Vlans(BriskObject):
    __slots__ = ('_parent', '_choice')

    _TYPES = {
        'vlan': 'Vlan',
    } # type: Dict[str, str]

    def __init__(self, parent=None, choice=None, name=None):
        super(Vlans, self).__init__()
        self._parent = parent
        self._choice = choice
        self._set_property('name', name)

    @property
    def vlan(self):
        # type: () -> Vlan
        """vlan getter

        Emulated ethernet protocol. MAC configurationsThe Ethernet configuration such as MAC/vlan config, autonegotiation etc.

        Returns: Vlan
        """
        return self._get_property('vlan', Vlan)

    @property
    def name(self):
        # type: () -> str
        """name getter

        Globally unique name of an object. It also serves as the primary key for arrays of objects.

        Returns: str
        """
        return self._get_property('name')

    @name.setter
    def name(self, value):
        """name setter

        Globally unique name of an object. It also serves as the primary key for arrays of objects.

        value: str
        """
        self._set_property('name', value)


class Vlan(BriskObject):
    __slots__ = ('_parent', '_choice')

    _TYPES = {
        'incrementBy': 'CommonSizeIncrement',
        'name': 'NamedObject',
    } # type: Dict[str, str]

    def __init__(self, parent=None, choice=None, url=None, uniqueCount=None):
        super(Vlan, self).__init__()
        self._parent = parent
        self._choice = choice
        self._set_property('url', url)
        self._set_property('uniqueCount', uniqueCount)

    @property
    def url(self):
        # type: () -> str
        """url getter

        url for Vlan -> Id is the stack ID of ethernet ->http://localhost:8080/api/v0/sessions/0/ixload/test/activeTest/communityList/0/network/stack/childrenList/2/vlanRangeList

        Returns: str
        """
        return self._get_property('url')

    @url.setter
    def url(self, value):
        """url setter

        url for Vlan -> Id is the stack ID of ethernet ->http://localhost:8080/api/v0/sessions/0/ixload/test/activeTest/communityList/0/network/stack/childrenList/2/vlanRangeList

        value: str
        """
        self._set_property('url', value)

    @property
    def incrementBy(self):
        # type: () -> CommonSizeIncrement
        """incrementBy getter

        A value to increment for Vlan 

        Returns: CommonSizeIncrement
        """
        return self._get_property('incrementBy', CommonSizeIncrement)

    @property
    def uniqueCount(self):
        # type: () -> int
        """uniqueCount getter

        Count for the MAC.

        Returns: int
        """
        return self._get_property('uniqueCount')

    @uniqueCount.setter
    def uniqueCount(self, value):
        """uniqueCount setter

        Count for the MAC.

        value: int
        """
        self._set_property('uniqueCount', value)

    @property
    def name(self):
        # type: () -> NamedObject
        """name getter

        Name of the Mac object.. Globally unique name of an object. It also serves as the primary key for arrays of objects.

        Returns: NamedObject
        """
        return self._get_property('name', NamedObject)


class CommonSizeIncrement(BriskObject):
    __slots__ = ('_parent', '_choice')

    _TYPES = {} # type: Dict[str, str]

    def __init__(self, parent=None, choice=None, start=None, end=None, step=None):
        super(CommonSizeIncrement, self).__init__()
        self._parent = parent
        self._choice = choice
        self._set_property('start', start)
        self._set_property('end', end)
        self._set_property('step', step)

    @property
    def start(self):
        # type: () -> int
        """start getter

        Starting frame size in bytes

        Returns: int
        """
        return self._get_property('start')

    @start.setter
    def start(self, value):
        """start setter

        Starting frame size in bytes

        value: int
        """
        self._set_property('start', value)

    @property
    def end(self):
        # type: () -> int
        """end getter

        Ending frame size in bytes

        Returns: int
        """
        return self._get_property('end')

    @end.setter
    def end(self, value):
        """end setter

        Ending frame size in bytes

        value: int
        """
        self._set_property('end', value)

    @property
    def step(self):
        # type: () -> int
        """step getter

        Step frame size in bytes

        Returns: int
        """
        return self._get_property('step')

    @step.setter
    def step(self, value):
        """step setter

        Step frame size in bytes

        value: int
        """
        self._set_property('step', value)


class EthernetIter(BriskIter):
    __slots__ = ('_parent', '_choice')

    def __init__(self, parent=None, choice=None):
        super(EthernetIter, self).__init__()
        self._parent = parent
        self._choice = choice

    def __getitem__(self, key):
        # type: (str) -> Union[Ethernet]
        return self._getitem(key)

    def __iter__(self):
        # type: () -> EthernetIter
        return self._iter()

    def __next__(self):
        # type: () -> Ethernet
        return self._next()

    def next(self):
        # type: () -> Ethernet
        return self._next()

    def ethernet(self, url='stack/childrenList/{id}/macRangeList/', count=None):
        # type: (str,int) -> EthernetIter
        """Factory method that creates an instance of Ethernet class

        Emulated ethernet protocol. MAC configurations

        Returns: EthernetIter
        """
        item = Ethernet(parent=self._parent, choice=self._choice, url=url, count=count)
        self._add(item)
        return self


class Ipv4(BriskObject):
    __slots__ = ('_parent', '_choice')

    _TYPES = {
        'address': 'DevicePattern',
        'gateway': 'DevicePattern',
        'prefix': 'DevicePattern',
    } # type: Dict[str, str]

    def __init__(self, parent=None, choice=None, url=None, count=None):
        super(Ipv4, self).__init__()
        self._parent = parent
        self._choice = choice
        self._set_property('url', url)
        self._set_property('count', count)

    @property
    def url(self):
        # type: () -> str
        """url getter

        url for ethernet -> Id is the stack ID of ethernet -> Id2 is the IPV stack objectID ->http://localhost:8080/api/v0/sessions/0/ixload/test/activeTest/communityList/0/network/stack/childrenList/2/childrenList/3/rangeList

        Returns: str
        """
        return self._get_property('url')

    @url.setter
    def url(self, value):
        """url setter

        url for ethernet -> Id is the stack ID of ethernet -> Id2 is the IPV stack objectID ->http://localhost:8080/api/v0/sessions/0/ixload/test/activeTest/communityList/0/network/stack/childrenList/2/childrenList/3/rangeList

        value: str
        """
        self._set_property('url', value)

    @property
    def address(self):
        # type: () -> DevicePattern
        """address getter

        A container for emulated device property patterns.The ipv4 address.

        Returns: DevicePattern
        """
        return self._get_property('address', DevicePattern)

    @property
    def gateway(self):
        # type: () -> DevicePattern
        """gateway getter

        A container for emulated device property patterns.The ipv4 address of the gateway.

        Returns: DevicePattern
        """
        return self._get_property('gateway', DevicePattern)

    @property
    def prefix(self):
        # type: () -> DevicePattern
        """prefix getter

        A container for emulated device property patterns.The prefix of the ipv4 address.

        Returns: DevicePattern
        """
        return self._get_property('prefix', DevicePattern)

    @property
    def count(self):
        # type: () -> int
        """count getter

        Count for the MAC.

        Returns: int
        """
        return self._get_property('count')

    @count.setter
    def count(self, value):
        """count setter

        Count for the MAC.

        value: int
        """
        self._set_property('count', value)


class Ipv4Iter(BriskIter):
    __slots__ = ('_parent', '_choice')

    def __init__(self, parent=None, choice=None):
        super(Ipv4Iter, self).__init__()
        self._parent = parent
        self._choice = choice

    def __getitem__(self, key):
        # type: (str) -> Union[Ipv4]
        return self._getitem(key)

    def __iter__(self):
        # type: () -> Ipv4Iter
        return self._iter()

    def __next__(self):
        # type: () -> Ipv4
        return self._next()

    def next(self):
        # type: () -> Ipv4
        return self._next()

    def ipv4(self, url='childrenList/{id}/rangeList', count=None):
        # type: (str,int) -> Ipv4Iter
        """Factory method that creates an instance of Ipv4 class

        Emulated ipv4 interface

        Returns: Ipv4Iter
        """
        item = Ipv4(parent=self._parent, choice=self._choice, url=url, count=count)
        self._add(item)
        return self


class Protocol(BriskObject):
    __slots__ = ('_parent', '_choice')

    _TYPES = {
        'httpclient': 'HttpclientIter',
        'httpserver': 'HttpserverIter',
        'ftpclient': 'FtpclientIter',
    } # type: Dict[str, str]

    def __init__(self, parent=None, choice=None, url=None, protocol_name=None, name=None):
        super(Protocol, self).__init__()
        self._parent = parent
        self._choice = choice
        self._set_property('url', url)
        self._set_property('protocol_name', protocol_name)
        self._set_property('name', name)

    @property
    def url(self):
        # type: () -> str
        """url getter

        url for protocol|activity list. {id} is the community object ID http://localhost:8080/api/v0/sessions/0/ixload/test/activeTest/communityList/0/activityList

        Returns: str
        """
        return self._get_property('url')

    @url.setter
    def url(self, value):
        """url setter

        url for protocol|activity list. {id} is the community object ID http://localhost:8080/api/v0/sessions/0/ixload/test/activeTest/communityList/0/activityList

        value: str
        """
        self._set_property('url', value)

    @property
    def protocol_name(self):
        # type: () -> str
        """protocol_name getter

        The unique name of a Port or Lag object that will contain the emulated interfaces and/or devices.

        Returns: str
        """
        return self._get_property('protocol_name')

    @protocol_name.setter
    def protocol_name(self, value):
        """protocol_name setter

        The unique name of a Port or Lag object that will contain the emulated interfaces and/or devices.

        value: str
        """
        self._set_property('protocol_name', value)

    @property
    def httpclient(self):
        # type: () -> HttpclientIter
        """httpclient getter

        The HTTP client protocol.

        Returns: HttpclientIter
        """
        return self._get_property('httpclient', HttpclientIter, self._parent, self._choice)

    @property
    def httpserver(self):
        # type: () -> HttpserverIter
        """httpserver getter

        The HTTP server protocol.

        Returns: HttpserverIter
        """
        return self._get_property('httpserver', HttpserverIter, self._parent, self._choice)

    @property
    def ftpclient(self):
        # type: () -> FtpclientIter
        """ftpclient getter

        The FTP client protocol.

        Returns: FtpclientIter
        """
        return self._get_property('ftpclient', FtpclientIter, self._parent, self._choice)

    @property
    def name(self):
        # type: () -> str
        """name getter

        Globally unique name of an object. It also serves as the primary key for arrays of objects.

        Returns: str
        """
        return self._get_property('name')

    @name.setter
    def name(self, value):
        """name setter

        Globally unique name of an object. It also serves as the primary key for arrays of objects.

        value: str
        """
        self._set_property('name', value)


class Httpclient(BriskObject):
    __slots__ = ('_parent', '_choice')

    _TYPES = {
        'commands': 'CommandIter',
    } # type: Dict[str, str]

    def __init__(self, parent=None, choice=None, url=None, enable_ssl=None, enable_per_conn_cookie_support=None, enable_auth=None, vlan_priority=None, validate_certificate=None, enable_decompress_support=None, enable_https_proxy=None, exact_transactions=None, name=None):
        super(Httpclient, self).__init__()
        self._parent = parent
        self._choice = choice
        self._set_property('url', url)
        self._set_property('enable_ssl', enable_ssl)
        self._set_property('enable_per_conn_cookie_support', enable_per_conn_cookie_support)
        self._set_property('enable_auth', enable_auth)
        self._set_property('vlan_priority', vlan_priority)
        self._set_property('validate_certificate', validate_certificate)
        self._set_property('enable_decompress_support', enable_decompress_support)
        self._set_property('enable_https_proxy', enable_https_proxy)
        self._set_property('exact_transactions', exact_transactions)
        self._set_property('name', name)

    @property
    def url(self):
        # type: () -> str
        """url getter

        url for HTTP. {id} is the community object ID http://localhost:8080/api/v0/sessions/0/ixload/test/activeTest/communityList/0/activityList/0/agent

        Returns: str
        """
        return self._get_property('url')

    @url.setter
    def url(self, value):
        """url setter

        url for HTTP. {id} is the community object ID http://localhost:8080/api/v0/sessions/0/ixload/test/activeTest/communityList/0/activityList/0/agent

        value: str
        """
        self._set_property('url', value)

    @property
    def enable_ssl(self):
        # type: () -> bool
        """enable_ssl getter

        The HTTP SSL configs. It must be the enable for secure HTTP. 

        Returns: bool
        """
        return self._get_property('enable_ssl')

    @enable_ssl.setter
    def enable_ssl(self, value):
        """enable_ssl setter

        The HTTP SSL configs. It must be the enable for secure HTTP. 

        value: bool
        """
        self._set_property('enable_ssl', value)

    @property
    def enable_per_conn_cookie_support(self):
        # type: () -> bool
        """enable_per_conn_cookie_support getter

        Cookie support for per HTTP connection.

        Returns: bool
        """
        return self._get_property('enable_per_conn_cookie_support')

    @enable_per_conn_cookie_support.setter
    def enable_per_conn_cookie_support(self, value):
        """enable_per_conn_cookie_support setter

        Cookie support for per HTTP connection.

        value: bool
        """
        self._set_property('enable_per_conn_cookie_support', value)

    @property
    def enable_auth(self):
        # type: () -> bool
        """enable_auth getter

        Authentication for HTTP connection

        Returns: bool
        """
        return self._get_property('enable_auth')

    @enable_auth.setter
    def enable_auth(self, value):
        """enable_auth setter

        Authentication for HTTP connection

        value: bool
        """
        self._set_property('enable_auth', value)

    @property
    def vlan_priority(self):
        # type: () -> int
        """vlan_priority getter

        Vlan Priority vlan id.

        Returns: int
        """
        return self._get_property('vlan_priority')

    @vlan_priority.setter
    def vlan_priority(self, value):
        """vlan_priority setter

        Vlan Priority vlan id.

        value: int
        """
        self._set_property('vlan_priority', value)

    @property
    def validate_certificate(self):
        # type: () -> int
        """validate_certificate getter

        Validate Certificate.

        Returns: int
        """
        return self._get_property('validate_certificate')

    @validate_certificate.setter
    def validate_certificate(self, value):
        """validate_certificate setter

        Validate Certificate.

        value: int
        """
        self._set_property('validate_certificate', value)

    @property
    def enable_decompress_support(self):
        # type: () -> int
        """enable_decompress_support getter

        enable decompress support.

        Returns: int
        """
        return self._get_property('enable_decompress_support')

    @enable_decompress_support.setter
    def enable_decompress_support(self, value):
        """enable_decompress_support setter

        enable decompress support.

        value: int
        """
        self._set_property('enable_decompress_support', value)

    @property
    def enable_https_proxy(self):
        # type: () -> int
        """enable_https_proxy getter

        enable Http proxy.

        Returns: int
        """
        return self._get_property('enable_https_proxy')

    @enable_https_proxy.setter
    def enable_https_proxy(self, value):
        """enable_https_proxy setter

        enable Http proxy.

        value: int
        """
        self._set_property('enable_https_proxy', value)

    @property
    def exact_transactions(self):
        # type: () -> int
        """exact_transactions getter

        exact transactions.

        Returns: int
        """
        return self._get_property('exact_transactions')

    @exact_transactions.setter
    def exact_transactions(self, value):
        """exact_transactions setter

        exact transactions.

        value: int
        """
        self._set_property('exact_transactions', value)

    @property
    def commands(self):
        # type: () -> CommandIter
        """commands getter

        The HTTP commands configs.

        Returns: CommandIter
        """
        return self._get_property('commands', CommandIter, self._parent, self._choice)

    @property
    def name(self):
        # type: () -> str
        """name getter

        Globally unique name of an object. It also serves as the primary key for arrays of objects.

        Returns: str
        """
        return self._get_property('name')

    @name.setter
    def name(self, value):
        """name setter

        Globally unique name of an object. It also serves as the primary key for arrays of objects.

        value: str
        """
        self._set_property('name', value)


class Command(BriskObject):
    __slots__ = ('_parent', '_choice')

    _TYPES = {} # type: Dict[str, str]

    def __init__(self, parent=None, choice=None, url=None, command_type=None, profile=None, enable_di=None, destination=None, page_object=None):
        super(Command, self).__init__()
        self._parent = parent
        self._choice = choice
        self._set_property('url', url)
        self._set_property('command_type', command_type)
        self._set_property('profile', profile)
        self._set_property('enable_di', enable_di)
        self._set_property('destination', destination)
        self._set_property('page_object', page_object)

    @property
    def url(self):
        # type: () -> str
        """url getter

        url for ethernet -> Id is the stack ID of ethernet -> Id2 is the IPV stack objectID ->http://localhost:8080/api/v0/sessions/11/ixload/test/activeTest/communityList/0/activityList/0/agent/actionList

        Returns: str
        """
        return self._get_property('url')

    @url.setter
    def url(self, value):
        """url setter

        url for ethernet -> Id is the stack ID of ethernet -> Id2 is the IPV stack objectID ->http://localhost:8080/api/v0/sessions/11/ixload/test/activeTest/communityList/0/activityList/0/agent/actionList

        value: str
        """
        self._set_property('url', value)

    @property
    def command_type(self):
        # type: () -> str
        """command_type getter

        The ipv4 address.

        Returns: str
        """
        return self._get_property('command_type')

    @command_type.setter
    def command_type(self, value):
        """command_type setter

        The ipv4 address.

        value: str
        """
        self._set_property('command_type', value)

    @property
    def profile(self):
        # type: () -> int
        """profile getter

        Count for the MAC.

        Returns: int
        """
        return self._get_property('profile')

    @profile.setter
    def profile(self, value):
        """profile setter

        Count for the MAC.

        value: int
        """
        self._set_property('profile', value)

    @property
    def enable_di(self):
        # type: () -> int
        """enable_di getter

        The ipv4 address of the gateway.

        Returns: int
        """
        return self._get_property('enable_di')

    @enable_di.setter
    def enable_di(self, value):
        """enable_di setter

        The ipv4 address of the gateway.

        value: int
        """
        self._set_property('enable_di', value)

    @property
    def destination(self):
        # type: () -> str
        """destination getter

        The prefix of the ipv4 address.

        Returns: str
        """
        return self._get_property('destination')

    @destination.setter
    def destination(self, value):
        """destination setter

        The prefix of the ipv4 address.

        value: str
        """
        self._set_property('destination', value)

    @property
    def page_object(self):
        # type: () -> str
        """page_object getter

        Count for the MAC.

        Returns: str
        """
        return self._get_property('page_object')

    @page_object.setter
    def page_object(self, value):
        """page_object setter

        Count for the MAC.

        value: str
        """
        self._set_property('page_object', value)


class CommandIter(BriskIter):
    __slots__ = ('_parent', '_choice')

    def __init__(self, parent=None, choice=None):
        super(CommandIter, self).__init__()
        self._parent = parent
        self._choice = choice

    def __getitem__(self, key):
        # type: (str) -> Union[Command]
        return self._getitem(key)

    def __iter__(self):
        # type: () -> CommandIter
        return self._iter()

    def __next__(self):
        # type: () -> Command
        return self._next()

    def next(self):
        # type: () -> Command
        return self._next()

    def command(self, url='actionList/', command_type=None, profile=-1, enable_di=0, destination=None, page_object=None):
        # type: (str,str,int,int,str,str) -> CommandIter
        """Factory method that creates an instance of Command class

        Commands config such GET, PUT 

        Returns: CommandIter
        """
        item = Command(parent=self._parent, choice=self._choice, url=url, command_type=command_type, profile=profile, enable_di=enable_di, destination=destination, page_object=page_object)
        self._add(item)
        return self


class HttpclientIter(BriskIter):
    __slots__ = ('_parent', '_choice')

    def __init__(self, parent=None, choice=None):
        super(HttpclientIter, self).__init__()
        self._parent = parent
        self._choice = choice

    def __getitem__(self, key):
        # type: (str) -> Union[Httpclient]
        return self._getitem(key)

    def __iter__(self):
        # type: () -> HttpclientIter
        return self._iter()

    def __next__(self):
        # type: () -> Httpclient
        return self._next()

    def next(self):
        # type: () -> Httpclient
        return self._next()

    def httpclient(self, url='agent/', enable_ssl=False, enable_per_conn_cookie_support=False, enable_auth=False, vlan_priority=None, validate_certificate=None, enable_decompress_support=None, enable_https_proxy=None, exact_transactions=None, name=None):
        # type: (str,bool,bool,bool,int,int,int,int,int,str) -> HttpclientIter
        """Factory method that creates an instance of Httpclient class

        Emulated HTTP Client

        Returns: HttpclientIter
        """
        item = Httpclient(parent=self._parent, choice=self._choice, url=url, enable_ssl=enable_ssl, enable_per_conn_cookie_support=enable_per_conn_cookie_support, enable_auth=enable_auth, vlan_priority=vlan_priority, validate_certificate=validate_certificate, enable_decompress_support=enable_decompress_support, enable_https_proxy=enable_https_proxy, exact_transactions=exact_transactions, name=name)
        self._add(item)
        return self


class Httpserver(BriskObject):
    __slots__ = ('_parent', '_choice')

    _TYPES = {} # type: Dict[str, str]

    def __init__(self, parent=None, choice=None, url=None, enable_ssl_send_close_notify=None, disable_mac_validation=None, enable_esm=None, vlan_priority=None, validate_certificate=None, enable_hTTP2=None, enable_tos=None, precedence_tOS=None, name=None):
        super(Httpserver, self).__init__()
        self._parent = parent
        self._choice = choice
        self._set_property('url', url)
        self._set_property('enable_ssl_send_close_notify', enable_ssl_send_close_notify)
        self._set_property('disable_mac_validation', disable_mac_validation)
        self._set_property('enable_esm', enable_esm)
        self._set_property('vlan_priority', vlan_priority)
        self._set_property('validate_certificate', validate_certificate)
        self._set_property('enable_hTTP2', enable_hTTP2)
        self._set_property('enable_tos', enable_tos)
        self._set_property('precedence_tOS', precedence_tOS)
        self._set_property('name', name)

    @property
    def url(self):
        # type: () -> str
        """url getter

        url for HTTP. {id} is the community object ID http://localhost:8080/api/v0/sessions/0/ixload/test/activeTest/communityList/0/activityList/0/agent

        Returns: str
        """
        return self._get_property('url')

    @url.setter
    def url(self, value):
        """url setter

        url for HTTP. {id} is the community object ID http://localhost:8080/api/v0/sessions/0/ixload/test/activeTest/communityList/0/activityList/0/agent

        value: str
        """
        self._set_property('url', value)

    @property
    def enable_ssl_send_close_notify(self):
        # type: () -> bool
        """enable_ssl_send_close_notify getter

        The HTTP SSL configs. It must be the enable for secure HTTP. 

        Returns: bool
        """
        return self._get_property('enable_ssl_send_close_notify')

    @enable_ssl_send_close_notify.setter
    def enable_ssl_send_close_notify(self, value):
        """enable_ssl_send_close_notify setter

        The HTTP SSL configs. It must be the enable for secure HTTP. 

        value: bool
        """
        self._set_property('enable_ssl_send_close_notify', value)

    @property
    def disable_mac_validation(self):
        # type: () -> bool
        """disable_mac_validation getter

        Cookie support for per HTTP connection.

        Returns: bool
        """
        return self._get_property('disable_mac_validation')

    @disable_mac_validation.setter
    def disable_mac_validation(self, value):
        """disable_mac_validation setter

        Cookie support for per HTTP connection.

        value: bool
        """
        self._set_property('disable_mac_validation', value)

    @property
    def enable_esm(self):
        # type: () -> bool
        """enable_esm getter

        Authentication for HTTP connection

        Returns: bool
        """
        return self._get_property('enable_esm')

    @enable_esm.setter
    def enable_esm(self, value):
        """enable_esm setter

        Authentication for HTTP connection

        value: bool
        """
        self._set_property('enable_esm', value)

    @property
    def vlan_priority(self):
        # type: () -> int
        """vlan_priority getter

        Vlan Priority vlan id.

        Returns: int
        """
        return self._get_property('vlan_priority')

    @vlan_priority.setter
    def vlan_priority(self, value):
        """vlan_priority setter

        Vlan Priority vlan id.

        value: int
        """
        self._set_property('vlan_priority', value)

    @property
    def validate_certificate(self):
        # type: () -> int
        """validate_certificate getter

        Validate Certificate.

        Returns: int
        """
        return self._get_property('validate_certificate')

    @validate_certificate.setter
    def validate_certificate(self, value):
        """validate_certificate setter

        Validate Certificate.

        value: int
        """
        self._set_property('validate_certificate', value)

    @property
    def enable_hTTP2(self):
        # type: () -> int
        """enable_hTTP2 getter

        enable decompress support.

        Returns: int
        """
        return self._get_property('enable_hTTP2')

    @enable_hTTP2.setter
    def enable_hTTP2(self, value):
        """enable_hTTP2 setter

        enable decompress support.

        value: int
        """
        self._set_property('enable_hTTP2', value)

    @property
    def enable_tos(self):
        # type: () -> int
        """enable_tos getter

        enable Http proxy.

        Returns: int
        """
        return self._get_property('enable_tos')

    @enable_tos.setter
    def enable_tos(self, value):
        """enable_tos setter

        enable Http proxy.

        value: int
        """
        self._set_property('enable_tos', value)

    @property
    def precedence_tOS(self):
        # type: () -> int
        """precedence_tOS getter

        exact transactions.

        Returns: int
        """
        return self._get_property('precedence_tOS')

    @precedence_tOS.setter
    def precedence_tOS(self, value):
        """precedence_tOS setter

        exact transactions.

        value: int
        """
        self._set_property('precedence_tOS', value)

    @property
    def name(self):
        # type: () -> str
        """name getter

        Globally unique name of an object. It also serves as the primary key for arrays of objects.

        Returns: str
        """
        return self._get_property('name')

    @name.setter
    def name(self, value):
        """name setter

        Globally unique name of an object. It also serves as the primary key for arrays of objects.

        value: str
        """
        self._set_property('name', value)


class HttpserverIter(BriskIter):
    __slots__ = ('_parent', '_choice')

    def __init__(self, parent=None, choice=None):
        super(HttpserverIter, self).__init__()
        self._parent = parent
        self._choice = choice

    def __getitem__(self, key):
        # type: (str) -> Union[Httpserver]
        return self._getitem(key)

    def __iter__(self):
        # type: () -> HttpserverIter
        return self._iter()

    def __next__(self):
        # type: () -> Httpserver
        return self._next()

    def next(self):
        # type: () -> Httpserver
        return self._next()

    def httpserver(self, url='agent/', enable_ssl_send_close_notify=False, disable_mac_validation=False, enable_esm=False, vlan_priority=None, validate_certificate=None, enable_hTTP2=None, enable_tos=None, precedence_tOS=None, name=None):
        # type: (str,bool,bool,bool,int,int,int,int,int,str) -> HttpserverIter
        """Factory method that creates an instance of Httpserver class

        Emulated HTTP Client

        Returns: HttpserverIter
        """
        item = Httpserver(parent=self._parent, choice=self._choice, url=url, enable_ssl_send_close_notify=enable_ssl_send_close_notify, disable_mac_validation=disable_mac_validation, enable_esm=enable_esm, vlan_priority=vlan_priority, validate_certificate=validate_certificate, enable_hTTP2=enable_hTTP2, enable_tos=enable_tos, precedence_tOS=precedence_tOS, name=name)
        self._add(item)
        return self


class Ftpclient(BriskObject):
    __slots__ = ('_parent', '_choice')

    _TYPES = {} # type: Dict[str, str]

    def __init__(self, parent=None, choice=None, url=None, enable_ssl=None, enable_per_conn_cookie_support=None, enable_auth=None, name=None):
        super(Ftpclient, self).__init__()
        self._parent = parent
        self._choice = choice
        self._set_property('url', url)
        self._set_property('enable_ssl', enable_ssl)
        self._set_property('enable_per_conn_cookie_support', enable_per_conn_cookie_support)
        self._set_property('enable_auth', enable_auth)
        self._set_property('name', name)

    @property
    def url(self):
        # type: () -> str
        """url getter

        url for HTTP. {id} is the community object ID http://localhost:8080/api/v0/sessions/0/ixload/test/activeTest/communityList/0/activityList/0/agent

        Returns: str
        """
        return self._get_property('url')

    @url.setter
    def url(self, value):
        """url setter

        url for HTTP. {id} is the community object ID http://localhost:8080/api/v0/sessions/0/ixload/test/activeTest/communityList/0/activityList/0/agent

        value: str
        """
        self._set_property('url', value)

    @property
    def enable_ssl(self):
        # type: () -> bool
        """enable_ssl getter

        The HTTP SSL configs. It must be the enable for secure HTTP. 

        Returns: bool
        """
        return self._get_property('enable_ssl')

    @enable_ssl.setter
    def enable_ssl(self, value):
        """enable_ssl setter

        The HTTP SSL configs. It must be the enable for secure HTTP. 

        value: bool
        """
        self._set_property('enable_ssl', value)

    @property
    def enable_per_conn_cookie_support(self):
        # type: () -> bool
        """enable_per_conn_cookie_support getter

        Cookie support for per HTTP connection.

        Returns: bool
        """
        return self._get_property('enable_per_conn_cookie_support')

    @enable_per_conn_cookie_support.setter
    def enable_per_conn_cookie_support(self, value):
        """enable_per_conn_cookie_support setter

        Cookie support for per HTTP connection.

        value: bool
        """
        self._set_property('enable_per_conn_cookie_support', value)

    @property
    def enable_auth(self):
        # type: () -> bool
        """enable_auth getter

        Authentication for HTTP connection

        Returns: bool
        """
        return self._get_property('enable_auth')

    @enable_auth.setter
    def enable_auth(self, value):
        """enable_auth setter

        Authentication for HTTP connection

        value: bool
        """
        self._set_property('enable_auth', value)

    @property
    def name(self):
        # type: () -> str
        """name getter

        Globally unique name of an object. It also serves as the primary key for arrays of objects.

        Returns: str
        """
        return self._get_property('name')

    @name.setter
    def name(self, value):
        """name setter

        Globally unique name of an object. It also serves as the primary key for arrays of objects.

        value: str
        """
        self._set_property('name', value)


class FtpclientIter(BriskIter):
    __slots__ = ('_parent', '_choice')

    def __init__(self, parent=None, choice=None):
        super(FtpclientIter, self).__init__()
        self._parent = parent
        self._choice = choice

    def __getitem__(self, key):
        # type: (str) -> Union[Ftpclient]
        return self._getitem(key)

    def __iter__(self):
        # type: () -> FtpclientIter
        return self._iter()

    def __next__(self):
        # type: () -> Ftpclient
        return self._next()

    def next(self):
        # type: () -> Ftpclient
        return self._next()

    def ftpclient(self, url='agent', enable_ssl=False, enable_per_conn_cookie_support=False, enable_auth=False, name=None):
        # type: (str,bool,bool,bool,str) -> FtpclientIter
        """Factory method that creates an instance of Ftpclient class

        Emulated FTP Client

        Returns: FtpclientIter
        """
        item = Ftpclient(parent=self._parent, choice=self._choice, url=url, enable_ssl=enable_ssl, enable_per_conn_cookie_support=enable_per_conn_cookie_support, enable_auth=enable_auth, name=name)
        self._add(item)
        return self


class ProtocolIter(BriskIter):
    __slots__ = ('_parent', '_choice')

    def __init__(self, parent=None, choice=None):
        super(ProtocolIter, self).__init__()
        self._parent = parent
        self._choice = choice

    def __getitem__(self, key):
        # type: (str) -> Union[Protocol]
        return self._getitem(key)

    def __iter__(self):
        # type: () -> ProtocolIter
        return self._iter()

    def __next__(self):
        # type: () -> Protocol
        return self._next()

    def next(self):
        # type: () -> Protocol
        return self._next()

    def protocol(self, url='activityList/{id}/', protocol_name=None, name=None):
        # type: (str,str,str) -> ProtocolIter
        """Factory method that creates an instance of Protocol class

        A container for emulated protocol devices.

        Returns: ProtocolIter
        """
        item = Protocol(parent=self._parent, choice=self._choice, url=url, protocol_name=protocol_name, name=name)
        self._add(item)
        return self


class Port(BriskObject):
    __slots__ = ('_parent', '_choice')

    _TYPES = {} # type: Dict[str, str]

    def __init__(self, parent=None, choice=None, url=None, chassis_id=None, card_id=None, port_id=None, name=None):
        super(Port, self).__init__()
        self._parent = parent
        self._choice = choice
        self._set_property('url', url)
        self._set_property('chassis_id', chassis_id)
        self._set_property('card_id', card_id)
        self._set_property('port_id', port_id)
        self._set_property('name', name)

    @property
    def url(self):
        # type: () -> str
        """url getter

        url for portList. {id} is the community object ID

        Returns: str
        """
        return self._get_property('url')

    @url.setter
    def url(self, value):
        """url setter

        url for portList. {id} is the community object ID

        value: str
        """
        self._set_property('url', value)

    @property
    def chassis_id(self):
        # type: () -> int
        """chassis_id getter

        The chassis id of port

        Returns: int
        """
        return self._get_property('chassis_id')

    @chassis_id.setter
    def chassis_id(self, value):
        """chassis_id setter

        The chassis id of port

        value: int
        """
        self._set_property('chassis_id', value)

    @property
    def card_id(self):
        # type: () -> int
        """card_id getter

        The card id of port

        Returns: int
        """
        return self._get_property('card_id')

    @card_id.setter
    def card_id(self, value):
        """card_id setter

        The card id of port

        value: int
        """
        self._set_property('card_id', value)

    @property
    def port_id(self):
        # type: () -> int
        """port_id getter

        The port id of port

        Returns: int
        """
        return self._get_property('port_id')

    @port_id.setter
    def port_id(self, value):
        """port_id setter

        The port id of port

        value: int
        """
        self._set_property('port_id', value)

    @property
    def name(self):
        # type: () -> str
        """name getter

        Globally unique name of an object. It also serves as the primary key for arrays of objects.

        Returns: str
        """
        return self._get_property('name')

    @name.setter
    def name(self, value):
        """name setter

        Globally unique name of an object. It also serves as the primary key for arrays of objects.

        value: str
        """
        self._set_property('name', value)


class PortIter(BriskIter):
    __slots__ = ('_parent', '_choice')

    def __init__(self, parent=None, choice=None):
        super(PortIter, self).__init__()
        self._parent = parent
        self._choice = choice

    def __getitem__(self, key):
        # type: (str) -> Union[Port]
        return self._getitem(key)

    def __iter__(self):
        # type: () -> PortIter
        return self._iter()

    def __next__(self):
        # type: () -> Port
        return self._next()

    def next(self):
        # type: () -> Port
        return self._next()

    def port(self, url='portList/', chassis_id=None, card_id=None, port_id=None, name=None):
        # type: (str,int,int,int,str) -> PortIter
        """Factory method that creates an instance of Port class

        An abstract test port.

        Returns: PortIter
        """
        item = Port(parent=self._parent, choice=self._choice, url=url, chassis_id=chassis_id, card_id=card_id, port_id=port_id, name=name)
        self._add(item)
        return self


class NetworkIter(BriskIter):
    __slots__ = ('_parent', '_choice')

    def __init__(self, parent=None, choice=None):
        super(NetworkIter, self).__init__()
        self._parent = parent
        self._choice = choice

    def __getitem__(self, key):
        # type: (str) -> Union[Network]
        return self._getitem(key)

    def __iter__(self):
        # type: () -> NetworkIter
        return self._iter()

    def __next__(self):
        # type: () -> Network
        return self._next()

    def next(self):
        # type: () -> Network
        return self._next()

    def network(self, url='network/', name=None, aggregation=None, lineSpeed=None):
        # type: (str,str,int,str) -> NetworkIter
        """Factory method that creates an instance of Network class

        Network configuration for communities

        Returns: NetworkIter
        """
        item = Network(parent=self._parent, choice=self._choice, url=url, name=name, aggregation=aggregation, lineSpeed=lineSpeed)
        self._add(item)
        return self


class ScenarioIter(BriskIter):
    __slots__ = ('_parent', '_choice')

    def __init__(self, parent=None, choice=None):
        super(ScenarioIter, self).__init__()
        self._parent = parent
        self._choice = choice

    def __getitem__(self, key):
        # type: (str) -> Union[Scenario]
        return self._getitem(key)

    def __iter__(self):
        # type: () -> ScenarioIter
        return self._iter()

    def __next__(self):
        # type: () -> Scenario
        return self._next()

    def next(self):
        # type: () -> Scenario
        return self._next()

    def scenario(self, url='ixload/test/activeTest/communityList/{id}/'):
        # type: (str) -> ScenarioIter
        """Factory method that creates an instance of Scenario class

        A container for Tests settings.

        Returns: ScenarioIter
        """
        item = Scenario(parent=self._parent, choice=self._choice, url=url)
        self._add(item)
        return self


class Details(BriskObject):
    __slots__ = ('_parent', '_choice')

    _TYPES = {} # type: Dict[str, str]

    def __init__(self, parent=None, choice=None, errors=None, warnings=None):
        super(Details, self).__init__()
        self._parent = parent
        self._choice = choice
        self._set_property('errors', errors)
        self._set_property('warnings', warnings)

    @property
    def errors(self):
        # type: () -> List[str]
        """errors getter

        A list of any errors that may have occurred while executing the request.

        Returns: List[str]
        """
        return self._get_property('errors')

    @errors.setter
    def errors(self, value):
        """errors setter

        A list of any errors that may have occurred while executing the request.

        value: List[str]
        """
        self._set_property('errors', value)

    @property
    def warnings(self):
        # type: () -> List[str]
        """warnings getter

        A list of any warnings generated while executing the request.

        Returns: List[str]
        """
        return self._get_property('warnings')

    @warnings.setter
    def warnings(self, value):
        """warnings setter

        A list of any warnings generated while executing the request.

        value: List[str]
        """
        self._set_property('warnings', value)


class Api(object):
    """Brisk Abstract API
    """

    def __init__(self, host=None):
        self.host = host if host else "https://localhost"

    def set_config(self, payload):
        """POST /config

        Sets configuration resources on the traffic generator.

        Return: details
        """
        raise NotImplementedError("set_config")

    def config(self):
        """Factory method that creates an instance of Config

        Return: Config
        """
        return Config()

    def details(self):
        """Factory method that creates an instance of Details

        Return: Details
        """
        return Details()


class HttpApi(Api):
    """Brisk HTTP API
    """
    def __init__(self, host=None):
        super(HttpApi, self).__init__(host=host)
        self._transport = BriskHttpTransport(host=self.host)

    def set_config(self, payload):
        """POST /config

        Sets configuration resources on the traffic generator.

        Return: details
        """
        return self._transport.send_recv(
            "post",
            "/config",
            payload=payload,
            return_object=self.details(),
        )


def api(host=None, version=None):
    if version is None:
        return HttpApi(host=host)

    try:
        lib = importlib.import_module("brisk_ixload")
        return lib.Api(host=host, ixload_version=version)
    except ImportError as err:
        msg = "Brisk extension %s is not installed or invalid: %s"
        raise Exception(msg % (ext, err))
