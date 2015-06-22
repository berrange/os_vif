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


class VIF(base.VersionedObject):
    """Represents a virtual network interface."""
    # Version 1.0: Initial version
    VERSION = '1.0'

    fields = {
        # Unique identifier of the VIF port
        'id': fields.UUIDField(),

        # The network to which the VIF is connected
        'network': fields.ObjectField('Network', nullable=True),

        # MAC address
        # TODO(berrange) how about a MACAddressField() type
        'address': fields.StringField(nullable=True),

        # Whether the VIF is initially up. If False, we must
        # wait for an event notification of online status
        'active': fields.BooleanField(default=True),

        # Whether the VIF was created by an external entity,
        # so Nova should avoid deleting VIF on instance
        # deletion
        'preserve_on_delete': fields.BooleanField(default=False),

        # Name of the plugin to use for performing host OS
        # setup / teardown actions
        'plugin': fields.StringField()
    }


class VIFTap(VIF):
    # Maps to libvirt type="ethernet" which just implies a
    # bare TAP device, all setup delegated to plugin

    fields = {
        # Name of the TAP device to create
        'devname': fields.StringField()
    }


class VIFBridge(VIFTap):
    # Maps to libvirt type='bridge'

    fields = {
        # Name of the bridge device to connect to
        'brname': fields.StringField(),

        # Whether the bridge device should be automatically
        # created if not already present
        'autocreate': fields.BooleanField(),
    }


class VIFOpenVSwitch(VIFBridge):
    # Maps to libvirt type='bridge' with openvswitch port profile

    fields = {
        'profileID': fields.StringField(),

        'interfaceID': fields.UUIDField(nullable=True)
    }


class VIFMidonet(VIFBridge):
    # Maps to libvirt type='bridge' with midonet port profile

    fields = {
        'interfaceID': fields.UUIDField(nullable=True)
    }


class VIFHostDevice(VIF):
    # Abstract base

    fields = {
        # The PCI address of the device to assign
        # TODO(berrange): should be a fields.PCIAddressField()
        'address': fields.StringField()

        # The VLAN number to configure
        'vlan': fields.IntegerField()
    }


class VIFHostDeviceDirect(VIFHostDevice):
    # Maps to libvirt type='direct' with mode='passthrough'
    pass


class VIFHostDeviceAssigned(VIFHostDevice):
    # Maps to libvirt hostdev (ie PCI device assignment)
    pass


class VIFDirect(VIF):
    # Abstract base

    fields = {
        # Name of the ethernet device to associate with
        'devname': fields.StringField()
    }


class VIFDirect801QBG(VIFDirect):
    fields = {
        'managerID': fields.IntegerField(nullable=True),

        'typeID': fields.IntegerField(nullable=True),

        'typeIDVersion': fields.IntegerField(nullable=True),

        'instanceID': fields.UUIDField(nullable=True),
    }


class VIFDirect801QBH(VIFDirect):

    fields = {
        'profileID': fields.StringField(),
    }


class VIFVHostUser(VIF):

    fields = {
        # Path to the UNIX domain socket
        'path': fields.StringField()

        # Sharing mode for the socket
        'mode': fields.StringField()
    }


class VIFDVS(VIF):
    # Maps to VMWare DVS network...
    # unless one of the other types alreadyu has the right
    # info for vmware, and we could just use that with a
    # different plugin class provided. Unclear

    fields = {
        # TODO(berrange) figure out if any are needed
    }


class InstanceInfo(base.VersionedObject):

    """Metadata about the instance that is allowed to be used
       by the VIF plugin"""

    VERSION = "1.0"

    fields = {
        # Name of the instance
        'name': fields.StringField()

        # UUID of the instance
        'uuid': fields.UUIDField()

        # Human friendly name of the instance
        'display_name': fields.StringField()

        # Project id
        'projectid': fields.StringField()
    }
