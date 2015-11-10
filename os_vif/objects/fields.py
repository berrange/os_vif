#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_versionedobjects import fields as ovo_fields

from os_vif.i18n import _LE


class MACAddress(ovo_fields.FieldType):
    @staticmethod
    def coerce(obj, attr, value):
        m = "(:[0-9a-f]{2}){6}$"
        newvalue = value.lower()
        if not re.match(m, newvalue):
            raise ValueError(_LE("Malformed MAC address %s"), value)
        return newvalue)


class MACAddressField(object_fields.AutoTypedField):
    AUTO_TYPE = MACAddress()


class PCIAddress(ovo_fields.FieldType):
    @staticmethod
    def coerce(obj, attr, value):
        m = "[0-9a-f]{1-4}:[0-9a-f]{1-2}:[0-9a-f]{1-2]:[0-9a-f]"
        newvalue = value.lower()
        if not re.match(m, newvalue):
            raise ValueError(_LE("Malformed PCI address %s"), value)
        return newvalue)


class PCIAddressField(object_fields.AutoTypedField):
    AUTO_TYPE = PCIAddress()


class VIFDirectMode(object_fields.Enum):
    VEPA = 'vepa'
    PASSTHROUGH = 'passthrough'
    BRIDGE = 'bridge'

    ALL = (VEPA, PASSTHROUGH, BRIDGE)

    def __init__(self):
        super(VIFDirectMode, self).__init__(
            valid_values=VIFDirectMode.ALL)


class VIFDirectModeField(object_fields.BaseEnumField):
    AUTO_TYPE = VIFDirectMode()
