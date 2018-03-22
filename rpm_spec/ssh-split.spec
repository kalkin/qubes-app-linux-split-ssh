#
# The Qubes OS Project, http://www.qubes-os.org
#
# Copyright © 2017 Bahtiar `kalkin-` Gadimov <bahtiar@gadimov.de>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#

%{!?version: %define version %(cat version)}

Name:		qubes-ssh-split
Version:	%{version}
Release:	0%{dist}
Summary:	The Qubes service for secure ssh separation

Group:		Qubes
Vendor:		Invisible Things Lab
License:	GPL
URL:		http://www.qubes-os.org

Requires:   openssh
Requires:   nmap-ncat

%define _builddir %(pwd)

%description
The Qubes service for delegating ssh actions to other VM. The protections for
the ssh private key should be similar to running ‘ssh -A’ into the client AppVM.

%prep
# we operate on the current directory, so no need to unpack anything

%build

%install
install -D qubes-ssh-agent.service \
        $RPM_BUILD_ROOT/usr/lib/systemd/system/qubes-ssh-agent.service
install -D qubes.SshAgent $RPM_BUILD_ROOT/etc/qubes-rpc/qubes.SshAgent
install -D qubes-ssh-agent-proxy@.service \
        $RPM_BUILD_ROOT/usr/lib/systemd/system/qubes-ssh-agent-proxy@.service
install -D qubes-ssh-agent-proxy.socket \
        $RPM_BUILD_ROOT/usr/lib/systemd/system/qubes-ssh-agent-proxy.socket
install -D qubes-ssh-agent-proxy.sh $RPM_BUILD_ROOT/etc/profile.d/qubes-ssh-agent-proxy.sh


%post
if [ $1 -eq 1 ]; then
    systemctl enable qubes-ssh-agent
    systemctl enable qubes-ssh-agent-proxy.socket
fi

%preun
if [ $1 -eq 0 ]; then
    systemctl disable qubes-ssh-agent
    systemctl disable qubes-ssh-agent-proxy.socket
fi

%files
%attr(0664,root,root)
/usr/lib/systemd/system/qubes-ssh-agent.service
/usr/lib/systemd/system/qubes-ssh-agent-proxy@.service
/usr/lib/systemd/system/qubes-ssh-agent-proxy.socket
/etc/qubes-rpc/qubes.SshAgent
/etc/profile.d/qubes-ssh-agent-proxy.sh
%changelog
