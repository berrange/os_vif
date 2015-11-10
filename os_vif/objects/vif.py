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

from os_vif import vnic_types
from os_vif.objects import osv_fields


class VIFBase(base.VersionedObject):
    """Represents a virtual network interface."""
    # Version 1.0: Initial version
    VERSION = '1.0'

    fields = {
        # Unique identifier of the VIF port
        'id': fields.UUIDField(),

        # The guest MAC address
        'address': osv_fields.MACAddressField(nullable=True),

        # The network to which the VIF is connected
        'network': fields.ObjectField('Network', nullable=True),

        # Name of the registered os_vif plugin
        'plugin': fields.StringField(),

        # Whether the VIF is initially online
        'active': fields.BooleanField(default=True),

        # Whether the host VIF should be preserved on unplug
        'preserve_on_delete': fields.BooleanField(default=False),

        # Port profile metadata
        'profile': fields.ObjectField("VIFProfile", nullable=True),
    }


class VIFGeneric(VIFBase):
    # For libvirt drivers, this maps to type="ethernet" which
    # just implies a bare TAP device, all setup delegated to
    # the plugin

    VERSION = VIFBase.VERSION

    fields = {
        # Name of the device to create
        'dev_name': fields.StringField()
    }


class VIFBridge(VIFBase):
    # For libvirt drivers, this maps to type='bridge'

    VERSION = VIFBase.VERSION

    fields = {
        # Name of the device to create
        'dev_name': fields.StringField()

        # Name of the bridge device to connect to
        'bridge_name': fields.StringField(),
    }


class VIFDirect(VIFBase):
    # For libvirt drivers, this maps to type='direct'

    VERSION = VIFBase.VERSION

    fields = {
        # Name of the source device to associate with (eg eth0)
        'dev_name': fields.StringField()

        # The device connection mode
        'mode': ovs_fields.VIFDirectModeField(),
    }


class VIFVHostUser(VIFBase):
    # For libvirt drivers, this maps to type='vhostuser'

    VERSION = VIFBase.VERSION

    fields = {
        # UNIX socket path
        'path': fields.StringField(),

        # UNIX socket access permissions
        'mode': fields.StringField()
    }


class VIFHostDevice(VIFBase):
    # For libvirt drivers, this maps to type='hostdev'

    VERSION = VIFBase.VERSION

    fields = {
        # The PCI address of the host device
        'dev_address': ovs_fields.PCIAddressField(),

        # The VLAN number to use
        'vlan': fields.IntegerField(),
    }


class VIFProfileBase(base.VersionedObject):
    VERSION = VIFBase.VERSION


class VIFProfile8021QBG(VIFProfile):
    VERSION = VIFBase.VERSION

    fields = {
        'manager_id': fields.IntegerField(),
        'type_id': fields.IntegerField(),
        'type_id_version': fields.IntegerField(),
        'instance_id': fields.UUIDField(),
    }


class VIFProfile8021QBH(VIFProfile):
    VERSION = VIFBase.VERSION

    fields = {
        'profile_id': fields.StringField()
    }


class VIFProfileOpenVSwitch(VIFProfile):
    VERSION = VIFBase.VERSION

    fields = {
        'interface_id': fields.UUIDField(),
        'profile_id': fields.StringField(),
    }


class VIFProfileMidonet(VIFProfile):
    VERSION = VIFBase.VERSION

    fields = {
        'interface_id': fields.UUIDField(),
    }
