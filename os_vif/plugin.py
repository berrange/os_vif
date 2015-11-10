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

import abc

import six


class PluginVIFSupport(object):

    def __init__(self, class_name, min_version, max_version):

        self.class_name = class_name
        self.min_version = min_version
        self.max_version = max_version


@six.add_metaclass(abc.ABCMeta)
class PluginBase(object):
    """Base class for all VIF plugins."""

    def __init__(self, config):
        """
        Sets up the plugin using os_vif.objects.PluginConfig instance
        """
        self.config = config

    @abc.abstractmethod
    def do_plug(self, instance, vif):
        """
        Given a model of a VIF, perform operations to plug the VIF properly.

        :param instance: `nova.objects.Instance` object.
        :param vif: `os_vif.objects.VIF` object.
        :raises `processutils.ProcessExecutionError`. Plugins implementing
                this method should let `processutils.ProcessExecutionError`
                bubble up. The plug() method catches, logs, and raises a
                standardized os_vif library exception.
        """
        raise NotImplementedError('do_plug')

    @abc.abstractmethod
    def do_unplug(self, vif):
        """
        Given a model of a VIF, perform operations to unplug the VIF properly.

        :param vif: `os_vif.objects.VIF` object.
        :raises `processutils.ProcessExecutionError`. Plugins implementing
                this method should let `processutils.ProcessExecutionError`
                bubble up. The plug() method catches, logs, and raises a
                standardized os_vif library exception.
        """
        raise NotImplementedError('do_unplug')

    @abs.abstractmethod
    def get_supported_vifs(self):
        """
        Get a list of supported VIF object tyoes

        :returns: list of os_vif.plugin.PluginVIFSupport instances
        """
        raise NotImplementedError("get_supported_vifs")
