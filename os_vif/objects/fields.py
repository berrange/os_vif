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
        m = "[0-9a-f]{2}(:[0-9a-f]{2}){5}$"
        if (not isinstance(value, six.string_types) or
            not re.match(m, value.lower())):
            raise ValueError(_LE("Malformed MAC %s"), value)
        return utils.validate_and_normalize_mac(value)


class MACAddressField(object_fields.AutoTypedField):
    AUTO_TYPE = MACAddress()
