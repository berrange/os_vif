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

class InstanceConfig(base.VersionedObject):
    """Represents instance info passed to a plugin"""
    # Version 1.0: Initial version
    VERSION = '1.0'

    fields = {
        # Name of the instance
        'name': fields.StringField()

        # UUID of the instance
        'uuid': fields.UUIDField()

        # Human friendly name of the instance
        'display_name': fields.StringField()

        # Project id
        'project_id': fields.StringField()
    }
