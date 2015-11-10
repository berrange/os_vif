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

from oslo_versionedobjects import base
from oslo_versionedobjects import fields

class PluginConfig(base.VersionedObject):
    """Represents configuration info passed to a plugin"""
    # Version 1.0: Initial version
    VERSION = '1.0'

    fields = {
        # Name of the virtualization driver
        'virt_driver': fields.StringField(),

        # Name of the hypervisor type (when virtualization
        # driver can support multiple hypervisors)
        'hypervisor_type': fields.StringField()
    }
